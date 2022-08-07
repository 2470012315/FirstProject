#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import pytest


def run():
    pytest.main(['-v',
                 '--alluredir','./result','--clean-alluredir'])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')

if __name__ == '__main__':
    run()