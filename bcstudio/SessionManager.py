__author__ = 'Rayer'

import Singleton


class SessionUser:

    def __init__(self):
        pass

    def get_name(self):
        pass

    def get_session(self):
        pass

    def get_capabilities(self):
        pass



class SessionManager(metaclass=Singleton):

    def __init__(self):
        pass

    def validate_session(self, session):
        pass

    def find_session_user_from_credential(self, credential):
        pass

    def expire_session(self, session):
        pass

    def __is_expired(self, session):
        pass

