#Amarantine 1.10 by cleverrat
#Date :
from tkinter import *
import tkinter as tk
import aiml
from tkinter import scrolledtext
import sys
import os
import time
import threading
import tkinter.font as tkFont
import tkinter.messagebox
import pyttsx3
time.sleep(0.3)
print("Anarantine Logs")
time.sleep(0.2)
print("Loading...")
time.sleep(0.4)
def com():
    os.system("start https://cleverrat-rat.github.io/cleverrat331.github.io/")
def down():
    os.system("update.py")#垃圾自动更新 根本没卵用
def teacher():#aiml教程
    rooter = tk.Tk()
    enres = StringVar() #设置变量
    rooter.title("AIML教程") #设置窗口标题
    rooter.minsize(730, 400) #固定窗口大小
    rooter.maxsize(730, 400) #固定窗口大小
    rooter.configure(bg='black')#设置背景色
    rooter.geometry("250x150+800+450")  #固定串口位置
    #rooter.iconbitmap("LOGO.ico")#窗口图标  ——>未知原因 标题图标废了
    # 对话消息框设置成滚动文本框
    scrolW = 100 # 设置文本框的长度
    scrolH = 30 # 设置文本框的高度
    fucker = scrolledtext.ScrolledText(rooter, width=scrolW, height=scrolH,wrap=tk.WORD,bg="dimgray",fg="darkorange")#设置颜色
    fucker.grid(row=1,column=0)#固定位置
def test():#测试编写的语料库 不过aiml好像又被整坏
           #所以这个是废的
    alice_path = './core'  
    alice = aiml.Kernel()  
    alice.learn("创意.xml") 
    alice.respond('LOAD CY') 
def claire():#打开文件
    os.system("创意.aiml")
def XS():#语料库制作窗口
    xs = tk.Tk()
    xs.title("制作语料库")
    xs.configure(bg='dimgray')
    button = Button(xs,text="制作语料库",font=("微软雅黑",10),bg="dimgray",fg="SpringGreen",width=35,height=2,command=claire)
    button.grid(row=0,column=0,sticky=E)#
    button = Button(xs,text="AIML教程",font=("微软雅黑",10),bg="dimgray",fg="SpringGreen",width=35,height=2,command=teacher)
    button.grid(row=1,column=0,sticky=E)#
def CL():#清除brn文件
    os.system("del AIの脑.brn")
    time.sleep(1)
    print("已清除，AI已废")
def clean():#清除自动学习的文件
    os.system("del 自动学习.aiml")
    os.system("del simple_rules.db.dir")
    os.system("del simple_rules.db.bak")    
    time.sleep(1)
    print("已清除，AI记忆")
def GIT():#打开GitHub
    os.system("start https://github.com/cleverrat-rat/amarantine-aiml/issues")
def songs():#播放主题曲
    os.system("start https://tonzhon.com/search?keyword=amarantine")
def sbb():
    time.sleep(1)#假的反馈 (狗头)
    tkinter.messagebox.showinfo('反馈/建议','感谢您的反馈或建议！')
def groups(): #假的语言设置
    groups = tk.Tk()
    groups.title("AI语言偏好设置")
    group = LabelFrame(groups, text="选择Amarantine的语言风格")
    group.pack(padx=10, pady=10)
    
    LANGS = [
    ("温柔", 1) ,
    ("正常", 2) ,
    ("超凶", 3) ,
    ("喷子", 4)]
    
    v = IntVar()
    v.set(1)
    for lang, num in LANGS:
        b = Radiobutton(group, text=lang, variable=v, value=num)
        b.pack(anchor=W)
def sb():
    sb = tk.Tk()
    sb.title("反馈/建议")
    sb.configure(bg='black')
    entry = Entry(sb,font=("微软雅黑",10),width=90,bg="dimgray",fg="gold")
    entry.grid(row=0,column=0)#固定位置
    button = Button(sb,text="SEND",font=("微软雅黑",10),bg="gray",fg="White",command=sbb)
    button.grid(row=0,column=1,sticky=E)#固定位置
