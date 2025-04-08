@echo off

REM Создание сети
docker network create my_network

REM Сборка образов
docker build -t app_img -f Dockerfile.app .
docker build -t database_img -f Dockerfile.db .

REM Запуск контейнера базы данных
docker run --name database --network my_network -e POSTGRES_USER=myapp_user -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=myapp_db -d database_img

REM Запуск контейнера приложения
docker run --name app --network my_network -p 80:5100 -d app_img
