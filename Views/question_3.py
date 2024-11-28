import tkinter as tk
from PIL import Image, ImageTk  # Importar Pillow para manejar imágenes
import config as cfg

class Scene3(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#D9C3A0')  # Establecer el fondo del frame
        self.grid_columnconfigure(0, weight=1, minsize=100)  # Primera columna  
        self.grid_columnconfigure(1, weight=1, minsize=100)  # Segunda columna

        self.image_label = tk.Label(self, bg='#D9C3A0')
        try:
            # Abrir y redimensionar la imagen con Pillow
            image = Image.open(f"assets/alux-question.png")
            image = image.resize((253, 300))  # Ajusta el tamaño de la imagen
            photo = ImageTk.PhotoImage(image)

            # Actualizar el widget de imagen
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Guardar referencia para evitar que se elimine la imagen
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
        self.image_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Título con la pregunta
        question_label = tk.Label(self, text=f"¿Que tipo de geografia tiene el sitio que estas buscando?",
                                  font=("Arial", 14), bg='#D9C3A0', wraplength=490)
        question_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Generar botones dinámicamente a partir de los elementos en geografias`
        row = 2
        column = 0
        for geography in cfg.geografias:
            button = tk.Button(self, text=geography, font=("Arial", 12), width=15, bg='#8b7d68',
                               command=lambda g= geography: self.on_geography_selected(g))
            button.grid(row=row, column=column, padx=10, pady=5)
            column += 1
            if column > 1:  # Cambiar a la siguiente fila después de 2 botones
                column = 0
                row += 1

        # Botones de navegación
        nav_button1 = tk.Button(self, text="<<", font=("Arial", 14), width=5, bg='#8b7d68',
                                command=self.previous_scene)
        nav_button1.grid(row=row + 1, column=0, padx=10, pady=20, sticky="e")
        nav_button2 = tk.Button(self, text="X", font=("Arial", 14), width=5, bg='#8b7d68',
                                command=self.first_scene)
        nav_button2.grid(row=row + 1, column=1, padx=10, pady=20, sticky="w")


    def on_geography_selected(self, geography):
        """Acción al seleccionar la geografia."""
        cfg.geography = geography
        self.controller.show_frame("Scene4")
        print(f"Geografia seleccionada: {geography}")
        

    def previous_scene(self):
        """Cambiar a la escena anterior."""
        print("Navegar a la escena anterior")
        self.controller.show_frame("Scene2")
        

    def first_scene(self):
        """Cambiar a la primera escena."""
        print("Navegar a la primera escena")
        self.controller.show_frame("Main")
