#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
from selenium import  webdriver
from time import sleep
# 定义关键字驱动类/工具类/基类
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver import ActionChains


class WebKeys:
    # 构造方法,用于接收driver对象
    def __init__(self,driver):
        self.driver = driver
        # 编代码用，写完删掉
        # self.driver = webdriver.Chrome()

    # 打开浏览器
    @allure.step("打开浏览器：{url}")
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

    # 获取title，获取网页标题栏
    def get_title(self):
        return self.driver.title

        # 获取页面text，获取页面文本，使用xpath定位
        def get_text(self, path):
            return self.locator("xpath", path).text

    # 窗口切换
    def change_window(self, n):
        # 获取句柄
        handles = self.driver.window_handles
        # 切换到原始页面,n = 0
        # 切换句柄到第二个页面,n = 1 ,以此类推
        self.driver.switch_to.window(handles[n])

    # 关闭当前窗口
    def close_window(self):
        self.driver.close()

    # 鼠标点击并悬停
    def mouse_hold(self, url):
        btn = self.driver.find_elements_by_xpath(url)[0]
        action = ActionChains(self.driver)
        action.click_and_hold(btn).perform()

    # 切换frame
    def change_frame(self, a):
        self.driver.switch_to.frame(a)

    # 切换回主框架
    def change_defaultFrame(self):
        self.driver.switch_to.default_content()

    # 网页title检查
    @allure.step("网页title检查:{expect_title}")
    def assert_title(self, expect_title):
        # 结果检查
        result = self.driver.title
        with allure.step("结果检查：（预期）{1} in （实际）{0}".format(result, expect_title)):
            assert expect_title in result
        sleep(2)

    # 滑动解锁
    @allure.step("滑动解锁")
    def slider(self, url):
        # 滑动解锁
        # 定位滑动块
        # slider = driver.find_element_by_class_name("cpt-drop-btn")[0]
        # slider = driver.find_elements_by_class_name("cpt-drop-btn")[0]
        slider = self.driver.find_elements_by_xpath(url)[0]
        action = ActionChains(self.driver)
        action.click_and_hold(slider).perform()
        action.move_by_offset(350, 0).perform()

    # 滑动解锁
    @allure.step("滑动解锁,慢滑版")
    def slider_by_step(self, url):
        slider = self.driver.find_elements_by_xpath(url)[0]
        action = ActionChains(self.driver)
        # 单击并按下鼠标左键
        action.click_and_hold(slider).perform()
        for index in range(300):
            try:
                # 移动鼠标，第一个参数为 x 坐标距离，第二个参数为 y 坐标距离
                action.move_by_offset(10, 0).perform()
            except UnexpectedAlertPresentException:
                break
            # 重置 action
            # action.reset_actions()
            sleep(0.1)  # 等待停顿时间

    def locate_by_js(self):
        # js = "document.querySelector({}).scrollIntoView(true);".format(css_url)
        js = "document.querySelector('center span#nc_1_n1z').scrollIntoView(true);"
        self.driver.execute_script(js)