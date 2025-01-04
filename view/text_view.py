# pylint: disable=no-name-in-module
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

# Importamos las clases necesarias de PySide6 para crear widgets
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout


# Esta clase representa la vista de nuestra aplicación
class TextView(QWidget):
    def __init__(self):
        super().__init__()
        # Creamos una etiqueta (label) para mostrar texto
        self.label = QLabel()
        # Creamos un botón que dice "Cambiar"
        self.button = QPushButton("Cambiar")
        # Creamos un diseño vertical para organizar los widgets
        layout = QVBoxLayout()
        # Añadimos la etiqueta al diseño
        layout.addWidget(self.label)
        # Añadimos el botón al diseño
        layout.addWidget(self.button)
        # Establecemos el diseño en el widget principal
        self.setLayout(layout)
