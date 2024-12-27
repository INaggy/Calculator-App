#!/bin/bash
echo "Начало сборки проекта..."

if [ ! -d "venv" ]; then
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "Ошибка при создании виртуального окружения. Убедитесь, что установлен python3-venv."
        exit 1
    fi
    echo "Создано виртуальное окружение."
fi

source venv/bin/activate
pip install -r requirements.txt || { echo "Ошибка при установке зависимостей."; exit 1; }
echo "Сборка проекта завершена!"
