#!/usr/bin/python3
import time
import threading
from streaming_potato import StreamingPotato
from selenium.common.exceptions import NoSuchElementException

SELECTOR_USER = '#id_userLoginId'
SELECTOR_PASS = '#id_password'
SELECTOR_LOGIN = '#appMountPoint > div > div.login-body > div > div > div.hybrid-login-form-main > form > button'
SELECTOR_SKIP_INTRO = '//*[@id="appMountPoint"]/div/div/div[1]/div/div/div[2]/div/div[3]/div[1]/a/span'
SELECTOR_PROFILE = 'profile'
SELECTOR_DEFAULT_PROFILE = '''//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/div/div'''


class Netflix_Potato(StreamingPotato):

    def __init__(self, settings):
        super().__init__(settings)
        self._open()

    def _open(self):
        self.browser.get('https://www.netflix.com/browse')

    def login(self, user=-1):
        if("Login" not in self.browser.current_url):
            return
            # login
        elem_user = self.browser.find_element_by_css_selector(SELECTOR_USER)
        elem_password = self.browser.find_element_by_css_selector(
            SELECTOR_PASS)
        elem_user.send_keys(self.credentials[0])
        elem_password.send_keys(self.credentials[1])
        elem_login = self.browser.find_element_by_css_selector(SELECTOR_LOGIN)
        elem_login.click()
        # user select
        if(user >= 0):
            profiles = self.browser.find_elements_by_class_name(
                SELECTOR_PROFILE)
            if(profiles != None and user < len(profiles)):
                profiles[user].click()
            else:
                self.browser.find_element_by_xpath(
                    SELECTOR_DEFAULT_PROFILE).click()

    def confinue_watching(self, index=0):
        # TODO
        elem = self.browser.find_element_by_xpath(
            '//*[@id="row-1"]/div/div/div/div/div')

        elems = elem.find_elements_by_xpath('./*')
        print(len(elems))

    def play(self):
        pass

    def pause(self):
        pass

    def auto_skip(self):
        if("watch" in self.browser.current_url):
            try:
                self.browser.find_element_by_xpath(SELECTOR_SKIP_INTRO).click()
            except NoSuchElementException:
                pass
        threading.Timer(3, self.auto_skip).start()
