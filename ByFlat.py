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
    """
    Здесь объявляются константы для поиска элементов по их CSS-селектору.
    """
    button_flat = "html body div.col-12.col-md-6.col-xl-4.m-1.table-responsive table.table_main.table.table-hover tbody tr td button"
    text_entrance = "html body.modal-open div#checkList_dialog.modal.fade.show div.modal-dialog.modal-dialog-centered.modal-lg div.modal-content div#checkListDialog_text.modal-body form#check_list_form div.m-1.text-right b"


class ByFlat:
    def __init__(self, address):
        self.address = address
        self.browser = Browser(address).browser

    def open_window_of_addition(browser):
        """
        Функция перехода в окне, в котором будет происходить заполнение
        квартир.
        """
        element = browser.find_elements_by_css_selector(CSSconst.button_flat.value)
        if len(element) != 0:
            element[0].click()
        else:
            print(f"Не видит кнопку. Длина равна {len(element)}")

    def Max_entrance(browser):
        """
        Функция определения, сколько всего квартир в выбранном доме"""
        entrance_text = browser.find_element_by_css_selector(
            CSSconst.text_entrance.value
        ).text
        if int(entrance_text) > 50:
            max = 50
        else:
            max = int(entrance_text)
        return max

    def flat(self):
        """ Главная функция заполнения поквартирного обхода"""
        browser = Browser(self.address).browser
        browser.get("http://inventory.ural.mts.ru/pc/agent_day.php")
        auth(browser)
        ByFlat.open_window_of_addition(browser)
        sleep(15)
        max_entrance = ByFlat.Max_entrance(browser)
        v = 2
        for i in range(9, max_entrance):
            if i == 12 or i == 28:
                continue
            if i == 23 or i == 42:
                v = 6
            flat_element = browser.find_element_by_id("flat")
            flat_element.send_keys(i)
            select_element = browser.find_element_by_id("status")
            select_object = Select(select_element)
            select_object.select_by_value(str(v))
            save = browser.find_elements_by_css_selector(
                "html body.modal-open div#checkList_dialog.modal.fade.show div.modal-dialog.modal-dialog-centered.modal-lg div.modal-content div#checkListDialog_text.modal-body form#check_list_form div.form-group.row.m-1 div.col-12.p-0.text-right button.m-1.btn.btn-primary.button_save"
            )
            browser.execute_script("arguments[0].click();", save[0])
            v = 2
            sleep(90)
        finish = browser.find_elements_by_css_selector(
            "html body.modal-open div#checkList_dialog.modal.fade.show div.modal-dialog.modal-dialog-centered.modal-lg div.modal-content div.modal-footer button#button_checkListComplete.m-1.btn.btn-success.button_save"
        )
        finish[0].click()
        sleep(10)
        yes = browser.find_elements_by_css_selector(
            "html body.modal-open div#confirm_dialog.modal.fade.show div.modal-dialog.modal-dialog-centered div.modal-content div.modal-footer button#confirmDialog_buttonYes.m-1.btn.btn-primary"
        )
        yes[0].click()
        close = browser.find_elements_by_css_selector(
            "html body.modal-open div#checkList_dialog.modal.fade.show div.modal-dialog.modal-dialog-centered.modal-lg div.modal-content div.modal-footer button.m-1.btn.btn-secondary"
        )
        browser.execute_script("arguments[0].click();", close)
        browser.quit()
