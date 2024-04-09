import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/inputData.ini")


class ReadConfig():

    @staticmethod
    def getBaseURL():
        BaseUrl = config.get('Login Details', 'BaseUrl')
        return BaseUrl

    @staticmethod
    def getUsername():
        Username = config.get('Login Details', 'Username')
        return Username

    @staticmethod
    def getPassword():
        Password = config.get('Login Details', 'Password')
        return Password

    @staticmethod
    def getFullNameL():
        FullName = config.get('User Information', 'FullName')
        return FullName

    @staticmethod
    def getSurname():
        Surname = config.get('User Information', 'Surname')
        return Surname

    @staticmethod
    def getZipCode():
        ZipCode = config.get('User Information', 'ZipCode')
        return ZipCode
