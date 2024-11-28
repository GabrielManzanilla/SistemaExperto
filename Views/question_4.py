import tkinter as tk
import config as cfg
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
        question_label = tk.Label(self, text="¿En que tipo de geografia se encuentra el sitio que estas buscando?",
                                  font=("Arial", 14), bg='#D9C3A0',  wraplength=490)
        question_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Generar botones dinámicamente a partir de los elementos en geografias`
        row = 1
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
        nav_button1.grid(row=row + 1, column=0, pady=20)
        nav_button2 = tk.Button(self, text="X", font=("Arial", 14), width=5, bg='#8b7d68',
                                command=self.first_scene)
        nav_button2.grid(row=row + 1, column=1, pady=20)


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

