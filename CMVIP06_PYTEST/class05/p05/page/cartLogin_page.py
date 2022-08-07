#!/usr/bin/env python
# -*- coding: utf-8 -*-
from class05.p05.key_word.keyword import WebKeys
from class05.p05.page import allPages
# 以页面为单位，封装常用的行为操作代码和元素定位代码



class CatLoginPage(WebKeys):
    #登陆操作
    def login(self,username,passwd):
        self.open("https://cart.taobao.com/cart.htm")
        # 定位到账户名文本框
        # self.locator(allPages.page_indexLogin_user[0],allPages.page_indexLogin_user[1]).send_keys(username)
        self.locator(*allPages.page_indexLogin_user).send_keys(username)
        # 定位到密码框
        self.locator(*allPages.page_indexLogin_pwd).send_keys(passwd)
        # 点击登陆按钮
        self.locator(*allPages.page_indexLogin_loginBtn).click()



