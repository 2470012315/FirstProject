#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 购物车登陆
def test_cart_login(browser):
    # 购物车登陆
    # 打开淘宝购物车的登陆页面
    browser.get("https://cart.taobao.com/cart.htm")

    # 定位到账户名文本框
    browser.find_element_by_id('fm-login-id').send_keys('19119282264')
    # 定位到密码
    browser.find_element_by_id('fm-login-password').send_keys('cema6666..')

    # 点击登陆按钮
    browser.find_element_by_xpath("//div[@class='fm-btn']").click()