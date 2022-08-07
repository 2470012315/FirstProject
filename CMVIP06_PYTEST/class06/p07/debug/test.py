#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

from class06.p07.key_word.keyword import WebKeys
from class06.p07.locate import allPages

"""
    使用编写的脚本以debug模式启动谷歌浏览器,脚本内容如下
    chrome.exe --remote-debugging-port=9222
    必须通过脚本执行，使用os.system执行命令无效
"""
# os.popen("d:/chrome.bat")
# sleep(3)

# 加载浏览器驱动
options = webdriver.ChromeOptions()
options.debugger_address = '127.0.0.1:9222'
driver = webdriver.Chrome(options=options)
sleep(2)

# 加载浏览器驱动
wk = WebKeys(driver)

# 点击加入购物车
wk.locator(*allPages.page_goodsDetail_cartBtn).click()

sleep(1)

# 切换frame
el = wk.locator(*allPages.page_goodsDetail_loginFrame)
wk.change_frame(el)

# sleep(1)

# 填账号密码
wk.locator(*allPages.page_indexLogin_user).send_keys("19119282264")
# sleep(2)
wk.locator(*allPages.page_indexLogin_pwd).send_keys("cema6666..")
# sleep(1)
wk.locator(*allPages.page_indexLogin_loginBtn).click()
sleep(3)

# 切换到滑块的iframe
el = wk.locator('xpath', "//div[@id='login']//iframe")
wk.change_frame(el)
wk.slider_by_step("//center//span[@id='nc_1_n1z']")