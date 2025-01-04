# pylint: disable=no-name-in-module
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from PySide6.QtCore import QTimer

# Esta clase representa el controlador de nuestra aplicación
class TextController:
    def __init__(self, model, view):
        # Guardamos el modelo y la vista
        self.model = model
        self.view = view
        # Establecemos el texto de la etiqueta en la vista usando el texto
        # del modelo
        self.view.label.setText(self.model.text)
        # Conectamos el clic del botón a la función update_text
        self.view.button.clicked.connect(self.update_text)

    def update_text(self):
        new_text = self.view.get_input_text()
        self.model.update_text(new_text)
        self.view.label.setText(self.model.text)
        # Cambiar el texto del botón después de actualizar el texto
        self.view.button.setText("Texto actualizado")
        # Restaurar el texto original del botón después de 2 segundos
        QTimer.singleShot(2000, lambda: self.view.button.setText("Cambiar"))
