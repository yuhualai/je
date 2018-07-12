#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '
from web.BasePage.BasePage import browser
from web.ElementPage.ArticlePage import ArticlePage

__author__ = 'hualai yu'

import unittest


class Article(unittest.TestCase):
    def setUp(self):
        self.driver = browser("chrome")
        self.login = ArticlePage(self.driver)
        self.login.open("http://chat.uat.zmops.cc/")
        self.login

    def tearDown(self):
        self.driver.quit()

    def login_case(self, username, psw, expect=True):
        self.login.mobile_test(username)
        self.login.password_test(psw)
        self.login.class_test()
        self.login.name_test()
        self.login.name_test1()
        # 判断昵称获取是否正确
        result = self.login.is_text_in_element(("class name", "name"), "蓓馨")
        expect_result = expect
        self.assertEquals(result, expect_result)

    def test_login_01(self):
        # 输入用户名和密码
        self.login_case("10000002850", "hello2850", True)

    def test_login_02(self):
        # 输入用户名和密码
        self.login_case("10000002850", "hello2850", True)

    # @Screen(driver)
    def test_login_03(self):
        # 输入用户名和密码
        self.login_case("10000002850", "hello2850", True)


