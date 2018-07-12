#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

from web.BasePage.BasePage import Action

__author__ = 'hualai yu'


class ArticlePage(Action):
    mobile = ("name", "mobile")
    password = ("name", "password")
    className = ("class name", "iQuOpA")
    name = ("class name", "gLuigJ")
    name1 = ("class name", "dwQpoy")

    def mobile_test(self, username):
        self.send_keys(self.mobile, username)

    def password_test(self, psw):
        self.send_keys(self.password, psw)

    def class_test(self):
        self.click(self.className)

    def name_test(self):
        clicks = self.texts(self.name,1)
        return clicks

    def name_test1(self):
        self.click(self.name1)
