#!/usr/bin/python3
from selenium import webdriver
from pathlib import Path
import platform


def get_brower(brower):
    user_path = get_user_data_dir(brower)
    if(brower == 'chrome'):
        chrome_options = webdriver.ChromeOptions()
        if(user_path != None and len(user_path) > 0):
            chrome_options.add_argument("user-data-dir=%s" % user_path)
        return webdriver.Chrome(options=chrome_options)
    elif brower == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference(  # added for mac
            'media.gmp-manager.updateEnabled', 'true')
        if(user_path != None and len(user_path) > 0):
            firefox_options.add_argument("user-data-dir=%s" % user_path)
        return webdriver.Firefox(options=firefox_options)
    raise Exception(
        'Please type in a valid browser name, chrome or firefox.')


def get_user_data_dir(browser):
    return None
    # TODO for now no user data
    pl = platform.system()
    if(pl == 'Windows'):
        if(browser == 'chrome'):
            return str(Path.joinpath(
                Path.home(), 'AppData\\Local\\Google\\Chrome\\User Data'))
        elif(browser == 'firefox'):
            return str(Path.joinpath(
                Path.home(), 'AppData\\Roaming\\Mozilla\\Firefox\\Profiles'))
    elif(pl == 'Darwin'):
        pass  # TODO mac
    elif(pl == 'Linux'):
        pass  # TODO linux
