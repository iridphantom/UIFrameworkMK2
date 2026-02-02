"""
    ERP系统进行登录操作
    UnitTest + DDT + YAML
"""
import unittest

from ddt import ddt, file_data
from base.web_keys import WebKeys

@ddt
class Login(unittest.TestCase):

    @file_data('../data/login.yaml')
    def test_01_login(self, **kwargs):
        driver = WebKeys('FireFox')
        driver.open(kwargs['url'])
        # driver.input(**kwargs['inputUsername'])   # 有缓存 就不输入了
        # driver.input(**kwargs['inputPassword'])
        driver.input(**kwargs['inputCode'], content=driver.get_code(**kwargs['codeImg']))
        driver.click(**kwargs['loginButton'])
        driver.wait(kwargs['wait_time'])