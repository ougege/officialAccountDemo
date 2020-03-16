#coding:utf-8
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
robot = WeRoBot(token='ougegeceshi')
# 文本消息
@robot.filter('天气')
def start():
    return Help.start()
# 短网址
@robot.filter(re.compile('短网址.*?'))
def transUrl(message):
    # return message.content
    reply = TextReply(message=message, content=ShortUrl.create(message.content))
    return reply
# 歌曲搜索
@robot.filter(re.compile('歌曲-.*?'))
def searchMusic(message):
    singleSong = Music163.searchSong(message.content)
    dealArr = Music163.songUrl(singleSong)
    return dealArr
# 图片消息
@robot.image
def img(message):
    return message.img
# 被关注
@robot.subscribe
def showWiki():
    return Help.start()
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
