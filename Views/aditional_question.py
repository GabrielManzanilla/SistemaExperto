import tkinter as tk
from PIL import Image, ImageTk  # Importar Pillow para manejar imágenes
import config as cfg  # Asegúrate de que config tenga los atributos necesarios
from dictionary import sitios_arqueologicos  # Importar el diccionario de sitios arqueológicos

class AdicionalQuestion(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#D9C3A0')

        # Widgets predefinidos para reutilización
        self.name_label = tk.Label(self, text="Acaso", font=("Arial", 14), bg='#D9C3A0')
        self.name_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.true_button = tk.Button(self, text="SI", font=("Arial", 14), width=10, bg='#8b7d68',
                                     command=self.second_search)
        self.true_button.grid(row=1, column=0, padx=10, pady=10)

        self.false_button = tk.Button(self, text="NO", font=("Arial", 14), width=10, bg='#8b7d68',
                                     command=self.next_question)
        self.false_button.grid(row=1, column=0, padx=10, pady=10)


        self.nav_button = tk.Button(self, text="RETURN", font=("Arial", 14), width=10, bg='#8b7d68',
                                    command=self.first_scene)
        self.nav_button.grid(row=3, column=0, columnspan=2, pady=20)

    def update_scene(self):
        """Actualiza los widgets con los datos actuales de cfg."""
        # Actualizar el nombre
        self.name_label.config(text=f"Acaso este sitio... {cfg.adition_condition}")

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

    def next_question(self):
        """Navegar a la siguiente pregunta."""
        clave=(cfg.cultura,cfg.estado,cfg.geography,cfg.estructura)
        cfg.contador += 1
        cfg.adition_condition=cfg.respuestas[clave][cfg.contador]
        self.controller.show_frame("AdicionalQuestion")

    def second_search(self):
        """Realizar la segunda búsqueda."""
        clave=(cfg.cultura,cfg.estado,cfg.geography,cfg.estructura, cfg.adition_info)
        (nombre,path_image,descripcion)=sitios_arqueologicos[clave]
        cfg.nombre=nombre
        cfg.path_image=path_image
        cfg.descripcion=descripcion
        self.controller.show_frame("Answer")