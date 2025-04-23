
#Запуск с помощью Docker
#Требования
 Установленный Docker

 Установленный Docker Compose

#Шаги для запуска
#Клонируйте репозиторий:
 git clone https://github.com/1mShafuu/detect_vehicles/



#Соберите и запустите контейнер:
 docker-compose up -d --build


#Сервис будет доступен по адресу:
 http://localhost:8000


#Запуск без Docker
#Требования
 Python 3.10+

 Установленный pip


#Повторите шаги по клонированию репозитория
#Создайте и активируйте виртуальное окружение:
 python -m venv venv
 source venv/bin/activate  # Linux/MacOS
 venv\Scripts\activate     # Windows


#Установите зависимости:
 pip install -r requirements.txt


#Запустите сервис:
 uvicorn app.main:app --reload


#Сервис будет доступен по адресу:

http://localhost:8000



#Использование API
#Получение информации об адресе

 POST /detect
 Body: {"file" : "@test.jpg"}
 Получение списка изображений транспортных средств на картинке( велосипеды и автомобили)
