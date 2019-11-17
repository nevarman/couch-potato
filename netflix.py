#!/usr/bin/python3
import time
from streaming_potato import StreamingPotato
'''
'''


class Netflix_Potato(StreamingPotato):

    def __init__(self, credentials, browser):
        super().__init__(credentials, browser)
        self._open()

    def _open(self):
        self.browser.get('https://www.netflix.com/browse')

    def login(self, user=-1):
        if("Login" not in self.browser.current_url):
            return
            # login
        elem_user = self.browser.find_element_by_css_selector(
            '#id_userLoginId')
        elem_password = self.browser.find_element_by_css_selector(
            '#id_password')
        elem_user.send_keys(self.credentials[0])
        elem_password.send_keys(self.credentials[1])
        elem_login = self.browser.find_element_by_css_selector(
            '#appMountPoint > div > div.login-body > div > div > div.hybrid-login-form-main > form > button')
        elem_login.click()
        # user select
        if(user >= 0):
            profiles = self.browser.find_elements_by_class_name('profile')
            if(profiles != None and user < len(profiles)):
                profiles[user].click()
            else:
                self.browser.find_element_by_xpath(
                    '''//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/div/div''').click()

    def confinue_watching(self, index=0):
        elem = self.browser.find_element_by_xpath(
            '//*[@id="row-1"]/div/div/div/div/div')

        elems = elem.find_elements_by_xpath('./*')
        print(len(elems))

    def play(self):
        pass

    def pause(self):
        pass

    def auto_skip(self):
        print('Watching Netflix, will try auto skip when playback allows!')
        while(True):
            if("watch" in self.browser.current_url):
                try:
                    self.browser.find_element_by_xpath(
                        '//*[@id="appMountPoint"]/div/div/div[1]/div/div/div[2]/div/div[3]/div[1]/a/span').click()
                except selenium.common.exceptions.NoSuchElementException:
                    pass
            time.sleep(3)  # sleep for a while
