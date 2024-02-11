# Это пример файла local_settings
# Здесь будут храниться определения переменных, которые необходимы для работы проекта


# БД
DATABASES: dict = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '...',
        'USER': 'postgres',
        'PASSWORD': '...',
        'HOST': 'localhost',
    },
}
