import requests
import time
import tkinter.messagebox
from tkinter import *
import tkinter as tk
# 1.Github项目及API接口数据
api = 'https://api.github.com/repos/cleverrat-rat/amarantine-aiml'
webpage = "https://cleverrat-rat.github.io/cleverrat331.github.io/"
# 2.发送请求，获取数据
allinfo = requests.get(api).json()  
# 3.解析想要的数据，并打印
curupdate = allinfo['updated_at']
print(curupdate)
last_update = curupdate
allinfo = requests.get(api).json()
curupdate = allinfo['updated_at']
print(curupdate)
# 假设第一次运行之前，不知道上次的更新时间 # 如果last_update 为 none，会执行下面的语句，把当前的时间给到上次时间
if not last_update:
    tkinter.messagebox.showinfo('更新','当前没有更新')
    last_update = curupdate

    # 第一次两个时间相等，不会执行
    # 假设10分钟后，cur_update更新，那么就会自动打开网页
    # 接下来，把 当前时间 赋值 给上次时间
    # 开始新一轮的监测
if last_update < curupdate:
    webbrowser.open(webpage)
