import tkinter as tk
import config as cfg  

class Scene2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#D9C3A0')

        self.dynamic_buttons = []  # Lista para almacenar botones dinámicos
        self.label = tk.Label(self, text="Escena 2", font=("Arial", 14), bg='#D9C3A0')
        self.label.grid(row=0, column=0, columnspan=2, pady=10)
        row = 5
        nav_button1 = tk.Button(self, text="←", font=("Arial", 14), width=5, bg='#8b7d68',
                                command=self.previous_scene)
        nav_button1.grid(row=row + 1, column=0, pady=20)
        nav_button2 = tk.Button(self, text="RETURN", font=("Arial", 14), width=5, bg='#8b7d68',
                                command=self.next_scene)
        nav_button2.grid(row=row + 1, column=1, pady=20)
        

    def update_scene(self):
        """Actualiza los botones dinámicamente basados en `cfg.cultura`."""
        for button in self.dynamic_buttons:
            button.destroy()  # Elimina los botones previos

        self.dynamic_buttons.clear()  # Limpia la lista

        row, column = 1, 0
        for estado in cfg.states_by_civilization.get(cfg.cultura, []):
            button = tk.Button(self, text=estado, font=("Arial", 12), bg='#8b7d68',
                               command=lambda e=estado: print(f"Seleccionaste: {e}"))
            button.grid(row=row, column=column, padx=10, pady=5)
            self.dynamic_buttons.append(button)  # Guarda el botón en la lista
            column += 1
            if column > 1:
                column = 0
                row += 1

        
    
    def previous_scene(self):
        """Cambiar a la escena anterior."""
        print("Navegar a la escena anterior")
        self.controller.show_frame("Scene1")
        

    def next_scene(self):
        """Cambiar a la siguiente escena."""
        print("Navegar a la siguiente escena")
        self.controller.show_frame("Scene1")  # Ejemplo de cambio de escena
