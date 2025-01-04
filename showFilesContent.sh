#!/bin/bash
clear
# Directorio de trabajo
DIRECTORIO="/home/andres/Desarrollo/Python/MostrarTexto PyQt PySide"

# Buscar y mostrar el contenido de los archivos .py, excluyendo README y la carpeta .venv
find "$DIRECTORIO" -path "$DIRECTORIO/.venv" -prune -o -name "*.py" -not -name "README" -print | while read -r file; do
    echo "Archivo: ${file#$DIRECTORIO/}"
    grep -v '^\s*#' "$file"
    echo -e "\n"
done