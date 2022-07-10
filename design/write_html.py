import os
f = open('header.txt')
body = f.read().split('\n')
# plz don't use i if its a name
for name in sorted(os.listdir("./svg")):
	body.append("<th>" + name.split('.')[0] + "<img src='svg/" + name + "' alt=''></th>")

body.append('</tr>')
body.append('</table>')
body.append('</body>')

g = open('test.html', 'w')
g.write("".join(body))