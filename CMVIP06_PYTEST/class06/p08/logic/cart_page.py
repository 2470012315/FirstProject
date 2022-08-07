#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
from time import sleep

from class06.p08.VAR.TAOBAO_VAR import *
from class06.p08.key_word.keyword import WebKeys

# 购车页面
from class06.p08.locate import allPages
from class06.p08.logic.cartLogin_page import CatLoginPage


class CartPage(WebKeys):
    # 商品结算
    @allure.step("商品结算")
    def pay(self):
        # 在报告里展示代码路径，方便查找
        with allure.step("流程代码路径：%s" % __file__):
            pass

        with allure.step("点击全选按钮"):
            self.locator(*allPages.page_cartDetail_selectAll).click()
            sleep(2)
        with allure.step("点击结算按钮"):
            self.locator(*allPages.page_cartDetail_payBtn).click()
            sleep(2)