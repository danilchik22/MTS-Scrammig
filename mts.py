from enum import Enum
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import re
import os


def get_location(address):
    url = "https://www.google.com/maps/search/Барнаул " + address
    opts = webdriver.FirefoxOptions()
    opts.headless = True
    browser = webdriver.Firefox(options=opts)  # создаем объект Firefox браузера
    browser.get(url)
    meta_gps = browser.find_elements_by_css_selector("html head meta")
    content_meta = meta_gps[10].get_attribute("content")
    weight = re.findall(r"center=([0-9\.]+)%2C", content_meta)[0]
    length = re.findall(r"2C([0-9\.]+)&zoom", content_meta)[0]
    browser.quit()
    return {"weight": weight, "length": length}


def auth(browser):
    element = browser.find_element_by_id("login")
    element.send_keys(os.getenv("LOGIN"))
    element = browser.find_element_by_id("password")
    element.send_keys(os.getenv("PASSWORD"))
    element = browser.find_elements_by_css_selector(
        "html body form div.col-12.col-md-2.offset-md-4.text-center button.m-1.btn.btn-primary"
    )
    element[0].click()
