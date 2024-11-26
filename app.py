import tkinter as tk
from Views.question_1 import Scene1
from Views.question_2 import Scene2  # Asegúrate de importar todas las escenas necesarias
from Views.question_3 import Scene3
from Views.question_4 import Scene4
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mi Aplicación")
        self.geometry("500x600+{}+{}".format(
        (self.winfo_screenwidth() - 500) // 2, (self.winfo_screenheight() - 600) // 2))
        self.configure(bg='#D9C3A0')  # Establecer el fondo del contenedor principal

        # Contenedor para las escenas
        self.container = tk.Frame(self, bg='#D9C3A0')
        self.container.pack(fill="both", expand=True)
        self.container.place(relx=0.5, rely=0.5, anchor="center")

        # Diccionario para guardar las escenas
        self.frames = {}

        # Inicializar escenas
        for SceneClass in (Scene1, Scene2,Scene3, Scene4):
            frame = SceneClass(self.container, self)
            self.frames[SceneClass.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_columnconfigure(1, weight=1)

        # Mostrar la primera escena
        self.show_frame("Scene1")

    def show_frame(self, scene_name):
        """Muestra la escena especificada."""
        frame = self.frames[scene_name]
        if hasattr(frame, "update_scene"):
            frame.update_scene()  # Llama al método de actualización si existe
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
