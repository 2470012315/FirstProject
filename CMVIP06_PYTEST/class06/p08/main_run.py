#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pytest


def run():
    pytest.main(['-v',
                 '--alluredir','./report/result','--clean-alluredir',
                 './test_case/test_taobao2.py'
                 # '--allure-no-capture'
                 ])
    os.system('allure generate ./report/result/ -o ./report/report_allure/ --clean')

if __name__ == '__main__':
    run()