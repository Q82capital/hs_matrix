#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import httpmd5util


class TestHttpmd5util(unittest.TestCase):
    def test_build_sign(self):
        self.assertEqual(httpmd5util.build_sign({'a': '1', 'b': '2', 'c': '3'}, '123'),
                         '91A5439DDA3174F5A88299D767DE3519', 'build_sign FAILED')

    def test_http_post(self):
        # curl -s 'https://www.okex.com/api/v1/ticker.do?symbol=ltc_btc' | jq .
        url = 'www.okex.com'
        resource = '/api/v1/ticker.do'
        params = {'symbol': 'ltc_btc'}
        json = httpmd5util.http_get(url, resource, params)
        print(json)
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()
