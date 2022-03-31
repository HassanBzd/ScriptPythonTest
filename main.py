import subprocess
print("HelloWorld")



command = "launch -a snapchat"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)