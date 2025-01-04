# pylint: disable=no-name-in-module
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# Importamos las clases necesarias de PySide6 para crear widgets
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
)


# Esta clase representa la vista de nuestra aplicación
class TextView(QWidget):
    def __init__(self):
        super().__init__()
        # Creamos una etiqueta (label) para mostrar texto
        self.label = QLabel()
        # Creamos una entrada de texto
        self.text_input = QLineEdit()
        # Creamos un botón que dice "Cambiar"
        self.button = QPushButton("Cambiar")
        # Aplicamos estilos personalizados al botón
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                margin: 4px 2px;
            }
            QPushButton:hover {
                background-color: white;
                color: black;
                border: 2px solid #4CAF50;
            }
        """)
        # Creamos un diseño vertical para organizar los widgets
        layout = QVBoxLayout()
        # Añadimos la etiqueta al diseño
        layout.addWidget(self.label)
        # Añadimos la entrada de texto al diseño
        layout.addWidget(self.text_input)
        # Añadimos el botón al diseño
        layout.addWidget(self.button)
        # Establecemos el diseño en el widget principal
        self.setLayout(layout)

    def get_input_text(self):
        return self.text_input.text()
