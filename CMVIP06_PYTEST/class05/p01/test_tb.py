#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from time import sleep

# 淘宝登陆验证码解决方案
"""
    使用编写的脚本以debug模式启动谷歌浏览器，脚本内容：
    chrome.exe --remote-debugging-port=9222
    必须通过os.popen执行，通过os.system执行命令无效
"""
# os.popen("d:/chrome.bat")
# sleep(5)

# 加载浏览器驱动
options = webdriver.ChromeOptions()
options.debugger_address = '127.0.0.1:9222'
driver = webdriver.Chrome(options=options)
sleep(2)


# 打开淘宝购物车的登陆页面
# driver.get("https://cart.taobao.com/cart.htm")
#
# # 定位到账户名文本框
# driver.find_element_by_id('fm-login-id').send_keys('19119282264')
# # 定位到密码
# driver.find_element_by_id('fm-login-password').send_keys('cema6666..')
#
# # 点击登陆按钮
# driver.find_element_by_xpath("//div[@class='fm-btn']").click()

# 点击商品链接
# driver.find_element_by_xpath("//ul/li[2]/div/div[2]/div/a").click()

# 浏览器页签切换
# 获取所有的浏览器页签（句柄）
handls = driver.window_handles
print(handls)
# 切换到新开的第二个页签，下标填1就可以了，下标都是从0开始的
driver.switch_to.window(handls[1])

# 在页签，选择颜色
driver.find_element_by_xpath('//ul[@data-property="颜色分类"]/li').click()