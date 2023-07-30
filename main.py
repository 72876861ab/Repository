# coding: utf-8
# 我是谁
import pytest,os
if __name__ == '__main__':
    pytest.main(["-vs",
                 "--capture=sys",
                 "Test_apiframework.py",
                 "--clean-alluredir","--alluredir=allure-results"])

os.system("allure generate ./allure-results/ -o ./report_allure --clean")

