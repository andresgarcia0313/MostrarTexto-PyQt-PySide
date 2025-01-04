# pylint: disable=no-name-in-module
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# Importamos las clases de PySide6 para crear una aplicación de escritorio.
from PySide6.QtWidgets import QApplication, QMainWindow
# Importamos las clases del modelo, la vista y el controlador
from model.text_model import TextModel
from view.text_view import TextView
from controller.text_controller import TextController

# Este es el punto de entrada de nuestra aplicación
if __name__ == "__main__":
    # Creamos una aplicación de escritorio
    app = QApplication([])
    # Creamos el modelo, que maneja los datos
    model = TextModel()
    # Creamos la vista, que muestra la interfaz al usuario
    view = TextView()
    # Creamos el controlador, que maneja la lógica entre el modelo y la vista
    controller = TextController(model, view)
    # Creamos la ventana principal de la aplicación
    main_window = QMainWindow()
    # Establecemos la vista como el contenido principal de la ventana
    main_window.setCentralWidget(view)
    # Ponemos un título a la ventana
    main_window.setWindowTitle("Software")
    # Establecemos un tamaño fijo para la ventana
    main_window.setFixedSize(400, 150)
    # Mostramos la ventana al usuario
    main_window.show()
    # Iniciamos la aplicación para que espere y responda a eventos del usuario
    app.exec()
