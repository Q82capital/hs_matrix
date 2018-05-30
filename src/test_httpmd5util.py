#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import unittest
import httpmd5util


class TestHttpmd5util(unittest.TestCase):
    def test_build_sign(self):
        self.assertEqual(httpmd5util.build_sign({'a': '1', 'b': '2', 'c': '3'}, '123'),
                         '91A5439DDA3174F5A88299D767DE3519', 'build_sign FAILED')


if __name__ == '__main__':
    unittest.main()
