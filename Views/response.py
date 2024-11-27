import tkinter as tk
from PIL import Image, ImageTk  # Importar Pillow para manejar imágenes
import config as cfg  # Asegúrate de que config tenga los atributos necesarios

class Answer(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#D9C3A0')

        # Widgets predefinidos para reutilización
        self.name_label = tk.Label(self, text="Nombre", font=("Arial", 14), bg='#D9C3A0')
        self.name_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.image_label = tk.Label(self, bg='#D9C3A0')
        self.image_label.grid(row=1, column=0, columnspan=2, pady=10)

        self.description_label = tk.Label(self, text="Descripción", font=("Arial", 12), bg='#D9C3A0')
        self.description_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.nav_button = tk.Button(self, text="RETURN", font=("Arial", 14), width=10, bg='#8b7d68',
                                    command=self.first_scene)
        self.nav_button.grid(row=3, column=0, columnspan=2, pady=20)

        self.nav_button = tk.Button(self, text="NO ES", font=("Arial", 14), width=10, bg='#8b7d68',
                                    command=self.append_adquisicion)
        self.nav_button.grid(row=3, column=1, columnspan=2, pady=20)

    def update_scene(self):
        """Actualiza los widgets con los datos actuales de cfg."""
        # Actualizar el nombre
        self.name_label.config(text=cfg.nombre)

        # Manejar la carga de la imagen con Pillow
        try:
            # Abrir y redimensionar la imagen con Pillow
            image = Image.open(cfg.path_image)
            image = image.resize((200, 200))  # Ajusta el tamaño de la imagen
            photo = ImageTk.PhotoImage(image)

            # Actualizar el widget de imagen
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Guardar referencia para evitar que se elimine la imagen
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")  # Mostrar el error en la consola

        # Actualizar la descripción
        self.description_label.config(text=cfg.descripcion)

    def first_scene(self):
        """Navegar a la primera escena."""
        cfg.nombre = ""
        cfg.path_image = ""
        cfg.descripcion = ""
        cfg.cultura = ""
        cfg.estado = ""
        cfg.geography = ""
        cfg.estructura = ""
        cfg.adition_info = ""
        self.controller.show_frame("Scene1")

    def append_adquisicion(self):
        """Navegar a la primera escena."""
        self.controller.show_frame("Adquisicion2")
