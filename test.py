coding:utf-8
import sys, random, json, re
sys.path.append('./util/')
from werobot import WeRoBot
from werobot.replies import TextReply, ArticlesReply, Article, MusicReply
# 帮助wiki
from help import Help
# 转换短网址
from shortUrl import ShortUrl
# 歌曲搜索
from music163 import Music163

value = 'http://baidu.com'
ShortUrl.create(value)
