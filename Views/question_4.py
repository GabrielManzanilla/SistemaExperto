import tkinter as tk
import config as cfg
from request import search_coincidences

class Scene4(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#D9C3A0')  # Establecer el fondo del frame

        # Título con la pregunta
        question_label = tk.Label(self, text="¿En que tipo de geografia se encuentra el sitio que estas buscando?",
                                  font=("Arial", 14), bg='#D9C3A0')
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
        nav_button1 = tk.Button(self, text="←", font=("Arial", 14), width=5, bg='#8b7d68',
                                command=self.previous_scene)
        nav_button1.grid(row=row + 1, column=0, pady=20)
        nav_button2 = tk.Button(self, text="RTN", font=("Arial", 14), width=5, bg='#8b7d68',
                                command=self.first_scene)
        nav_button2.grid(row=row + 1, column=1, pady=20)


    def on_structure_selected(self, structure):
        """Acción al seleccionar la geografia."""
        cfg.estructura= structure
        print(f"Estrucutra seleccionada: {structure}")
        search_coincidences()
        

    def previous_scene(self):
        """Cambiar a la escena anterior."""
        print("Navegar a la escena anterior")
        self.controller.show_frame("Scene3")
        

    def first_scene(self):
        """Cambiar a la primera escena."""
        print("Navegar a la primera escena")
        self.controller.show_frame("Scene1")