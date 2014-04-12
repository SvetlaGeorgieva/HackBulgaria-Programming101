class Client():
    def __init__(self, id, username, balance, access_log, failed_login_count):
        self.__username = username
        self.__balance = balance
        self.__id = id
        self.__access_log = access_log
        self.__failed_login_count = failed_login_count

    def get_username(self):
        return self.__username

    def get_balance(self):
        return self.__balance

    def get_id(self):
        return self.__id

    def get_access_log(self):
        return self.__access_log

    def get_failed_login_count(self):
        return self.__failed_login_count
