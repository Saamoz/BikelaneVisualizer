import os

for i in sorted(os.listdir("./svg")):
	print("<div><img src='svg/" + i + "' alt=''></div>")