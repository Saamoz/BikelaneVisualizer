import geopy
from image_tools import filter_bikelanes, crop_image, write_svg
from maps_web_scraper import screenshot_page
import os

if __name__ == '__main__':
    location_name = "toronto"
    # screenshot_path = screenshot_page(location_name)
    cropped_image = crop_image('temp/ss.png')
    filter_bikelanes(cropped_image, f"output/{location_name}_bikelanes.png")
    os.system(f"potrace temp/pbm_image.pbm --svg -o output/{location_name}_bikelanes.svg")
    # write_svg(contours, f"output/{location_name}_bikelanes.svg")
