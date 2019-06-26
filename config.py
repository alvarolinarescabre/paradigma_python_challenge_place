class Config(object):
       ''' Common configuration '''

class DevelopmentConfig(Config):
   ''' Development configuration '''
   DEBUG = True
   SQLALCHEMY_ECHO = True
   SQLALCHEMY_TRACK_MODIFICATIONS = True
   

class ProductionConfig(Config):
   DEBUG = False

app_config = {
   'development' : DevelopmentConfig,
   'production' : ProductionConfig,
   'default' : 'development'
}
