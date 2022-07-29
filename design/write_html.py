import os
f = open('header.txt')
body = f.read().split('\n')

i = 0
body.append('<table>')
body.append('<tr>')
for name in sorted(os.listdir("./svg")):
	body.append("<th><p>" + (name.split('.')[0])[:-9] + "</p><img src='svg/" + name + "' alt=''></th>")
	if i > 0 and i % 7 == 0:
		body.append('</tr><tr>')

	i = i + 1

body.append('</tr>')
body.append('</table>')
body.append('</body>')

g = open('test.html', 'w')
g.write("".join(body))