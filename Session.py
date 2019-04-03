# -*- coding=UTF-8 -*-

class Session:
    """ represent a session 
    properties:
        limit: minutes of session time limit
        talk_list: list of talk object
        used: number of minutes that has been used
        balance: the remained number of minutes in session object
    """

    def __init__(self, time_limit):
        self.limit = time_limit
        self.talk_list = [] # list storing talk objects
        self.used = 0 # minutes used
        self.balance = self.limit - self.used

    def add(self, talk):
        """Put talk in session's talk list
        """
        self.used += talk.duration
        self.balance = self.limit - self.used
        self.talk_list.append(talk)
