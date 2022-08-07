#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

# 常规list嵌套元祖
# def return_data():
#     return [('zz','123456'),('xz','123456'),('qs','123456')]
#
# @pytest.mark.parametrize('data',return_data())
# def test_01(data):
#     print('\n' + data[0])
#     print('\n' + data[1])

# 常规list嵌套字典
# def return_data():
#     return [{'aaa': '1111'},{'bbb': '2222'},{'ccc': '333'}]
#
# @pytest.mark.parametrize('data',return_data())
# def test_01(data):
#     print(data)
#     print(type(data))

# 常规list嵌套字典
# def return_data():
#     return [{'name': 'zz',"age":"18"},{'name': 'xz',"age":"20"},{'name': 'qs',"age":"18"}]
#
# @pytest.mark.parametrize('data',return_data())
# def test_01(data):
#     print(data['name'])
#     print(data['age'])

# 纯字典
# def return_data():
#     return {'name': 'zz',"age":"18"}
#
# @pytest.mark.parametrize('data',return_data())
# def test_01(data):
#     print(data)
#     print(type(data))

# list嵌套list也行
def return_data():
    return [[1,2,3,4,5],[2,2,2,2,2],[4,4,4,4,4]]

@pytest.mark.parametrize('data',return_data())
def test_01(data):
    print(data)
    print(type(data))
    print(data[0])
    print(data[1])
    print(data[2])


if __name__ == '__main__':
    pytest.main(['-s','test_func03.py'])