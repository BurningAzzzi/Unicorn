#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-10-11
# Author: Master Yumi
# Email : yumi@meishixing.com

import hashlib   

def md5(text):
    """md5加密"""
    return hashlib.md5(text).hexdigest()

