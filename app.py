import tkinter as tk
from Views.question_1 import Scene1
from Views.question_2 import Scene2  # Asegúrate de importar todas las escenas necesarias
from Views.question_3 import Scene3
from Views.question_4 import Scene4
from Views.response import Answer
from Views.aditional_question import AdicionalQuestion
from Views.adquisicion1 import Adquisicion1
from Views.adquisicion2 import Adquisicion2 
from Views.response_details import AnswerDetails

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sitios Arqueológicos de México")
        
        # Dimensiones de la ventana
        width = 550
        height = 600
        
        # Calcular la posición central
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        #self.resizable(False, False)
        # Configurar tamaño y posición de la ventana
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.configure(bg='#D9C3A0')  # Establecer el fondo del contenedor principal
        
        # Contenedor para las escenas
        self.container = tk.Frame(self, bg='#D9C3A0')
        self.container.pack(fill="both", expand=True)
        
        
        # Diccionario para guardar las escenas
        self.frames = {}
        
        # Inicializar escenas
        for SceneClass in (Scene1, Scene2, Scene3, Scene4, Answer, AnswerDetails, Adquisicion1, Adquisicion2, AdicionalQuestion):
            frame = SceneClass(self.container, self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[SceneClass.__name__] = frame
        
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

