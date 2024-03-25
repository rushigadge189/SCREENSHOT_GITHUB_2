# import configparser
#
# config=configparser.RawConfigParser() ;
#
# filepath="D:\\PYTHON CT15\\REVISION\\configuration\\config.ini" ;
#
# config.read(filepath) ;
#
# class ReadConfig():
#     @staticmethod
#     def getUserName():
#         username=config.get('common data' ,'username') ;
#         return username;
#     @staticmethod
#     def getPassWord():
#         password=config.get('common data', 'password') ;
#         return password ;
#import configparser

# import configparser
#
# config=configparser.RawConfigParser() ;
#
# filepath="D:\\PYTHON CT15\\REVISION\\configuration\\config.ini" ;
#
# config.read(filepath) ;
#
# class ReadConfig():
#     @staticmethod
#     def getUserName():
#         USERNAME=config.get('common data', 'username') ;
#         return USERNAME ;
#
#     @staticmethod
#     def getPassWord() :
#         PASSWORD = config.get('common data', 'password');
#         return PASSWORD ;

import configparser

config=configparser.RawConfigParser() ;

filepath="D:\\PYTHON CT15\\REVISION\\configuration\\config.ini"

config.read(filepath) ;

class ReadConfig():
    @staticmethod
    def getUserName():
        username=config.get('common data' , 'username') ;
        return username ;
    @staticmethod
    def getPassWord():
        password=config.get('common data' , 'password') ;
        return password ;