import tkinter as tk
import config as cfg
from PIL import Image, ImageTk  # Importar Pillow para manejar imágenes
# from request import search_coincidences
from dictionary import sitios_arqueologicos

class Scene4(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#D9C3A0')  # Establecer el fondo del frame
        self.grid_columnconfigure(0, weight=1, minsize=100)  # Primera columna  
        self.grid_columnconfigure(1, weight=1, minsize=100)  # Segunda columna
        # Título con la pregunta

        self.image_label = tk.Label(self, bg='#D9C3A0')
        try:
            # Abrir y redimensionar la imagen con Pillow
            image = Image.open(f"assets/alux-question2.png")
            image = image.resize((253, 300))  # Ajusta el tamaño de la imagen
            photo = ImageTk.PhotoImage(image)

            # Actualizar el widget de imagen
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Guardar referencia para evitar que se elimine la imagen
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
        self.image_label.grid(row=0, column=0, columnspan=3, pady=10)

        question_label = tk.Label(self, text="¿En qué tipo de estructura recuerdas que se encuentra el sitio que estas buscando?",
                                  font=("Arial", 14), bg='#D9C3A0',  wraplength=490)
        question_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Generar botones dinámicamente a partir de los elementos en geografias`
        row = 2
        column = 0
        for estructura in cfg.estructuras:
            button = tk.Button(self, text=estructura, font=("Arial", 12), width=15, bg='#8b7d68',
                               command=lambda e= estructura: self.on_structure_selected(e))
            button.grid(row=row, column=column, padx=10, pady=5)
            column += 1
            if column > 1:  # Cambiar a la siguiente fila después de 2 botones
                column = 0
                row += 1

        # Botones de navegación
        nav_button1 = tk.Button(self, text="<<", font=("Arial", 14), width=5, bg='#8b7d68',
                                command=self.previous_scene)
        nav_button1.grid(row=row + 1, column=0, padx=10,pady=20, sticky="e")
        nav_button2 = tk.Button(self, text="X", font=("Arial", 14), width=5, bg='#8b7d68',
                                command=self.first_scene)
        nav_button2.grid(row=row + 1, column=1, padx=10,pady=20, sticky="w")


    def on_structure_selected(self, structure):
        """Acción al seleccionar la geografia."""
        cfg.estructura= structure
        clave=(cfg.cultura,cfg.estado,cfg.geography,cfg.estructura)
        print(clave)
        # cfg.cultura = cfg.estado = cfg.geography = cfg.estructura = ""
        if clave in cfg.respuestas:
            cfg.adition_condition=cfg.respuestas[clave][cfg.contador]
            self.controller.show_frame("AdicionalQuestion")
        else:
            if clave in sitios_arqueologicos:
                (nombre,path_image,descripcion)=sitios_arqueologicos[clave]
                print(f"Nombre: {nombre} {path_image} {descripcion}")
                cfg.nombre=nombre
                cfg.path_image=path_image
                cfg.descripcion=descripcion
                self.controller.show_frame("Answer")
            else:
                self.controller.show_frame("Adquisicion1")
        

    def previous_scene(self):
        """Cambiar a la escena anterior."""
        print("Navegar a la escena anterior")
        self.controller.show_frame("Scene3")
        

    def first_scene(self):
        """Cambiar a la primera escena."""
        print("Navegar a la primera escena")
        self.controller.show_frame("Scene1")

