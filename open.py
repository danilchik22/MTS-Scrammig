from time import sleep

from selenium import webdriver #Ипортируем библиотеку


def delivery(number):
    browser = webdriver.Firefox() #создаем объект Firefox браузера
    browser.get("https://www.delivery-club.ru/moscow?authPopupOpened=1")
    elements = browser.find_elements_by_css_selector("input")
    for el in elements:
        if el.get_attribute("type") == "tel":
            el.send_keys(number)
    sleep(10)
    browser.quit()
def drom(number):
    browser = webdriver.Firefox() #создаем объект Firefox браузера
    browser.get("https://my.drom.ru/sign/recover?return=https%3A%2F%2Fwww.drom.ru%2F%3Ftcb%3D1652164476")
    element = browser.find_element_by_id("sign")
    element.send_keys("+7" + number + "\n")
    elements = browser.find_elements_by_css_selector("button")
    elements[0].click()
    sleep(10)
    browser.quit()
def apteka_ru(number):
    browser = webdriver.Firefox()  # создаем объект Firefox браузера
    browser.get("https://apteka.ru/")
    sleep(10)
    element = browser.find_element_by_css_selector("div.overlay-wrapper div.overlay.TownSelector div.TownSelector__select div div.simplebar-wrapper div.simplebar-mask div.simplebar-offset div.simplebar-content-wrapper div.simplebar-content div ol.TownSelector__options li")
    element.click()
    elements = browser.find_elements_by_css_selector("div.HeaderUserButton div.ButtonIcon a")
    elements.click()
    element = browser.find_element_by_id("authorizer-input-username")
    element.send_keys("+7" + number)
    elements = browser.find_element_by_css_selector("div.Authorizer-background div.Authorizer div.Authorizer__login div.AuthorizerForm form#authorizer div.AuthorizerForm__password p span button")
    elements[0].click()
# browser.get('https://id.vk.com/auth?app_id=7913379&v=1.46.0&redirect_uri=https%3A%2F%2Fvk.com%2Flogin%3Fu%3D2%26to%3D%2Fal_im.php%3Fsel%3D710131621&uuid=NNFQDqT2ghhnm6QKqyFrR&action=eyJuYW1lIjoibm9fcGFzc3dvcmRfZmxvdyIsInBhcmFtcyI6eyJ0eXBlIjoic2lnbl9pbiJ9fQ%3D%3D') #посредством метода get, переходим по указаному URL
# elements = browser.find_elements_by_css_selector('div.vkc__TextField__wrapper input')
# elements[0].send_keys("+79612404234")
# elements = browser.find_elements_by_css_selector('button')
# elements[1].click()
# elements = browser.find_elements_by_css_selector('div.vkc__TextField__wrapper input')
# elements[1].send_keys("CfifDkfl+2")
# elements = browser.find_elements_by_css_selector('div.vkc__EnterPasswordNoUserInfo__buttonWrap button')
# elements[0].click()
# sleep(15)
# elements = browser.find_elements_by_css_selector("a.left_row")
# elements[2].click()
# sleep(15)
# elements = browser.find_elements_by_css_selector("button.nim-dialog--markre _im_dialog_markre")
# elements[1].click()
# browser.get('https://vk.com/im?media=&sel=50397662&v=')
# element = browser.find_element_by_id("im_editable50397662")
# element.send_keys("Привет, Анютка\n")