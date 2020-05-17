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
# @robot.filter('天气')
# def start():
#     return Help.start()
# # 短网址
# @robot.filter(re.compile('短网址.*?'))
# def transUrl(message):
#     # return message.content
#     reply = TextReply(message=message, content=ShortUrl.create(message.content))
#     return reply
# # 歌曲搜索
# @robot.filter(re.compile('歌曲-.*?'))
# def searchMusic(message):
#     singleSong = Music163.searchSong(message.content)
#     dealArr = Music163.songUrl(singleSong)
#     return dealArr

@robot.text
def echo(message):
    content = message.content
    objArr = content.split('$')
    label = objArr[0]
    value = objArr[1]
    # print(label)
    # print(value)
    if (label == '短网址'):
        reply = TextReply(message=message, content=ShortUrl.create(value))
        return reply
    elif (label == '歌曲'):
        # singleSong = Music163.searchSong(value)
        # dealArr = Music163.songUrl(singleSong)
        # return dealArr
        return '开发中'
    elif (label == '天气'):
        return '开发中'
    else:
        return Help.start()

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
