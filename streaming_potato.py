#!/usr/bin/python3
from abc import ABC, abstractmethod

'''
Base class for streaming apps
'''


class StreamingPotato:

    def __init__(self, credentials, browser):
        self.credentials = credentials
        self.browser = browser

    @abstractmethod
    def _open(self):
        pass

    @abstractmethod
    def login(self, user=-1):
        pass

    @abstractmethod
    def confinue_watching(self, index=0):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def auto_skip(self):
        pass
