# jiandan.net-ooxx-urllib-python
 Python-urllib.request-"jiandan.net/ooxx"


作者 @shinkaimonka
"urllib.request";"os";"base64";"easygui";"datetime";"threading";"sys"
#均为python自带模块 python3.x
2020-08测试可用
===========================================================
思路:因为jiandan.net/ooxx的url从老污龟(误)的视频里的数字变成了base64编码，所以小甲鱼视频里的示例已经无法使用。研究得知，url进行base64解码后
格式为:%Y%m%d-page，比如20200818-93转为base64后为MjAyMDA4MTgtOTM= ，再把字符串拼合为"http://jiandan.net/ooxx/MDA4MTgtOTM=#comments",就可以得到要找的url了。
开始爬链接时会从最新一页开始逐页递减(日期取系统时间),最后爬到第一页停止，爬取的数据在/OOXX文件夹(当然，可以随时停止)。我也做了个控制用的gui窗口(easygui)
===========================================================
具体大家可以自己试一试，经我测试应该没什么bug(吧)?(flag) o(╥﹏╥)o
2020-08-18深夜留