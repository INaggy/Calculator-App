#!/bin/bash
echo "Запуск модульных тестов..."
# Пример для Python
source venv/bin/activate
pytest unittests.py
if [ $? -eq 0 ]; then
    echo "Все тесты успешно пройдены!"
else
    echo "Некоторые тесты завершились с ошибками!"
    exit 1
fi
