#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pytest

if __name__ == '__main__':
    pytest.main(['--alluredir', './result', '--clean-alluredir'])
    # 4. 这里的clean 只是让报告可重新生成，生成的结果，会保留之前的用例执行记录
    os.system('allure generate ./result/ -o ./report_allure/ --clean')