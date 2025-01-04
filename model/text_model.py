# pylint: disable=no-name-in-module
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# Esta clase representa el modelo de nuestra aplicación
class TextModel:
    def __init__(self):
        # Inicializamos el texto con un valor por defecto
        self.text = "Texto inicial"

    def update_text(self, new_text):
        # Actualizamos el texto con el nuevo valor proporcionado
        self.text = new_text
