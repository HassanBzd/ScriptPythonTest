import os
print("HelloWorld")
sleep = "sleep 10"



command = "launch -a screen coordinate"
os.system(command)
os.system(sleep)

command = "input tap"
x = 0
y = 0

for x in range(100):
	for y in range(100):
		command = command+" "+str(x)+" "+str(y)
		os.system(command)

print("Finish")
