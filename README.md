*API представляет собой сервис по распознаванию транспортных средств(велосипеды,
автомобили) на фото*
# Запуск с помощью Docker
## Требования
 Установленный Docker

 Установленный Docker Compose

## Шаги для запуска
### Клонируйте репозиторий:
 git clone https://github.com/1mShafuu/detect_vehicles/



### Соберите и запустите контейнер (используя терминал в папке с проектом):
 docker-compose build\
 docker-compose up


# Сервис будет доступен по адресу:
 http://localhost:8000


# Запуск без Docker
## Требования
 Python 3.10+

 Установленный pip


## Повторите шаги по клонированию репозитория
### Создайте и активируйте виртуальное окружение:
 python -m venv venv
 source venv/bin/activate  # Linux/MacOS
 venv\Scripts\activate     # Windows


### Установите зависимости:
 pip install -r requirements.txt


### Запустите сервис:
 uvicorn app.main:app --reload


## Сервис будет доступен по адресу:

http://localhost:8000



# Использование API
## Получение информации об адресе

 POST /detect\
 Body: {"file" : "@test.jpg"}\
 Получение списка изображений транспортных средств на картинке( велосипеды и автомобили)\
  

 ## Присутствует скрипт проверки запроса send_request.bat
 Можно запустить предварительно указав полный путь к файлу с изображением для поиска\
 Например: "file=@C:\Users\Username\Pictures\test.jpg"
 
 ## Также можно проверить работу сервиса через Swagger http://localhost:8000/docs
