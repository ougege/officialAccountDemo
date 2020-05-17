#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import random

class ShortUrl:
    def create(address):
      # newAddress = address.split('短网址', 1)
      url = 'https://create.ft12.com/go.php?m=index&a=urlCreate'
      method = 'POST'
      content_type = 'application/x-www-form-urlencoded; charset=UTF-8'
      value = "".join(random.choice("0123456789") for i in range(15))
      # 设置待创建的长网址
      bodys = {'url':address,'type':'8rr', 'random': value}
      # 配置headers
      headers = {'Content-Type':content_type}
      # 发起请求
      response = requests.post(url=url, data=bodys, headers=headers)
      # 读取响应
      # print(response.text['ErrMsg'])
      resDict = json.loads(response.text)
      if (resDict['status'] == '1'):
        return resDict['list']
      else:
        return resDict['err_msg']