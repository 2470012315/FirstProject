#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import allure
import pytest



# pytest用例函数
# @pytest.mark.parametrize("a,b",[('zz','123456'),('xz','123456'),('qs','123456')])
# def test_login(a,b):
#     """ 测试登陆用例"""
#     print("登陆")
#     print(a)
#     print(b)

# @pytest.mark.parametrize("test_input,expeted",test_datas)
# def test_login(test_input,expeted):
#     """ 测试登陆用例"""
#     # 获取输入数据
#     print("获取输入数据")
#     print(test_input["useranme"])
#     print(test_input["password"])
#     # 获取预期结果
#     print("获取预期结果")
#     print(expeted)

# @pytest.mark.parametrize("test_input,expeted",test_datas)
# def test_login(test_input,expeted):
#     """ 测试登陆用例"""
#     # 获取输入数据
#     print("获取输入数据")
#     print(test_input["useranme"])
#     print(test_input["password"])
#     # 获取预期结果
#     print("获取预期结果")
#     print(expeted)

# 模拟定义登陆接口
def login(username,password):
    """登陆"""
    print("输入账户： %s" % username)
    print("输入密码： %s" % password)
    # 返回
    return {"code":0,"msg":"success!"}

# 测试数据
test_datas = [
    # {"useranme":"zz1","password":"123456"} 是用例的输入数据
    # "success!" 是预期结果
    ({"username":"zz","password":"123456"},"success!"),
    ({"username":"xu","password":"111111"},"failed!"),
    ({"username":"qs","password":"123456"},"success!")
]

@allure.title("用例描述，测试输入:{test_input}")
@pytest.mark.parametrize("test_input,expeted",test_datas)
def test_login(test_input,expeted):
    """ 测试登陆用例"""
    # 获取输入数据
    # 获取函数返回结果
    result = login(test_input["username"],test_input["password"])
    # 断言
    assert result["msg"] == expeted


if __name__ == '__main__':
    # 生成报告数据源到result目录,存储json数据
    pytest.main(['test_a_title.py','--alluredir','./result3','--clean-alluredir'])
    # 基于json数据生成web报告工程
    os.system('allure generate ./result3/ -o ./report_allure3/ --clean')