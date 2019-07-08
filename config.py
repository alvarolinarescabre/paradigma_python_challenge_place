class Config(object):
   ''' Common configuration '''
   DEBUG = False
   SQLALCHEMY_ECHO = False
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/database?charset=utf8'

class DevelopmentConfig(Config):
   ''' Development configuration '''
   DEBUG = True
   SQLALCHEMY_ECHO = True
   SQLALCHEMY_TRACK_MODIFICATIONS = True
   
class TestingConfig(Config):
   ''' Testing configuration '''
   SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/database?charset=utf8'
   
class ProductionConfig(Config):
   ''' Production configuration '''
   DEBUG = False

app_config = {
   'development' : DevelopmentConfig,
   'production' : ProductionConfig,
   'testing' : TestingConfig,
   'default' : 'development'
}
