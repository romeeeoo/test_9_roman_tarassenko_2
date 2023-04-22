1. git clone https://github.com/romeeeoo/test_9_roman_tarassenko_2.git
2. запустить приложение PyCharm и открыть папку проекта
3. PyCharm предложит установить виртуальное окружение и установить модули из файла requirements.txt
4. Нажимает Ок
5. Далее необходимо создать БД на локальном компьютере
6. В проекте, в приложении app открыть файл settings.py и добавить подключение к локальной БД: DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'название БД',
        'USER': 'пользователь',
        'PASSWORD': 'пароль',
        'HOST': 'localhost',
        'PORT': ''
    }
}
7. В терминале запустить команду python manage.py migrate, которая создаст в БД необходимые таблицы
8. Запустить проект командой python manage.py runserver
