from image_tools import filter_bikelanes, crop_image
from maps_web_scraper import screenshot_page
import os
import csv


def get_city_bikelanes(city_name):
    screenshot_path = screenshot_page(city_name)
    cropped_image = crop_image(screenshot_path)
    filter_bikelanes(cropped_image, f'output/png/{city_name} Bikelanes.png')
    os.system(f'potrace temp/pbm_image.pbm --svg -o "output/svg/{city_name} Bikelanes.svg"')


if __name__ == '__main__':
    # get_city_bikelanes("Monterrey")
    city_list_file = "cities.csv"
    with open(city_list_file, 'r', encoding='utf-8') as csvfile:
        datareader = csv.reader(csvfile)
        datareader.__next__()
        start_name = ""
        do = False
        for row in datareader:
            city_name = ", ".join(row)
            if not start_name or start_name in city_name:
                do = True
            print(f"Exporting bike lanes for {city_name}")
            if do:
                get_city_bikelanes(city_name)

