#!/usr/bin/python3
from selenium import webdriver
from pathlib import Path


def get_brower(brower):
    if(brower == 'chrome'):
        chrome_user_path = str(Path.joinpath(
            Path.home(), 'AppData\\Local\\Google\\Chrome\\User Data'))
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir=%s" % chrome_user_path)
        return webdriver.Chrome('D:/chromedriver.exe',  # todo change this
                                options=chrome_options)
    elif brower == 'firefox':
        firefox_user_path = str(Path.joinpath(
            Path.home(), 'AppData\\Roaming\\Mozilla\\Firefox\\Profiles'))
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("user-data-dir=%s" % firefox_user_path)
        # todo change this
        return webdriver.Firefox(executable_path='D:/geckodriver.exe', options=firefox_options)
    raise Exception(
        'Please type in a browser name, such as chrome, firefox, opera...')
