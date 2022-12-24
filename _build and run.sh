#!/bin/bash

version=$(sed -n -r "s/__version__ = '(.*)'\r/\1/p" __version__.py)

echo "current version = $version"

# собираем новый образ
docker build \
    --tag "oemakarov/torgigovru_bot:$version" \
    .

# останавливаем запущенный контейнер
docker stop \
    torgigovru 

# удаляем запущенный контейнер
docker rm \
    --force \
    torgigovru 

# контейнер из нового образа
docker run \
    --detach \
    --name=torgigovru \
    --restart unless-stopped \
    --volume /home/oleg/docker/torgigovru_bot/data:/data \
    --volume /home/oleg/docker/torgigovru_bot/log:/log \
    oemakarov/torgigovru_bot:$version

echo "current version = $version"