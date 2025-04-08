@echo off

REM Остановка и удаление контейнера приложения
docker stop app
docker rm app

REM Остановка и удаление контейнера базы данных
docker stop database
docker rm database

REM Удаление образов
docker rmi app_img
docker rmi database_img

REM Удаление сети
docker network rm my_network
