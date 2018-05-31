#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import configparser

import okex_future

class TestOKExFuture(unittest.TestCase):
    def setUP(self):
        CONFIG_FILE = '../config/api.ini'

        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        self.__url = okex_future.DOMAIN
        print(self.__url)

    def test_init(self):
        print(self.__url)
        self.assertEqual(self.__url, 'www.okex.com')