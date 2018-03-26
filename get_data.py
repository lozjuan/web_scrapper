import requests
from lxml import html
from app import app


def get_app_info(url):
    """Basic web scraping function from amazon app catalogue. Retrieve basic information :
    name, version and new release information provided by developer"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
    }
    req = requests.get(url, headers=headers)
    all_data = html.fromstring(req.content)
    name = all_data.xpath('normalize-space(//*[@id="btAsinTitle"]/text())')
    version = all_data.xpath('normalize-space(//*[@id="mas-technical-details"]/div/div[2]/text())')
    release_date = all_data.xpath('normalize-space(//*[@id="masrw-center"]/div[5]//li[2])')
    update_date = all_data.xpath('normalize-space(//*[@id="masrw-center"]/div[5]//li[3])')
    updates = all_data.xpath('//*[@id="masrw-center"]/div[4]/div/ul//li/text()')
    info = [name, version, release_date, update_date, updates]
    return info

if __name__ == '__main__':
    app.run()
