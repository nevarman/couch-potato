#!/usr/bin/python3
from selenium import webdriver
from providers.streaming_provider import StreamingProviderSettings, StreamingProvider
import getopt
import sys

# read commandline arguments, first
fullCmdArguments = sys.argv
# - further arguments
argumentList = fullCmdArguments[1:]
# print(argumentList)
unixOptions = "hpr:po:b:"
gnuOptions = ["help", "profile=", "potato=", "browser="]

try:
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    # output error, and return with an error code
    print(str(err))
    sys.exit(2)

potato = 'netflix'
user = 0
browser = 'chrome'
for currentArgument, currentValue in arguments:
    if currentArgument in ("-h", "--help"):
        print("displaying help")
    elif currentArgument in ("-pr", "--profile"):
        print(("enabling user: (%d)") % (int(currentValue)))
        user = int(currentValue)
    elif currentArgument in ("-po", "--potato"):
        print(("enabling potato mode: (%s)") % (currentValue))
        potato = currentValue.lower()
    elif currentArgument in ("-b", "--browser"):
        print(("opening browser: (%s)") % (currentValue))
        browser = currentValue.lower()

settings = StreamingProviderSettings(potato, browser)
# potato
streaming_potato = StreamingProvider(settings).get_potato()
# login
streaming_potato.login(user=user)
# skip
streaming_potato.auto_skip()
