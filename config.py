# encoding: utf-8

import os

DEBUG = False

SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'zlktqa'
DB_URL = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,
                                                      DRIVER,
                                                      USERNAME,
                                                      PASSWORD,
                                                      HOST,
                                                      PORT,
                                                      DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
