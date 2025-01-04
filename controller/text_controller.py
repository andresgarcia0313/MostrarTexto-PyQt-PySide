# pylint: disable=no-name-in-module
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

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
        # Actualizamos el texto en el modelo
        self.model.update_text()
        # Actualizamos el texto de la etiqueta en la vista
        self.view.label.setText(self.model.text)
