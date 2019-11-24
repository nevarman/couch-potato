#!/usr/bin/python3
import getpass
import keyring
import io
import os

filepath = 'user.txt'


def get_credentials(account):
    try:
        users = open(filepath)
        lines = users.readlines()
        if(len(lines) == 0):
            raise IOError('User file is empty!')
        for line in lines:
            if(account in line):
                user = line.split(':')[1]
    except IOError:
        # If not exists, create the file
        users = open(filepath, 'w+')
        user = input("Please enter your %s user name:" % account)
        users.write(''.join([account, ':', user]))
        users.close()
    pswd = keyring.get_password(account, user)
    if(pswd == None):
        keyring.set_password(account, user, getpass.getpass("Password:"))
    pswd = keyring.get_password(account, user)
    return user, pswd
