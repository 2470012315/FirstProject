#!/usr/bin/env python
# -*- coding: utf-8 -*-


from class05.p04.key_word.keyword import WebKeys

# 以页面为单位，封装常用的行为操作代码和元素定位代码
class CatLoginPage(WebKeys):
    #登陆操作
    def login(self,username,passwd):
        self.open("https://cart.taobao.com/cart.htm")
        # 定位到账户名文本框
        self.locator('id', 'fm-login-id').send_keys(username)
        # 定位到密码框
        self.locator('id', 'fm-login-password').send_keys(passwd)
        # 点击登陆按钮
        self.locator('xpath', "//div[@class='fm-btn']").click()



