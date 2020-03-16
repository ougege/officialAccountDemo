#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

class Music163:
    # api 地址:http://doc.itooi.cn/#/
    # 搜索歌曲Id
    def searchSong(musicName):
      newMusicName = musicName.split('歌曲-', 1)
      defaulUrl = 'https://v1.itooi.cn/netease/search?type=song&pageSize=1&page=0&'
      searchStr = 'keyword=' + newMusicName[1]
      url = defaulUrl + searchStr
      method = 'GET'
      # 配置headers
      # content_type = 'application/json'
      # headers = {'Content-Type':content_type}
      # 发起请求
      response = requests.get(url)
      # 读取响应
      resDict = json.loads(response.text)
      songIds = resDict['data']['songs']
      name = songIds[0]['name']
      singer = songIds[0]['ar'][0]['name']
      id = songIds[0]['id']
      singleSong = {'name': name, 'singer': singer, 'id': id}
      return singleSong
    def songUrl(singleSong):
      tempArr = []
      defaulUrl = 'https://v1.itooi.cn/netease/url?quality=320&isRedirect=0&'
      searchStr = 'id=' + str(singleSong['id'])
      url = defaulUrl + searchStr
      method = 'GET'
      # 发起请求
      response = requests.get(url)
      # 读取响应
      resDict = json.loads(response.text)
      name = singleSong['name']
      singer = singleSong['singer']
      url = resDict['data']
      return [name, singer, url]