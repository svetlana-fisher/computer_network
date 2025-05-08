#!/bin/bash

# Остановка и удаление контейнера приложения
docker stop app
docker rm app

# Остановка и удаление контейнера базы данных
docker stop database
docker rm database

# Удаление образов
docker rmi app_img
docker rmi database_img

docker stop nginx
docker rm nginx

# Удаление сети
docker network rm my_network

pkill -f nginx