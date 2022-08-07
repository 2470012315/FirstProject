#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
from time import sleep
from class06.p08.VAR.TAOBAO_VAR import *
from class06.p08.locate import allPages
from class06.p08.logic.shopping_page import GoodsSale


@allure.title("淘宝商品订购")
def test_goodsSale(browser):
    # 初始化业务流程
    goodssale = GoodsSale(browser)

    goodssale.open(TAOBAO_URL)

    # 搜索商品
    goodssale.goodsSearch("膳魔师")

    # 进行购物
    goodssale.shopping()

@allure.title("删除全部购物车的商品")
def test_del_goods(browser):
    # 复用商品购物流程
    goodssale = GoodsSale(browser)

    goodssale.open(TAOBAO_URL)

    # 搜索商品
    goodssale.goodsSearch("膳魔师")

    # 进行购物
    goodssale.shopping()

    with allure.step("打开购物车"):
        goodssale.open(CART_LOGIN_URL)

    with allure.step("全选商品"):
        goodssale.locator(*allPages.page_cartDetail_selectAll).click()
    sleep(3)

    with allure.step("点击删除按钮"):
        goodssale.locator(*allPages.page_cartDetail_delBtn).click()
    sleep(3)

    with allure.step("点击确认按钮"):
        goodssale.locator(*allPages.page_cartDetail_confirmBtn).click()
    sleep(3)