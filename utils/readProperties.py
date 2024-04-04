import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/inputData.ini")


class ReadConfig():

    @staticmethod
    def getBaseURL():
        BaseUrl = config.get('Login Details', 'BaseUrl')

    @staticmethod
    def getUsername():
        Username = config.get('Login Details', 'Username')

    @staticmethod
    def getPassword():
        Password = config.get('Login Details', 'Password')

    @staticmethod
    def getFullNameL():
        FullName = config.get('User Information', 'FullName')

    @staticmethod
    def getSurname():
        Surname = config.get('User Information', 'Surname')

    @staticmethod
    def getZipCode():
        ZipCode = config.get('User Information', 'ZipCode')