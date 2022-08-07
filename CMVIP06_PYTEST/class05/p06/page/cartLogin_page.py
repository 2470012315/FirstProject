#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
from time import sleep
from class05.p06.key_word.keyword import WebKeys
from class05.p06.page import allPages
# 以页面为单位，封装常用的行为操作代码和元素定位代码



class CatLoginPage(WebKeys):
    #登陆操作
    @allure.step("登陆")
    def login(self,username,passwd):
        # 在报告里展示代码路径，方便查找
        with allure.step("流程代码路径：%s" % __file__):
            pass

        with allure.step("打开网页"):
            self.open("https://cart.taobao.com/cart.htm")
        with allure.step("输入账户"):
            # 定位到账户名文本框
            self.locator(*allPages.page_indexLogin_user).send_keys(username)
        with allure.step("输入密码"):
            # 定位到密码框
            self.locator(*allPages.page_indexLogin_pwd).send_keys(passwd)
        with allure.step("点击登陆"):
            # 点击登陆按钮
            self.locator(*allPages.page_indexLogin_loginBtn).click()

        sleep(3)

        # 登录后的结果检查
        result = self.get_title()
        expect = "购物车"
        with allure.step("结果检查：（预期）{1} in 实际{0}".format(result,expect)):
            assert expect in result

        sleep(3)


