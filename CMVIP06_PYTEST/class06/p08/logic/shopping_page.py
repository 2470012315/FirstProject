#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
from time import sleep

from class06.p08.VAR.TAOBAO_VAR import *
from class06.p08.key_word.keyword import WebKeys
from class06.p08.locate import allPages
from class06.p08.logic.cartLogin_page import CatLoginPage
from class06.p08.logic.cart_page import CartPage


class GoodsSale(WebKeys):
    @allure.step("淘宝搜索商品：{goodsname}")
    def goodsSearch(self,goodsname):
        """
        :param goodsname: 搜索商品名
        :return:
        """
        # 在报告里展示代码路径，方便查找
        with allure.step("流程代码路径：%s" % __file__):
            pass

        with allure.step("搜索："+goodsname):
            self.locator(*allPages.page_index_search).send_keys(goodsname)
            self.locator(*allPages.page_index_searchBtn).click()
        sleep(2)
        # 网页title检查
        self.assert_title(goodsname)

    @allure.step("登陆框登陆")
    def login_frame(self,username,passwd,expect_tile):
        # 在报告里展示代码路径，方便查找
        with allure.step("流程代码路径：%s" % __file__):
            pass

        el = self.locator(*allPages.page_goodsDetail_loginFrame)
        with allure.step("切换到登陆框frame"):
            self.change_frame(el)
        sleep(3)

        #执行登陆流程
        # 调用登陆流程
        with allure.step("调用登陆流程"):
            # 调用登陆流程
            login = CatLoginPage(self.driver)
            login.login(USERNAME, PASSWD, expect_tile)

        with allure.step("切换回默认的frame"):
            self.change_defaultFrame()
        sleep(3)

        # 结果检查
        self.assert_title(expect_tile)
        sleep(2)


    @allure.step("淘宝购买商品")
    def shopping(self):
        # 在报告里展示代码路径，方便查找
        with allure.step("流程代码路径：%s" % __file__):
            pass

        '''
            找不到元素，也能继续运行
            方法1:
                try:
                 elem = driver.find_element_by_name('...')
                except:
                 pass
            方法2：
                elems = driver.find_elements_by_name('...')
                if len(elems)>0:
                   elem = elems[0]
        '''
        with allure.step("判断是否有登陆页，有就登陆"):
            try:
                # 调用登陆流程
                login = CatLoginPage(self.driver)
                login.login(USERNAME,PASSWD,'淘宝')
            except:
                with allure.step("未出现登陆页，跳过"):
                    pass

        with allure.step("选择二手"):
            self.locator(*allPages.page_searchResults_old).click()
        sleep(2)

        with allure.step("选择商品"):
            self.locator(*allPages.page_searchResults_good).click()
        sleep(2)

        with allure.step("窗口切换"):
            self.change_window(1)
        sleep(1)

        with allure.step("点击加入购物车按钮"):
            self.locator(*allPages.page_goodsDetail_cartBtn).click()
        sleep(1)

        with allure.step("判断是否有登录框，有就登陆"):
            try:
                # 调用登录框登陆流程
                self.login_frame(USERNAME,PASSWD,'成功')
            except:
                with allure.step("未出现登陆框，跳过"):
                    pass

        # with allure.step("点击购物结算按钮"):
        #     self.locator(*allPages.page_goodsDetail_payBtn).click()
        #     sleep(3)
        #     # 结果检查
        #     self.assert_title("我的购物车")
        #
        # sleep(5)
        #
        # # 调用购物车结算流程
        # cartPay = CartPage(self.driver)
        # cartPay.pay()