def sbbb():
    sys.exit() #单纯的退出
def setthings():
    setter = tk.Tk()
    setter.title("关于")
    setter.minsize(372, 230) #固定窗口大小
    setter.maxsize(372, 230) #固定窗口大小
    setter.configure(bg='black')
    lable = Label(setter,text="     Amarantine 1.10    ",fg="SlateBlue1",bg="black",font="微软雅黑")
    lable.grid(row=0,column=0)#固定位置
    scrolW = 50 # 设置文本框的长度
    scrolH = 10 # 设置文本框的高度
    scr = scrolledtext.ScrolledText(setter, width=scrolW, height=scrolH,wrap=tk.WORD,bg="dimgray",fg="gold")#设置颜色
    scr.grid(row=1,column=0)#固定位置
    scr.insert(END, "-@-@-@-@-@更新公告@-@-@-@-@-"+"\n"+"Date:8/18-8/24"+"\n"+"New:"+"\n"+"1.升级界面 ——>对于 关于 界面进行升级 整理菜单"+"\n"+"2.新增100+对话"+"\n"+"3.修复bug"+"\n"+"4.新的logo"+"\n")
    button = Button(setter,text="检查更新",font=("微软雅黑",10),bg="dimgray",fg="SpringGreen",width=46,height=1,command=down)
    button.grid(row=2,column=0)#固定位置
    button = Button(setter,text="报告反馈",font=("微软雅黑",10),bg="dimgray",fg="SpringGreen",width=46,height=1,command=sb)
    button.grid(row=3,column=0)#固定位置
def about():
    settere = tk.Tk()
    settere.title("介绍")
    settere.minsize(50,50)
    settere.configure(bg='black')
    lable = Label(settere,text="Amarantine",fg="gold",bg="black",font="微软雅黑")
    lable.grid(row=0,column=0)#固定位置
    lable = Label(settere,text="性别: 男",fg="gold",bg="black",font="微软雅黑")
    lable.grid(row=1,column=0)#固定位置
    lable = Label(settere,text="年龄:12",fg="gold",bg="black",font="微软雅黑")
    lable.grid(row=2,column=0)#固定位置
    lable = Label(settere,text="职业:学生",fg="gold",bg="black",font="微软雅黑")
    lable.grid(row=3,column=0)#固定位置
    lable = Label(settere,text="性格:阳光 开朗",fg="gold",bg="black",font="微软雅黑")
    lable.grid(row=4,column=0)#固定位置
def sendmes():
    time.sleep(0.6) 
    content = entry.get()#读取屏幕内容
    response = mybot.respond(content)#链接aiml
    torboot = "我:"+content+"\n"
    claire = "Amarantine:"+response+"\n"
    scr.insert(END, torboot)
    scr.insert(END, claire)
    entry.delete(0,'end') 
    AIsay = pyttsx3.init()#初始化pyttsx3
    AIsay.setProperty('rate', 125)#语速:125
    AIsay.say(response)#文本转语音
    AIsay.runAndWait()
