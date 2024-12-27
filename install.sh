#!/bin/bash
echo "Установка приложения..."

DEB_PACKAGE="deb_build.deb"

if [ ! -f "$DEB_PACKAGE" ]; then
    echo "Файл $DEB_PACKAGE не найден. Выполните create_installer.sh."
    exit 1
fi

sudo dpkg -i "$DEB_PACKAGE" || { echo "Ошибка при установке .deb пакета"; exit 1; }

echo "Приложение установлено!"
