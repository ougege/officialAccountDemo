class Help:
  def start():
    reply = '帮助文档\n'
    reply_1 = '【1】 查询天气: 城市+天气,例如“杭州$天气”\n'
    reply_2 = '【2】 短网址: 输入“短网址$链接”转成短网址\n'
    reply_3 = '【3】 搜歌: 输入“歌曲$歌名”搜索歌曲,例如(歌曲$男孩)\n'
    return reply + reply_1 + reply_2 + reply_3