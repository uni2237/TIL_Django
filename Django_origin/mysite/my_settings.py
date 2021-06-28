# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jp_item_info',  # db 이름
        'USER': 'ojjo',     # 로그인-유저 명
        'PASSWORD': 'ojjo2021',  # 로그인-비밀번호
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}