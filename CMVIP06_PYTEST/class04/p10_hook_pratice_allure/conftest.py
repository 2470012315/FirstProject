#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    # 用例前置
    # 定义全局变量，方便文件里的其他函数调用
    global driver
    # 初始化浏览器对象并启动浏览器
    driver = webdriver.Chrome()
    # 返回浏览器对象给用例
    yield driver
    # 用例的后置处理：关闭浏览器
    driver.quit()
    print("test end!!")

"""
    装饰器@pytest.hookimpl(hookwrapper=True)等价于 @pytest.mark.hookwrapper
    作用：
    a:可以获取测试用例的信息，比如用例函数的描述
    b:可以获取测试用例的执行结果，yield，返回一个result对象
"""
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    # 可以获取测试用例的执行结果，yield，返回一个result对象
    out = yield
    """
        从返回一个result对象（out）获取调用结果的测试报告，返回一个report对象
        report对象的属性
        包括when(setup,call,teardown三个值)、nodeid(测试用例的名字)、
        outcome(用例的执行结果：passed,failed)
    """
    report = out.get_result()
    # 仅仅获取用例call阶段的执行结果，不包含setup和teardown
    if report.when == 'call':
        # 获取用例call执行结果为结果为失败的情况
        xfail = hasattr(report,"wasxfail")
        if(report.skipped and xfail) or (report.failed and not xfail):
            # 添加allure报告截图
            with allure.step("添加失败截图。。"):
                # 使用allure自带的添加附件的方法：三个参数分别为：源文件、文件名、文件类型
                allure.attach(driver.get_screenshot_as_png(),"失败截图",
                              allure.attachment_type.PNG)
