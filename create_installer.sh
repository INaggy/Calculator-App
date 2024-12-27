#!/bin/bash
echo "Создание структуры .deb пакета..."

# Переменные
BUILD_DIR="deb_build"
INSTALL_DIR="$BUILD_DIR/usr/bin"
CONTROL_FILE="$BUILD_DIR/DEBIAN/control"

# Удаляем старую структуру
rm -rf "$BUILD_DIR"
mkdir -p "$INSTALL_DIR"
mkdir -p "$(dirname "$CONTROL_FILE")"

# Копируем Python файлы
cp Calculator_functions.py "$INSTALL_DIR/"
cp gui_calculator.py "$INSTALL_DIR/"

# Создаём файл control
cat <<EOF >"$CONTROL_FILE"
Package: gui-calculator
Version: 1.0.0
Architecture: all
Maintainer: grigoryd2004@gmail.com
Description: GUI-калькулятор на Python
EOF

echo "Структура для .deb пакета создана!"
