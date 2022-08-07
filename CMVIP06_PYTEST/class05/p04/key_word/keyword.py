#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import  webdriver

# 定义关键字驱动类/工具类/基类
class WebKeys:
    # 构造方法,用于接收driver对象
    def __init__(self,driver):
        self.driver = driver
        # 编代码用，写完删掉
        # self.driver = webdriver.Chrome()

    # 打开浏览器
    def open(self,url):
        self.driver.get(url)

    # 元素定位
    def locator(self,name,value):
        """
        :param name: 元素定位的方式
        :param value: 元素定位的路径
        :return:
        """
        el = self.driver.find_element(name,value)
        # 将定位的元素框出来
        self.locater_station(el)
        return el

    # 显示定位的地方，方便确认定位位置
    def locater_station(self,element):
        self.driver.execute_script(
            "arguments[0].setAttribute('style',arguments[1]);",
            element,
            "border: 2px solid green" # 边框，green绿色
        )