class ProdConfig:
    ENV = 'production'
    DEBUG = False
    DEBUG_TB_ENABLED = False
    HOST = '0.0.0.0'
    TEMPLATES_AUTO_RELOAD = True
    JSON_SORT_KEYS = False

class DevConfig:
    ENV = 'development'
    DEBUG = True
    DEBUG_TB_ENABLED = True
    HOST = '0.0.0.0'
    TEMPLATES_AUTO_RELOAD = True
    JSON_SORT_KEYS = False