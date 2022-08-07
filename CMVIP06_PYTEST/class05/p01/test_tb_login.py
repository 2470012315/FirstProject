#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver

# 浏览器对象的初始化
driver = webdriver.Chrome()

# 打开淘宝购物车的登陆页面
driver.get("https://cart.taobao.com/cart.htm")

# 定位到账户名文本框
driver.find_element_by_id('fm-login-id').send_keys('19119282264')
# 定位到密码
driver.find_element_by_id('fm-login-password').send_keys('cema6666..')

# 点击登陆按钮
driver.find_element_by_xpath("//div[@class='fm-btn']").click()