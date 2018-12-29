# -*- coding: utf-8 -*-
from datetime import timedelta


class Config(object):
    DEBUG = False
    SECRET_KEY = '\x00\xf1\x00Bv\x990\\1\x04\xe1\xe3g'


class ProductionConfig(Config):
    DEBUG = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=120)


class DevelopmentConfig(Config):
    DEBUG = True
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=1000)
    TESA = 'privet'


class TestingConfig(Config):
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=120)
    DEBUG = True