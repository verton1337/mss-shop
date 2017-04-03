import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop',
        'USER': 'lapollry_turchaninov',
        'PASSWORD': 'Verton1337',
        'HOST': '127.0.0.1',
    },
    
}