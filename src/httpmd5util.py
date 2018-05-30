#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# 用于进行http请求，以及MD5加密，生成签名的工具类
# copy from https://github.com/OKCoin/rest/blob/master/python/HttpMD5Util.py

import hashlib


def build_sign(params, secret_key):
    sign = ''
    for key in sorted(params.keys()):
        sign += key + '=' + str(params[key]) + '&'
    data = sign + 'secret_key=' + secret_key
    return hashlib.md5(data.encode("utf8")).hexdigest().upper()
