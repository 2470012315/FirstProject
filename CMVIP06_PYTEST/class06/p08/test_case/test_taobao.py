#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from time import sleep
from class06.p08.VAR.TAOBAO_VAR import *
from class06.p08.data import yaml_driver
from class06.p08.key_word.keyword import WebKeys

# 跳过用例
# 购物车登陆
from class06.p08.locate import allPages
from class06.p08.logic.cartLogin_page import CatLoginPage
from class06.p08.logic.cart_page import CartPage

# 实现购物车结算
# def test_case_pay(browser):
#     # 初始化购物车页面对象
#     cartPage = CartPage(browser)
#     cartPage.pay()

@allure.title("淘宝搜索")
@pytest.mark.parametrize('data',yaml_driver.load_yaml('./data/taobao_search.yaml'))
def test_taobao_search(browser,data):
    # 初始化工具类
    wk = WebKeys(browser)

    with allure.step("打开淘宝首页"):
        wk.open(TAOBAO_URL)
    sleep(2)

    with allure.step("淘宝搜索："+data["txt"]):
        wk.locator(*allPages.page_index_search).send_keys(data["txt"])
        wk.locator(*allPages.page_index_searchBtn).click()

    allure.dynamic.title("淘宝搜索："+data["txt"])