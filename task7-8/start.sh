#!/bin/bash

# Создание сети
docker network create my_network

# Сборка образов
docker build -t app_img -f Dockerfile.app .
docker build -t database_img -f Dockerfile.db .
docker build -t nginx_img -f Dockerfile.nginx .

# Запуск контейнера базы данных
docker run --name database --network my_network -e POSTGRES_USER=myapp_user -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=myapp_db -d database_img

# Запуск контейнера приложения
docker run --name app --network my_network -p 5100:5100 -d app_img

# Запуск контейнера Nginx
docker run --name nginx --network my_network -p 80:80 -d nginx_img
