from splinter import Browser
import requests
import json
import sys
import os


__version__ = "0.1.1"


def remove_bars(site_name):
    site_name_size = len(site_name)-1

    if site_name[site_name_size] == "/":
        site_name = site_name[0:site_name_size]
        return remove_bars(site_name)
    else:
        return site_name


def check_dir(name_dir="output"):
    if not os.path.exists(name_dir):
        os.makedirs(name_dir)
        os.chdir(name_dir)


def main():

    try:
        site_name = str(sys.argv[1])
    except Exception as ex:
        print('Insert URL to access site.json file')
        print(ex)
        sys.exit(-1)

    site_name_clean = remove_bars(site_name)

    req = requests.get(site_name_clean + "/site.json")
    if req.status_code != 200:
        print("Only OK! This response is " + req.status_code)
        sys.exit(-1)

    check_dir("typoshot-output")

    j = json.loads(req.text)
    for i in j["pages"]:
        browser = Browser("firefox")
        browser.visit(i["url"])
        if browser.status_code.is_success():
            str_replaced = i["title"].replace(" ", "-")
            browser.driver.save_screenshot(str_replaced + ".png")
        browser.quit()
