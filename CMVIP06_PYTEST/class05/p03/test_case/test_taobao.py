#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
# 购物车登陆


# 跳过用例
from class05.p03.key_word.keyword import WebKeys


@pytest.mark.skip
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

# 使用关键字驱动模式实现购物车登陆
def test_case_login2(browser):
    # 初始化工具类，传递浏览器对象
    wk = WebKeys(browser)
    wk.open("https://cart.taobao.com/cart.htm")
    # 定位到账户名文本框
    wk.locator('id','fm-login-id').send_keys('19119282264')
    # 定位到密码框
    wk.locator('id','fm-login-password').send_keys('cema6666..')

    # 点击登陆按钮
    wk.locator('xpath',"//div[@class='fm-btn']").click()