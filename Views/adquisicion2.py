import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import shutil
import os
import config as cfg
from dictionary import sitios_arqueologicos

class Adquisicion2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#D9C3A0')  # Fondo beige como en la UI
        self.grid_columnconfigure(0, weight=1, minsize=75)
        self.grid_columnconfigure(1, weight=1, minsize=50)
        self.grid_columnconfigure(2, weight=1, minsize=75)

        # Variables para almacenar datos
        self.name_var = tk.StringVar()
        self.description_var = tk.StringVar()
        self.question_var = tk.StringVar()
        self.image_path = None  # Para almacenar la ruta de la imagen seleccionada

        self.image_label = tk.Label(self, bg='#D9C3A0')
        try:
            # Abrir y redimensionar la imagen con Pillow
            image = Image.open(f"assets/oops_img.jpg")
            image = image.resize((int(474/2), int(266/2)))  # Ajusta el tamaño de la imagen
            photo = ImageTk.PhotoImage(image)

            # Actualizar el widget de imagen
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Guardar referencia para evitar que se elimine la imagen
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
        self.image_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Título
        title_label = tk.Label(self, text="Oops!!\nParece que no conocemos el sitio.",
                               font=("Arial", 16, "bold"), bg='#D9C3A0', fg="black", justify="left")
        title_label.grid(row=1, column=0, columnspan=3, sticky="w", padx=20, pady=10)

        # Subtítulo
        subtitle_label = tk.Label(self, text="Ayúdanos a identificarlo con los pasos que se presentan a continuación",
                                  font=("Arial", 12), bg='#D9C3A0', fg="black", justify="left")
        subtitle_label.grid(row=2, column=0, columnspan=3, sticky="w", padx=20)

        # Imagen
        # self.image_label = tk.Label(self, text="(No hay imagen seleccionada)", font=("Arial", 12),
        #                             bg='#D9C3A0', fg="black")
        # self.image_label.grid(row=2, column=0, columnspan=2, pady=10)

        # Campo para ingresar el nombre
        name_label = tk.Label(self, text="Ingresa el nombre", font=("Arial", 12, "bold"),
                              bg='#D9C3A0', fg="black", anchor="w")
        name_label.grid(row=4, column=0, columnspan=3, sticky="w", padx=20, pady=(10, 0))
        self.name_entry = tk.Entry(self, textvariable=self.name_var, font=("Arial", 12), width=30, background="#8b7d68")
        self.name_entry.grid(row=5, column=0, columnspan=3, padx=20, pady=5)

        # Botón para subir imagen
        image_button_label = tk.Label(self, text="Sube una Imagen", font=("Arial", 12, "bold"),
                                      bg='#D9C3A0', fg="black", anchor="w")
        image_button_label.grid(row=6, column=0, columnspan=3, sticky="w", padx=20, pady=(10, 0))
        image_button = tk.Button(self, text="📷", font=("Arial", 14), bg="white", width=25, background="#8b7d68", relief="solid",
                                 command=self.upload_image)
        image_button.grid(row=7, column=0, columnspan=3, padx=20, pady=5)

        # Campo para ingresar descripción
        description_label = tk.Label(self, text="Ingresa una breve descripción", font=("Arial", 12, "bold"),
                                     bg='#D9C3A0', fg="black", anchor="w")
        description_label.grid(row=8, column=0, columnspan=3, sticky="w", padx=20, pady=(10, 0))
        description_text = tk.Text(self, font=("Arial", 12), height=5, width=30, wrap="word", background="#8b7d68")
        description_text.grid(row=9, column=0, columnspan=3, padx=20, pady=5)
        self.description_text_widget = description_text  # Referencia para obtener el texto después

        # Pregunta adicional
        question_label = tk.Label(self, text="Ingresa alguna descripción para identificarlo",
                                  font=("Arial", 12, "bold"), bg='#D9C3A0', fg="black", anchor="w")
        question_label.grid(row=10, column=0, columnspan=3, sticky="w", padx=20, pady=(10, 0))
        self.question_entry = tk.Entry(self, textvariable=self.question_var, font=("Arial", 12), width=30, background="#8b7d68")
        self.question_entry.grid(row=11, column=0, columnspan=3, padx=20, pady=5)

        # Botones de acción
        nav_button1 = tk.Button(self, text="<<", font=("Arial", 14), bg="#8b7d68", width=5, relief="solid",
                                command=self.reset_form)
        nav_button1.grid(row=12, column=0, pady=20, padx=10, sticky="e")

        nav_button2 = tk.Button(self, text="✔", font=("Arial", 14), bg="#8b7d68", width=5, relief="solid",
                                command=self.submit_data)
        nav_button2.grid(row=12, column=1, pady=20, padx=10)

        nav_button3 = tk.Button(self, text="X", font=("Arial", 14), bg="#8b7d68", width=5, relief="solid",
                                command=self.cancel)
        nav_button3.grid(row=12, column=2, pady=20, padx=10, sticky="w")

    def upload_image(self):
        """Abrir un diálogo para seleccionar una imagen."""
        file_path = filedialog.askopenfilename(filetypes=[("Imagenes", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image_path = file_path
            # Crear la carpeta 'imagenes' si no existe


            # Actualizar la etiqueta de la imagen
            self.image_label.config(text=f"Imagen: {os.path.basename(file_path)}")
            # self.image_label.config(text=f"Imagen: {file_path.split('/')[-1]}")

    def reset_form(self):
        """Restablecer todos los campos del formulario."""
        self.controller.show_frame("Scene1")

    def submit_data(self):
        """Obtener los datos de los inputs y mostrar un mensaje."""
        name = self.name_var.get()
        description = self.description_text_widget.get("1.0", tk.END).strip()
        question = self.question_var.get()

        if not name or not description or not self.image_path:
            messagebox.showerror("Error", "Por favor, completa todos los campos y sube una imagen.")
            return

        # Aquí puedes manejar los datos recolectados
        print(f"Nombre: {name}")
        print(f"Descripción: {description}")
        print(f"Pregunta: {question}")
        sitios_arqueologicos[(cfg.cultura,cfg.estado,cfg.geography,cfg.estructura, question)]=(name,self.image_path,description)
        if (cfg.cultura,cfg.estado,cfg.geography,cfg.estructura) not in cfg.respuestas:
            cfg.respuestas[(cfg.cultura,cfg.estado,cfg.geography,cfg.estructura)] = []
        cfg.respuestas[(cfg.cultura,cfg.estado,cfg.geography,cfg.estructura)].append(question)
        print(f"Sitios arqueologicos: {sitios_arqueologicos}")
        print(f"Respuestas: {cfg.respuestas}")

        print(f"Ruta de la imagen: {self.image_path}")
        if not os.path.exists('imagenes'):
            os.makedirs('imagenes')
        # Copiar la imagen a la carpeta 'imagenes'
        destination_path = os.path.join('imagenes', os.path.basename(self.image_path))
        shutil.copy(self.image_path, destination_path)

        messagebox.showinfo("Éxito", "Los datos se han enviado correctamente.")

    def cancel(self):
        """Cancelar y cerrar la aplicación (puedes modificar para navegar a otra escena)."""
        self.name_entry.delete(0, tk.END)
        self.description_text_widget.delete("1.0", tk.END)
        self.image_path = None
        self.question_entry.delete(0, tk.END)
        self.controller.show_frame("Adquisicion2")
