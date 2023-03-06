from enum import Enum
from time import sleep
from selenium.webdriver.support.select import Select
from browser import Browser
from mts import auth
from enum import Enum
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import re


class CSSconst(Enum):
    button_house = "button"
    text_entrance = (
        "html body.modal-open div#checkList_dialog.modal.fade.show "
        "div.modal-dialog.modal-dialog-centered.modal-lg div.modal-content "
        "div#checkListDialog_text.modal-body form#check_list_form div.m-1.text-right b "
    )
    radio1 = (
        "html body.modal-open div#checkList_dialog.modal.fade.show "
        "div.modal-dialog.modal-dialog-centered.modal-lg div.modal-content "
        "div#checkListDialog_text.modal-body form#check_list_form div.table-responsive "
        "table.table.table_main.table-hover tbody tr td "
        "div.custom-control.custom-radio.custom-control-inline "
        "input#sticker_drs_1.custom-control-input.cRequired_class "
    )
    radio2 = (
        "html body.modal-open div#checkList_dialog.modal.fade.show "
        "div.modal-dialog.modal-dialog-centered.modal-lg div.modal-content div#checkListDialog_text.modal-body "
        "form#check_list_form div.table-responsive table.table.table_main.table-hover tbody tr td "
        "div.custom-control.custom-radio.custom-control-inline input#sticker_drs_change_0.custom-control-input "
    )
    save = (
        "html body.modal-open div#checkList_dialog.modal.fade.show div.modal-dialog.modal-dialog-centered.modal-lg "
        "div.modal-content div#checkListDialog_text.modal-body form#check_list_form "
        "div.form-group.col-12.p-0.text-right button.m-1.btn.btn-primary.button_save "
    )
    yes = (
        "html body.modal-open div#confirm_dialog.modal.fade.show div.modal-dialog.modal-dialog-centered "
        "div.modal-content div.modal-footer button#confirmDialog_buttonYes.m-1.btn.btn-primary "
    )
    close = (
        "html body.modal-open div#confirm_dialog.modal.fade.show div.modal-dialog.modal-dialog-centered "
        "div.modal-content div.modal-footer button#confirmDialog_buttonYes.m-1.btn.btn-primary"
    )


class House:
    def __init__(self, address):
        self.address = address
        self.browser = Browser(address).browser

    def open_window_of_addition(browser):
        element = browser.find_elements_by_tag_name(CSSconst.button_house.value)
        # for _ in element:
        #    print(_.get_attribute('innerHTML'))
        if len(element) != 0:
            element[7].click()
        else:
            print(f"Не видит кнопку. Длина равна {len(element)}")

    def house(self):
        browser = Browser(self.address).browser
        browser.get("http://inventory.ural.mts.ru/pc/agent_day.php")
        auth(browser)
        sleep(10)
        House.open_window_of_addition(browser)
        sleep(10)
        count_element = browser.find_element_by_css_selector(
            CSSconst.text_entrance.value
        )
        print(type(count_element))
        count = int(count_element.text)
        for entrance in range(1, count + 1):
            select_element = browser.find_element_by_id("entrance")
            select_object = Select(select_element)
            print(entrance)
            select_object.select_by_value(str(entrance))
            sleep(10)
            radio1 = browser.find_element_by_css_selector(CSSconst.radio1)
            browser.execute_script("arguments[0].click();", radio1)
            radio2 = browser.find_element_by_css_selector(CSSconst.radio2)
            browser.execute_script("arguments[0].click();", radio2)
            radio3 = browser.find_elements_by_id("heavy_media_1")
            browser.execute_script("arguments[0].click();", radio3[0])
            radio4 = browser.find_element_by_id("heavy_media_change_0")
            browser.execute_script("arguments[0].click();", radio4)
            radio5 = browser.find_element_by_id("poster_elevator_0")
            browser.execute_script("arguments[0].click();", radio5)
            radio6 = browser.find_element_by_id("poster_elevator_change_0")
            browser.execute_script("arguments[0].click();", radio6)
            radio7 = browser.find_element_by_id("flyer_agent_1")
            browser.execute_script("arguments[0].click();", radio7)
            radio8 = browser.find_element_by_id("flyer_provider_0")
            browser.execute_script("arguments[0].click();", radio8)
            save_one = browser.find_elements_by_css_selector(CSSconst.save)
            save_one[0].click()
            sleep(4800 // count)
        finish = browser.find_element_by_id("button_checkListComplete")
        finish.click()
        yes = browser.find_elements_by_css_selector(CSSconst.yes)
        yes[0].click()
        sleep(5)
        close = browser.find_elements_by_css_selector(CSSconst.close)
        close[0].click()
