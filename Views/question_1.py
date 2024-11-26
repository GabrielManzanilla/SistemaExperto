import tkinter as tk
import config as cfg  


class Scene1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#D9C3A0')  # Establecer el fondo del frame

        # Título con la pregunta
        question_label = tk.Label(self, text="¿A qué cultura pertenece el sitio que estas buscando?",
                                  font=("Arial", 14), bg='#D9C3A0')
        question_label.grid(row=0, column=0, columnspan=2, pady=10)


        row = 1
        column = 0
        for culture in cfg.estados:
            if culture == list(cfg.estados.keys())[-1]:
                button = tk.Button(self, text=culture, font=("Arial", 12), width=15, bg='#8b7d68',
                                            command=lambda c=culture: self.on_culture_selected(c))
                button.grid(row=row, column=column, columnspan=2, padx=1, pady=1)
            else:
                button = tk.Button(self, text=culture, font=("Arial", 12), width=15, bg='#8b7d68',
                                command=lambda c=culture: self.on_culture_selected(c))
                button.grid(row=row, column=column, padx=1, pady=1)
                column += 1
                if column > 1:  # Cambiar a la siguiente fila después de 2 botones
                    column = 0
                    row += 1

        # Botones de navegación
        # nav_button1 = tk.Button(self, text="←", font=("Arial", 14), width=5, bg='#8b7d68',
        #                         command=self.previous_scene)
        # nav_button1.grid(row=row + 1, column=0, pady=20)
        # nav_button2 = tk.Button(self, text="RETURN", font=("Arial", 14), width=5, bg='#8b7d68',
        #                         command=self.next_scene)
        # nav_button2.grid(row=row + 1, column=1, pady=20)

    def on_culture_selected(self, culture):
        """Acción al seleccionar una cultura."""
        cfg.cultura = culture
        self.controller.show_frame("Scene2")
        print(f"Cultura seleccionada: {culture}")
        # Aquí puedes manejar el cambio de escena u otra acción

    def previous_scene(self):
        """Cambiar a la escena anterior."""
        print("Navegar a la escena anterior")
        self.controller.show_frame("Scene1")
        

    def next_scene(self):
        """Cambiar a la siguiente escena."""
        print("Navegar a la siguiente escena")
        self.controller.show_frame("Scene1")  # Ejemplo de cambio de escena


# if __name__ == "__main__":
#     # Ejemplo mínimo para probar
#     class App(tk.Tk):
#         def __init__(self):
#             super().__init__()
#             self.title("Cultura Quiz")
#             self.geometry("400x500")
#             container = tk.Frame(self)
#             container.pack(fill="both", expand=True)
#             self
