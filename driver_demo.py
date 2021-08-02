#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 23:16
# @Author  : ywb
# @Site    : selenium原理相关的代码
# @File    : driver_demo.py
# @Software: PyCharm

import time


def selenium_test(debug_flag=True):
    if debug_flag:
        from selenium import webdriver
        # 创建浏览器对象
        driver = webdriver.Chrome()
        # 浏览器访问指定的url
        driver.get('http:www.baidu.com')
        # 元素定位，先获取webElement, 然后再考虑元素如何操作
        wb_input = driver.find_element_by_xpath('//*[@id="kw"]')
        # 输入内容5
        wb_input.send_keys("三国演义")
        wb_button = driver.find_element_by_id('su')
        # 点击操作
        wb_button.click()
        # webdriver是服务端代理，当自动化结束时，需要释放资源
        time.sleep(5)
        driver.quit()
    else:
        from selenium.webdriver.chrome.webdriver import WebDriver
        from selenium.webdriver.common.by import By
        # 创建浏览器对象
        wb = WebDriver(executable_path="chromedriver")
        # 浏览器访问指定的url
        wb.get("http:www.baidu.com")
        wb.execute('get', {'url': 'http:www.baidu.com'})
        # 元素定位，先获取webElement, 然后再考虑元素如何操作
        wb_input = wb.execute("findElement", {
            'using': By.XPATH,
            'value': '//*[@id="kw"]'})['value']
        # 输入内容
        wb_input._execute("sendKeysToElement",
                          {'text': "三国演义",
                           'value': ''})
        wb_button = wb.execute("findElement", {
            'using': By.ID,
            'value': 'su'})['value']
        # 点击操作
        wb_button._execute("clickElement")
        time.sleep(5)
        wb.quit()


if __name__ == '__main__':
    selenium_test()
