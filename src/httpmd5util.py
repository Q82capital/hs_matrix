#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 用于进行http请求，以及MD5加密，生成签名的工具类
# copy from https://github.com/OKCoin/rest/blob/master/python/HttpMD5Util.py

import hashlib
import http.client
import urllib
import json
import time


def build_sign(params, secret_key):
    sign = ''
    for key in sorted(params.keys()):
        sign += key + '=' + str(params[key]) + '&'
    data = sign + 'secret_key=' + secret_key
    return hashlib.md5(data.encode("utf8")).hexdigest().upper()


def http_get(url, resource, params=''):
    conn = http.client.HTTPSConnection(url, timeout=10)
    temp_params = urllib.parse.urlencode(params)
    conn.request("GET", resource + '?' + temp_params)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    return json.loads(data)


def http_post(url, resource, params):
    # test: curl -s 'https://www.okex.com/api/v1/ticker.do?symbol=ltc_btc' | jq .
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
    }
    conn = http.client.HTTPSConnection(url, timeout=10)
    temp_params = urllib.parse.urlencode(params)
    print(temp_params)
    conn.request("POST", resource, temp_params, headers)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    params.clear()
    conn.close()
    return data
