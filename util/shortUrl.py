#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

class ShortUrl:
    def create(address):
      newAddress = address.split('短网址', 1)
      host = 'https://dwz.cn'
      path = '/admin/v2/create'
      url = host + path
      method = 'POST'
      content_type = 'application/json'
      # TODO: 设置Token
      token = 'e066525b23353a9ff4f0b0b896dce084'
      # TODO：设置待创建的长网址
      bodys = {'Url':newAddress[1],'TermOfValidity':'1-year'}
      # 配置headers
      headers = {'Content-Type':content_type, 'Token':token}
      # 发起请求
      response = requests.post(url=url, data=json.dumps(bodys), headers=headers)
      # 读取响应
      # print(response.text['ErrMsg'])
      resDict = json.loads(response.text)
      if (resDict['ErrMsg'] == ''):
        return resDict['ShortUrl']
      else:
        return resDict['ErrMsg']