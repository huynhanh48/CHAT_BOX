# config.py
class Config(object):
    """Cấu hình chung cho tất cả các môi trường"""
    pass

class Development(Config):
    """Cấu hình cho môi trường phát triển"""
    DEBUG = True  # Bật chế độ Debug

class Production(Config):
    """Cấu hình cho môi trường sản xuất"""
    DEBUG = False  # Tắt chế độ Debug

app_config = {
    'development': Development,
    'production': Production,
}
