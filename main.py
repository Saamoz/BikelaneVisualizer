import geopy
from mask_bikelanes import filter_bikelanes
from maps_web_scraper import screenshot_page, crop_image

if __name__ == '__main__':
    # coordinates = geopy.Point(43.6635, -79.3899)
    screenshot_path = screenshot_page("Paris")
    crop_image()
    filter_bikelanes("temp/cropped_ss.png", f"toronto_bikelanes.png")
