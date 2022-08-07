import os

# make header

f = open("bikelanes.html", "w")
f.write('<!DOCTYPE html>\n<html>\n<head>\n<link rel="stylesheet" href="styles.css">\n</head>\n<body>\n\n')
f.write('<h1>MAPPING BIKE INFRASTRUCTURE</h1>\n<p><i>IN 100 CITIES AROUND THE WORLD</i></p>\n\n')
f.write('<div class="grid">\n')

for svg_filename in sorted(os.listdir("./svg")):
    city_name = svg_filename.split("Bikelanes")[0]
    line = f'<div>' \
           f'<div class="text-container">' \
           f'<h3>{city_name}</h3>' \
           f'</div>' \
           f'<div class="image-container">' \
           f'<img src="svg/{svg_filename}" alt=''>' \
           '</div>' \
           '</div>'
    f.write(line)

f.write('</div>\n</body>\n')
f.close()
