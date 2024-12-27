#!/bin/bash

LOG_FILE="script.log"
PROJECT_DIR="/home/$USER/projects/your_project"
BUILD_DIR="$PROJECT_DIR/deb_build"
INSTALL_DIR="$BUILD_DIR/usr/bin"
CONTROL_FILE="$BUILD_DIR/DEBIAN/control"

# Логирование
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

# Обновление репозитория
update_repository() {
    log "Начало обновления репозитория..."
    if [ -d "$PROJECT_DIR" ]; then
        cd "$PROJECT_DIR" || exit
        git reset --hard HEAD
        git pull origin main || log "Ошибка при обновлении репозитория" && exit 1
    else
        git clone https://github.com/INaggy/script-linux.git "$PROJECT_DIR" || {
            log "Ошибка при клонировании репозитория"
            exit 1
        }
    fi
    log "Обновление репозитория завершено!"
}

# Сборка проекта
build_project() {
    log "Сборка проекта..."
    chmod +x "$PROJECT_DIR/build.sh"
    "$PROJECT_DIR/build.sh" || {
        log "Ошибка при сборке проекта"
        exit 1
    }
    log "Сборка проекта завершена!"
}

# Выполнение тестов
run_tests() {
    log "Выполнение тестов..."
    chmod +x "$PROJECT_DIR/run_unittests.sh"
    "$PROJECT_DIR/run_unittests.sh" || {
        log "Ошибка при выполнении тестов"
        exit 1
    }
    log "Тесты успешно пройдены!"
}

# Создание .deb пакета
create_deb_package() {
    log "Создание .deb пакета..."

    # Удаление старой структуры и создание новой
    rm -rf "$BUILD_DIR"
    mkdir -p "$INSTALL_DIR"
    mkdir -p "$(dirname "$CONTROL_FILE")"

    # Копирование Python файлов
    cp "$PROJECT_DIR/Calculator_functions.py" "$INSTALL_DIR/"
    cp "$PROJECT_DIR/gui_calculator.py" "$INSTALL_DIR/"

    # Создание файла control
    cat <<EOF >"$CONTROL_FILE"
Package: gui-calculator
Version: 1.0.0
Architecture: all
Maintainer: youremail@example.com
Description: GUI-калькулятор на Python
EOF

    # Сборка пакета
    dpkg-deb --build "$BUILD_DIR" || {
        log "Ошибка при создании .deb пакета"
        exit 1
    }

    log ".deb пакет создан успешно!"
}

# Установка приложения
install_package() {
    log "Установка приложения..."
    sudo dpkg -i "$BUILD_DIR.deb" || {
        log "Ошибка при установке приложения"
        exit 1
    }
    log "Приложение установлено успешно!"
}

# Основной процесс
update_repository
build_project
run_tests
create_deb_package
install_package

log "Процесс завершён успешно!"
