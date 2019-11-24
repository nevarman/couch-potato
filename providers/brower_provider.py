#!/usr/bin/python3
from selenium import webdriver
from pathlib import Path
import platform


def get_brower(brower):
    user_path = get_user_data_dir(brower)
    if(brower == 'chrome'):
        chrome_options = webdriver.ChromeOptions()
        if(len(user_path) > 0):
            chrome_options.add_argument("user-data-dir=%s" % user_path)
        return webdriver.Chrome(options=chrome_options)
    elif brower == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        if(len(user_path) > 0):
            firefox_options.add_argument("user-data-dir=%s" % user_path)
        return webdriver.Firefox(options=firefox_options)
    raise Exception(
        'Please type in a browser name, such as chrome or firefox.')


def get_user_data_dir(browser):
    pl = platform.system()
    if(pl == 'Windows'):
        if(browser == 'chrome'):
            return str(Path.joinpath(
                Path.home(), 'AppData\\Local\\Google\\Chrome\\User Data'))
        elif(browser == 'firefox'):
            return str(Path.joinpath(
                Path.home(), 'AppData\\Roaming\\Mozilla\\Firefox\\Profiles'))
    elif(pl == 'Darwin'):
        pass
    elif(pl == 'Linux'):
        pass  # pass for now
