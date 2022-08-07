#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

def test_baidu_case01(browser):
    driver = browser
    driver.get("http://www.baidu.com")
    sleep(2)
    # 定位到百度搜索框，然后输入关键字
    driver.find_element_by_id('kw').send_keys('狗狗币')
    sleep(2)
    # 定位到搜索按钮，点击搜索
    driver.find_element_by_id('su').click()
    sleep(2)
    assert driver.title == "11狗狗币_百度搜索"
