#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
from time import sleep
from class06.p08.key_word.keyword import WebKeys
from class06.p08.locate import allPages


# 以页面为单位，封装常用的行为操作代码和元素定位代码



class CatLoginPage(WebKeys):
    #登陆操作
    @allure.step("登陆")
    def login(self,username,passwd,expect_tile):
        """
        :param username:
        :param passwd:
        :param expect_tile: 登录后断言，期望网页title包含字符串
        :return:
        """

        # 在报告里展示代码路径，方便查找
        with allure.step("流程代码路径：%s" % __file__):
            pass

        with allure.step("输入账户"):
            # 定位到账户名文本框
            self.locator(*allPages.page_indexLogin_user).send_keys(username)
        sleep(2)
        with allure.step("输入密码"):
            # 定位到密码框
            self.locator(*allPages.page_indexLogin_pwd).send_keys(passwd)
        sleep(2)
        with allure.step("点击登陆"):
            # 点击登陆按钮
            self.locator(*allPages.page_indexLogin_loginBtn).click()
        sleep(3)

        # 结果检查
        self.assert_title(expect_tile)
        sleep(2)


