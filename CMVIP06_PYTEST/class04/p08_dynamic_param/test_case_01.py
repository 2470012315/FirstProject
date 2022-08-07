#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import allure


# 接口用例描述例子
import pytest

desc = "<font color='red'>请求URL:</font>{}<Br/>" \
       "<font color='red'>请求类型:</font>{}<Br/>" \
       "<font color='red'>期望结果:</font>{}<Br/>" \
       "<font color='red'>实际结果:</font>{}<Br/>" \
       .format("http://www.baidu.com","post","200","404")

@allure.description("简单描述")
def test_dynamic_desc():
    # 断言成功之后，变更描述信息
    assert 1 == 2
    allure.dynamic.description(desc)

@allure.title("原始标题")
def test_dynamic_title():
    assert 2 + 2 == 4
    allure.dynamic.title("当断言成功时，用例标题会动态更新")

@allure.title("参数化用例标题：添加{param1}和{param2}")
@pytest.mark.parametrize('param1,param2,expected',[(2,2,4),(1,2,5)])
def test_with_param_title(param1,param2,expected):
    assert param1 + param2 == expected
    allure.dynamic.title("变更标题")

if __name__ == '__main__':
    pytest.main(['-s','test_case_01.py','--alluredir','./result','--clean-alluredir'])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')