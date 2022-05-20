import geopy
from mask_bikelanes import filter_bikelanes
from maps_web_scraper import screenshot_page

if __name__ == '__main__':
    coordinates = geopy.Point(43.6635, -79.3899)
    screenshot_path = screenshot_page(coordinates)
    filter_bikelanes(screenshot_path, f"Toronto Bikelanes.png")
