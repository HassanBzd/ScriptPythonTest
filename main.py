import os

sleep = "sleep 5"



command = "launch -a snapchat &"
os.system(command)
os.system(sleep)
command = "input tap"
x = 660
y = 280

command = command+" "+str(x)+" "+str(y)
os.system(command)

name = vevoisback
os.system(sleep)
command = "input text "+name
os.system(command)