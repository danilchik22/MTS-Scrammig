from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from mts import get_location


class Browser:
    def __init__(self, address):
        self.browser = Browser.init_browser(address)

    def init_browser(address):
        binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        profile = FirefoxProfile("C:\\Users\\111\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\w8iy627a.debanjan")
        user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
        profile.set_preference("general.useragent.override", user_agent)
        geoAllowed = webdriver.FirefoxOptions()
        geoAllowed.set_preference('geo.prompt.testing', True)
        geoAllowed.set_preference('geo.prompt.testing.allow', True)
        geoAllowed.set_preference('geo.provider.network.url',
                                  f'data:application/json,{{"location": {{"lat": {get_location(address)["weight"]}, '
                                  f'"lng": {get_location(address)["length"]}}}, "accuracy": 100.0}}')
        browser = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary,
                                    executable_path="C:\\Users\\111\\Desktop\\Scramming\\geckodriver.exe",
                                    options=geoAllowed)
        return browser