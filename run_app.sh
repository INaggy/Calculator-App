#!/bin/bash
echo "Чтение конфигурации из app_config.yaml..."
START_COMMAND=$(python3 -c "
import yaml
with open('app_config.yaml') as file:
    print(yaml.safe_load(file)['commands']['start'])
")

echo "Запуск приложения..."
eval "$START_COMMAND"
