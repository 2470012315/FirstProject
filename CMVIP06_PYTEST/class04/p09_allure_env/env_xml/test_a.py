#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 模拟定义登陆接口
import os

import pytest


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

# @pytest.mark.parametrize("test_input,expeted",test_datas)
# def test_login(test_input,expeted):
#     """ 测试登陆用例"""
#     # 获取输入数据
#     # 获取函数返回结果
#     result = login(test_input["username"],test_input["password"])
#     # 断言
#     assert result["msg"] == expeted

def test_case02():
    assert 1 == 1


if __name__ == '__main__':
    # 1.allure报告可以记录用例每次执行的情况，方便跟踪用例的成功率，数据保留在json文件中
    # 2.会带来一个问题，当你代码里的用例删除或者更换名称后，依然会记录之前的用例报告
    # 3. --clean-alluredir 每次用例执行之前先清空allure的报告记录
    pytest.main(['test_a.py','--alluredir','./result',])
    # 4. 这里的clean 只是让报告可重新生成，生成的结果，会保留之前的用例执行记录
    os.system('allure generate ./result/ -o ./report_allure/ --clean')