#!/usr/bin/python3
import getpass
import keyring
import io
import os

filepath = 'user.txt'


def get_credentials(account):
    try:
        users = open(filepath)
        user = users.readline()
    except IOError:
        # If not exists, create the file
        users = open(filepath, 'w+')
        user = input("User Name:")
        users.write(user)
        users.close()
    pswd = keyring.get_password(account, user)
    if(pswd == None):
        keyring.set_password(account, user, getpass.getpass("Password:"))
    pswd = keyring.get_password(account, user)
    return user, pswd
