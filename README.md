# MostrarTexto-PyQt-PySide

Este repositorio contiene un ejemplo simple de una aplicación de interfaz gráfica de usuario (GUI) utilizando **PyQt** y **PySide6**. La aplicación es un ejemplo básico del patrón **MVC (Modelo-Vista-Controlador)** donde se muestra un texto que se puede actualizar al presionar un botón.

## Requisitos

- **Python 3.x** (se recomienda usar una versión reciente de Python).
- **PySide6** (para la interfaz gráfica).
  
  Puedes instalar los requisitos utilizando `pip`:

  ```bash
  pip install -r requirements.txt
  ```

  Si no tienes el archivo `requirements.txt`, puedes instalar PySide6 manualmente con:

  ```bash
  pip install PySide6
  ```

## Estructura del Proyecto

La estructura básica del repositorio es la siguiente:

```
MostrarTexto-PyQt-PySide/
│
├── controller/
│   └── text_controller.py        # Controlador de la aplicación (conecta el modelo y la vista).
│
├── model/
│   └── text_model.py             # Lógica del modelo (gestiona los datos de la aplicación).
│
├── view/
│   └── text_view.py              # Vista de la aplicación (interfaz gráfica).
│
├── main.py                       # Archivo principal para ejecutar la aplicación.
└── requirements.txt              # Lista de dependencias de la aplicación.
```

## Descripción del Código

- **main.py**: Este es el punto de entrada de la aplicación. Inicializa la aplicación, el modelo, la vista y el controlador. Luego, conecta la vista con el controlador y muestra la ventana principal.
  
- **model/text_model.py**: El modelo gestiona los datos, en este caso el texto que se muestra en la interfaz. Contiene un texto inicial y un método para actualizarlo.

- **view/text_view.py**: La vista se encarga de mostrar los elementos gráficos de la interfaz. En este caso, contiene un `QLabel` para mostrar el texto y un `QPushButton` para actualizar el texto.

- **controller/text_controller.py**: El controlador es el encargado de manejar la lógica de interacción entre el modelo y la vista. En este caso, conecta el botón de la vista con la acción de actualizar el texto en el modelo.

## Licencia

Este código se distribuye bajo la licencia **MIT**. Puedes usarlo y modificarlo libremente, pero cualquier modificación también debe estar disponible como código abierto.

## Cómo Ejecutar el Proyecto

Para ejecutar el proyecto, sigue estos pasos:

1. Clona el repositorio:

   ```bash
   git clone https://github.com/andresgarcia0313/MostrarTexto-PyQt-PySide.git
   ```

2. Navega a la carpeta del proyecto:

   ```bash
   cd MostrarTexto-PyQt-PySide
   ```

3. Crea un entorno virtual y actívalo (opcional pero recomendado):

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # En Linux/macOS
   .venv\Scripts\activate      # En Windows
   ```

4. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

5. Ejecuta la aplicación:

   ```bash
   python main.py
   ```

La ventana de la aplicación debería abrirse con un botón "Cambiar". Al hacer clic en el botón, el texto en la ventana cambiará de "Texto inicial" a "Texto actualizado".

## Contribuciones

Las contribuciones al proyecto son bienvenidas. Si encuentras algún problema o tienes ideas para mejorar la aplicación, puedes hacer un **fork** del repositorio y crear un **pull request**.

## Contacto

Si tienes alguna duda o sugerencia, no dudes en abrir un **issue** en el repositorio.

---

¡Gracias por usar este proyecto!

## Dependencias con apt

Para configurar el entorno de desarrollo sin usar `venv`, puede instalar las dependencias necesarias utilizando `apt`. Ejecute los siguientes comandos:

```sh
sudo apt update
sudo apt install python3-pyside6.qtcore python3-pyside6.qtgui python3-pyside6.qtwidgets python3-pyside6.qtqml python3-pyside6.qtquick -y
sudo apt install python3-pyside6.qt3danimation python3-pyside6.qt3dcore python3-pyside6.qt3drender -y
sudo apt install python3-pyside6.qtnetwork python3-pyside6.qtmultimedia -y

```
