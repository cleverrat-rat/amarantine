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
last_update = curupdate
print("官网上次更新时间:"+curupdate)

