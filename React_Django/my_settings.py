DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',  #[ 1 ]  
        'NAME': 'jp_item_info',                #[ 2 ] 
        'USER': 'ojjo',                        #[ 3 ] 
        'PASSWORD': 'ojjo2021',                #[ 4 ]
        'HOST': 'localhost',                   #[ 5 ]
        'PORT': '3306',                        #[ 6 ]
    }
}

#[ 1 ] : 사용할 엔진 설정. 그대로 두면 됨
#[ 2 ] : 연동할 MySQL의 데이터베이스 이름
#[ 3 ] : DB 접속 계정명
#[ 4 ] : 해당 DB 접속 계정 비밀번호
#[ 5 ] : 실제 DB 주소, 따로 설정 안했으면 그대로 두면 됨
#[ 6 ] : 포트번호, 따로 설정 안했으면 그대로 두면 됨