import tkinter as tk

class Scene1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Escena 1", font=("Arial", 18))
        label.pack(pady=20)

        button = tk.Button(self, text="Ir a Escena 2",
                           command=lambda: controller.show_frame("Scene2"))
        button.pack()