#-@-@-@-@-@-@-@-@-@-@
#设置主窗口
root = tk.Tk()
enres = StringVar() #设置变量
root.title("Amarantine 1.10") #设置窗口标题
root.minsize(723, 492) #固定窗口大小
root.maxsize(723, 492) #固定窗口大小
root.configure(bg='black')#设置背景色
root.geometry("250x150+800+450")  #固定串口位置
root.iconbitmap("LOGO.ico")#窗口图标
lable = Label(root,text="Amarantine ● 在线",fg="SpringGreen",bg="black",font="微软雅黑")
lable.grid(row=0,column=0)#固定位置
lable = Label(root,text="Amarantine 1.10 BY CLEVERRAT",fg="gold",bg="black",font="微软雅黑")
lable.grid(row=3,column=0)#固定位置
#-@-@-@-@-@-@-@-@-@-@
#设置输入框
entry = Entry(root,font=("微软雅黑",10),width=90,bg="dimgray",fg="gold")
entry.grid(row=2,column=0)#固定位置
#-@-@-@-@-@-@-@-@-@-@ 
# 对话消息框设置成滚动文本框
scrolW = 100 # 设置文本框的长度
scrolH = 30 # 设置文本框的高度
scr = scrolledtext.ScrolledText(root, width=scrolW, height=scrolH,wrap=tk.WORD,bg="dimgray",fg="gold")#设置颜色
scr.grid(row=1,column=0)#固定位置
#设置发送按钮，点击的时候去执行sendmes函数
button = Button(root,text="SEND",font=("微软雅黑",10),bg="gray",fg="White",command=sendmes)
button.grid(row=2,column=0,sticky=E)#固定位置
#-@-@-@-@-@-@-@-@-@-@
menubar = Menu(root) #设置菜单
setVar = IntVar()
opeVar = IntVar()
sbVar = IntVar()
ncVar = IntVar()
songVar = IntVar()
comVar = IntVar()
CLVar = IntVar()
#-@-@-@-@-@-@-@-@-@-@
filemenu = Menu(menubar, tearoff=True)
filemenu.add_checkbutton(label="关于", command=setthings, variable=setVar)
filemenu.add_separator()#无情分割线
filemenu.add_checkbutton(label="AI介绍", command=about, variable=opeVar)
filemenu.add_checkbutton(label="反馈/建议", command=sb, variable=sbVar)
filemenu.add_separator()#无情分割线
filemenu.add_checkbutton(label="主题歌", command=songs, variable=songVar)
filemenu.add_checkbutton(label="官网", command=com, variable=comVar)
filemenu.add_separator()#无情分割线
filemenu.add_checkbutton(label="退出", command=sbbb, variable=ncVar)
menubar.add_cascade(label="更多", menu=filemenu)
#-@-@-@-@-@-@-@-@-@-@
cleanVar = IntVar()
cleverVar = IntVar()
downloadVar = IntVar()
#-@-@-@-@-@-@-@-@-@-@
settermenu = Menu(menubar, tearoff=True)
settermenu.add_checkbutton(label="摘除AI之脑", command=CL, variable=cleverVar)
settermenu.add_checkbutton(label="AI记忆清除", command=clean, variable=cleanVar)
settermenu.add_separator()#无情分割线
settermenu.add_checkbutton(label="检查更新", command=down, variable=downloadVar)
settermenu.add_separator()#无情分割线
settermenu.add_checkbutton(label="AI语言偏好", command=groups, variable=CLVar)
menubar.add_cascade(label="设置", menu=settermenu)
#-@-@-@-@-@-@-@-@-@-@
sonVar = IntVar()
CVar = IntVar()
testVar = IntVar()
#-@-@-@-@-@-@-@-@-@-@
cymenu = Menu(menubar, tearoff=True)
cymenu.add_checkbutton(label="上传语料库", command=GIT, variable=sonVar)
cymenu.add_checkbutton(label="制作语料库", command=XS, variable=CVar)
cymenu.add_checkbutton(label="测试语料库", command=test, variable=testVar)
menubar.add_cascade(label="工作台", menu=cymenu)
root.config(menu=menubar)#显示菜单



#加载AIML
mybot_path = './core'
#切换到语料库所在工作目录
os.chdir(mybot_path)
mybot = aiml.Kernel()
if os.path.isfile("AIの脑.brn"):#生成brain文件
    mybot.bootstrap(brainFile="AIの脑.brn")#读取brain文件
else:
    mybot.bootstrap(learnFiles="启动文件.xml", commands="LOAD CL")#读取AI启动文件
    mybot.saveBrain("AIの脑.brn")#保存brain文件
root.mainloop()#显示TK窗口

#Amarantine.py 是Amarantine的一部分  作者:CLEVERRAT   