import geopy
from image_tools import filter_bikelanes, crop_image, write_svg
from maps_web_scraper import screenshot_page
import os

if __name__ == '__main__':
    location_name = "paris"
    do_screenshot = True
    screenshot_path = screenshot_page(location_name) if do_screenshot else 'temp/ss.png'
    cropped_image = crop_image(screenshot_path)
    filter_bikelanes(cropped_image, f"output/{location_name}_bikelanes.png")
    os.system(f"potrace temp/pbm_image.pbm --svg -o output/{location_name}_bikelanes.svg")
