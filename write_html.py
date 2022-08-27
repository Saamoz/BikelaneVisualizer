import os


def make_webpage(svg_folder_path):
    f = open("design/bikelanes.html", "w")
    f.write('<!DOCTYPE html>\n<html>\n<head>\n<link rel="stylesheet" href="styles.css">\n</head>\n<body>\n\n')
    f.write('<h1>MAPPING BIKE INFRASTRUCTURE</h1>\n<p><i>IN 100 CITIES AROUND THE WORLD</i></p>\n\n')
    f.write('<div class="grid">\n')

    for svg_filename in sorted(os.listdir(svg_folder_path)):
        city_name = svg_filename.split("Bikelanes")[0]
        line = f'<div> \n' \
               f'\t<div class="text-container"> \n' \
               f'\t\t<h3>{city_name}</h3> \n' \
               f'\t</div> \n' \
               f'\t<div class="image-container"> \n' \
               f'\t\t<img src="../{svg_folder_path}/{svg_filename}" alt=''> \n' \
               f'\t</div> \n' \
               f'</div> \n\n'
        f.write(line)

    f.write('</div>\n</body>\n')
    f.close()


if __name__ == "__main__":
    make_webpage('output/svg')