import os
print("HelloWorld")
sleep = "sleep 10"



command = "launch -a screen coordinate"
os.system(command)
os.system(sleep)

command = "input tap"
x = 0
y = 0

for x in range(1400,1500):
	for y in range(1300;1500):
		command = "input tap"
		command = command+" "+str(x)+" "+str(y)
		print(command)
		os.system(command)

print("Finish")
