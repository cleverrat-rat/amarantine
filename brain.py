import aiml
import os
import time
mybot_path = './core'
#切换到语料库所在工作目录
os.chdir(mybot_path)
mybot = aiml.Kernel()
if os.path.isfile("mybot_brain.brn"):
    mybot.bootstrap(brainFile="mybot_brain.brn")
else:
    mybot.bootstrap(learnFiles="启动文件.xml", commands="LOAD CL")
    mybot.saveBrain("mybot_brain.brn")
while True:
    print(mybot.respond(input("向Claire发送信息>>>")))
    os.system("color 09")
    
