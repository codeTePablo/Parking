# image
from PIL import Image, ImageTk

# interface
import tkinter as tk
from tkinter import ttk

# arduino / esp32
import serial

# date
import time
import datetime

# modelos
from model.person import Person
from model.guest import Guest
from model.admin import Admin

from model.password import Password

# database
from db import get_connection
import db


class Windows:
    def __init__(self, root):
        self.root = root
        self.root.title("Parking System UAEMEX")
        self.root.geometry("790x580")
        self.root.resizable(False, False)

        self.admin = Admin()

        # set background image of the window
        image = Image.open("img/background.jpg")
        self.background_image = ImageTk.PhotoImage(image)
        # Crear el label de fondo con la imagen
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        image = Image.open("img/huella_3.png")
        image = image.resize((200, 200), Image.LANCZOS)
        self.huella_image = ImageTk.PhotoImage(image)
        self.huella_label = tk.Label(root, image=self.huella_image, bg=None)
        self.huella_label.place(x=300, y=200)

        self.title_label = tk.Label(
            self.root,
            text="Bienvenido",
            font=("Agency FB", 40),
            bg="#EEC591",
            fg="white",
        )
        self.title_label.place(x=310, y=140)

        self.title_label_login = tk.Label(
            self.root,
            text="Login as ",
            font=("Agency FB", 15),
            bg="#EEC591",
            fg="white",
        )
        self.title_label_login.place(x=590, y=180)

        self.boton_principal_login = ttk.Style()
        self.boton_principal_login.configure(
            "Estilo.TButton",
            font=("Agency FB", 15),
            background="#4CAF50",
            foreground="Black",
            # color
        )
        self.boton_principal_login = ttk.Button(
            root,
            text="Administrador",
            style="Estilo.TButton",
            command=self.admin_window,
        )
        self.boton_principal_login.pack(pady=20)
        self.boton_principal_login.place(x=10, y=10)

        self.boton_principal_user = ttk.Style()
        self.boton_principal_user.configure(
            "Estilo.TButton",
            font=("Agency FB", 15),
            background="#4CAF50",
            foreground="Black",
        )
        self.boton_principal_user = ttk.Button(
            root,
            text="Usuario",
            style="Estilo.TButton",
            command=self.open_window_user,
        )
        self.boton_principal_user.pack(pady=20)
        self.boton_principal_user.place(x=570, y=250)

        self.boton_principal_guest = ttk.Style()
        self.boton_principal_guest.configure(
            "Estilo.TButton",
            font=("Agency FB", 15),
            background="#4CAF50",
            foreground="Black",
        )
        self.boton_principal_guest = ttk.Button(
            root,
            text="Invitado",
            style="Estilo.TButton",
            command=self.open_window_guest,
        )
        self.boton_principal_guest.pack(pady=20)
        self.boton_principal_guest.place(x=570, y=300)

        self.boton_principal_guest_exit = ttk.Style()
        self.boton_principal_guest_exit.configure(
            "Estilo.TButton",
            font=("Agency FB", 15),
            background="#4CAF50",
            foreground="Black",
        )
        self.boton_principal_guest_exit = ttk.Button(
            root,
            text="Registrar salida",
            style="Estilo.TButton",
            command=self.reg_exit_guest,
        )
        self.boton_principal_guest_exit.pack(pady=20)
        self.boton_principal_guest_exit.place(x=340, y=450)

    def admin_window(self):
        self.root.title("Input Box")
        self.root.geometry("550x580")
        self.root.resizable(False, False)

        # set background image of the window
        image_admin_login = Image.open("img/background_admin_1.jpg")
        self.background_image_admin_login = ImageTk.PhotoImage(image_admin_login)
        # Crear el label de fondo con la imagen
        self.background_label_admin_login = tk.Label(
            self.root, image=self.background_image_admin_login
        )
        self.background_label_admin_login.place(x=0, y=0, relwidth=1, relheight=1)

        show_password_var = tk.BooleanVar()
        show_password_var.set(False)

        # generar un label con texto
        self.label_title = tk.Label(
            self.root, text="Admin", font=("Helvetica", 10), fg="white", bg="#66CDAA"
        )
        self.label_title.pack(pady=0)
        self.label_title.place(x=260, y=70)

        # entry user name
        self.entry_user = tk.Entry(
            self.root,
        )
        self.entry_user.pack(pady=10)
        self.entry_user.place(x=220, y=100)

        # Crear el cuadro de entrada en el Toplevel
        self.entry_pass = tk.Entry(
            self.root,
            show="*",
        )
        self.entry_pass.pack(pady=10)
        self.entry_pass.place(x=220, y=150)

        # agregar un checkbox para poder ver la contraseña
        checkbutton = tk.Checkbutton(
            self.root,
            text="Mostrar Contraseña",
            variable=show_password_var,
            command=lambda: self.toggle_show_password(
                self.entry_pass, show_password_var
            ),
        )
        checkbutton.pack()
        checkbutton.place(x=220, y=200)

        # Crear el botón en el Toplevel
        button = tk.Button(
            self.root,
            text="Entrar",
            command=lambda: self.check_credentials(
                self.entry_user.get(), self.entry_pass.get(), self.open_menu_admin
            ),
        )
        button.pack()
        button.place(x=260, y=250)

    def toggle_show_password(self, entry, show_password_var):
        # Mostrar u ocultar la contraseña según el estado del Checkbutton
        show_password = show_password_var.get()
        if show_password:
            entry.config(show="")
        else:
            entry.config(show="*")

    def check_credentials(self, input_user, input_pass, toplevel):
        admin_user = ""
        admin_pass = ""
        if input_user == admin_user and input_pass == admin_pass:
            self.open_menu_admin()
        else:
            popup = tk.Toplevel(self.root)
            popup.title("Error")
            label_error = tk.Label(
                popup,
                text="Usuario o contraseña incorrectos",
                fg="black",
                bg="cyan",
            )
            label_error.pack(padx=20, pady=10)

    def open_menu_admin(self):
        # self.frame_update_window.destroy()
        # self.frame_update.destroy()

        self.root.title("Admin")
        self.root.geometry("790x580")
        self.root.resizable(False, False)

        # set background image of the window
        image_crud = Image.open("img/background_crud.jpg")
        self.background_image_crud = ImageTk.PhotoImage(image_crud)
        # Crear el label de fondo con la imagen
        self.background_label_crud = tk.Label(
            self.root, image=self.background_image_crud
        )
        self.background_label_crud.place(x=0, y=0, relwidth=1, relheight=1)

        # create 4 buttons for CRUD
        self.boton_principal_login = ttk.Style()
        self.boton_principal_login.configure(
            "Estilo.TButton",
            font=("Agency FB", 15),
            background="#4CAF50",
            foreground="Black",
            # color
        )
        self.boton_principal_login = ttk.Button(
            self.root,
            text="Registrar",
            style="Estilo.TButton",
            command=self.create_new_users,
        )
        self.boton_principal_login.pack(pady=20)
        self.boton_principal_login.place(x=350, y=200)

        self.boton_principal_read = ttk.Style()
        self.boton_principal_read.configure(
            "Estilo.TButton",
            font=("Agency FB", 15),
            background="#4CAF50",
            foreground="Black",
        )
        self.boton_principal_read = ttk.Button(
            self.root,
            text="Update",
            style="Estilo.TButton",
            command=self.crud,
        )
        self.boton_principal_read.pack(pady=20)
        self.boton_principal_read.place(x=350, y=250)

        self.boton_principal_back = ttk.Style()
        self.boton_principal_back.configure(
            "Estilo.TButton",
            font=("Agency FB", 15),
            background="#4CAF50",
            foreground="Black",
        )
        self.boton_principal_back = ttk.Button(
            self.root,
            text="Regresar",
            style="Estilo.TButton",
            command=lambda: self.__init__(self.root),
        )
        self.boton_principal_back.pack(pady=20)
        self.boton_principal_back.place(x=350, y=500)

    def create_new_users(self):
        self.root.title("Ventana Secundaria")
        self.root.geometry("790x580")
        self.root.resizable(False, False)

        self.frame_create = tk.Frame(
            self.root,
            highlightbackground="#66CDAA",
            highlightcolor="#66CDAA",
            highlightthickness=5,
        )
        self.frame_create.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        self.label_verde = tk.Label(self.frame_create, text="", bg="#66CDAA")
        self.label_verde.pack(expand=True, fill=tk.BOTH)

        # crear un label dentro del self.frame_create con el texto "Registro"
        self.label_registro = tk.Label(
            self.label_verde,
            text="Nuevo usuario",
            font=("Agency FB", 27),
            bg="#66CDAA",
            fg="white",
        )
        self.label_registro.pack(pady=0)
        self.label_registro.place(x=15, y=50)

        self.label_registro_nombre = tk.Label(
            self.label_verde,
            text="Nombre",
            font=("Agency FB", 13),
            bg="#66CDAA",
            fg="white",
        )
        self.label_registro_nombre.pack(pady=0)
        self.label_registro_nombre.place(x=50, y=120)

        self.textbox_nombre = tk.Entry(self.label_verde)
        self.textbox_nombre.pack(padx=5)
        self.textbox_nombre.place(x=50, y=150)

        self.label_registro_apellido = tk.Label(
            self.label_verde,
            text="Apellido",
            font=("Agency FB", 13),
            bg="#66CDAA",
            fg="white",
        )
        self.label_registro_apellido.pack(pady=0)
        self.label_registro_apellido.place(x=50, y=170)

        self.textbox_apellido = tk.Entry(self.label_verde)
        self.textbox_apellido.pack(padx=5)
        self.textbox_apellido.place(x=50, y=195)

        self.label_registro_numero_cuenta = tk.Label(
            self.label_verde,
            text="Numero de cuenta",
            font=("Agency FB", 13),
            bg="#66CDAA",
            fg="white",
        )
        self.label_registro_numero_cuenta.pack(pady=0)
        self.label_registro_numero_cuenta.place(x=50, y=220)

        self.textbox_numero_cuenta = tk.Entry(self.label_verde)
        self.textbox_numero_cuenta.pack(padx=5)
        self.textbox_numero_cuenta.place(x=50, y=245)

        self.label_registro_numero_placa = tk.Label(
            self.label_verde,
            text="Numero de placa",
            font=("Agency FB", 13),
            bg="#66CDAA",
            fg="white",
        )
        self.label_registro_numero_placa.pack(pady=0)
        self.label_registro_numero_placa.place(x=50, y=270)

        self.textbox_numero_placa = tk.Entry(self.label_verde)
        self.textbox_numero_placa.pack(padx=0)
        self.textbox_numero_placa.place(x=50, y=295)

        self.boton_escanear = tk.Button(
            self.label_verde,
            text="Escanear huella",
            # command=self.escanear_huella_arduino
        )
        self.boton_escanear.pack(side=tk.BOTTOM)
        self.boton_escanear.place(x=60, y=340)

        self.boton_recopilar = tk.Button(
            self.label_verde, text="Registrar", command=self.recopilar_texto
        )
        self.boton_recopilar.pack(side=tk.BOTTOM)
        self.boton_recopilar.place(x=65, y=480)

        self.boton_cerrar = tk.Button(
            self.root, text="Cerrar", command=self.open_menu_admin
        )
        self.boton_cerrar.pack(side=tk.BOTTOM)
        self.boton_cerrar.place(x=75, y=540)

        frame2 = tk.Frame(self.root)
        frame2.pack(pady=5, side=tk.RIGHT)

        # set into frame2 the image of the fingerprint
        image = Image.open("img/background_login.jpg")
        image = image.resize((580, 600), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        etiqueta_imagen_huella = tk.Label(frame2, image=image)
        etiqueta_imagen_huella.image = image
        etiqueta_imagen_huella.pack()

    def crud(self):
        self.root.title("CRUD")
        self.root.geometry("790x580")
        self.root.resizable(False, False)

        self.frame_update = tk.Frame(
            self.root,
            highlightbackground="#66CDAA",
            highlightcolor="#66CDAA",
            highlightthickness=5,
        )
        # self.frame_update.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        self.frame_update.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        style = ttk.Style(self.frame_update)
        style.theme_use("default")
        style.configure(
            "Treeview",
            background="white",
            foreground="black",
            rowheight=25,
            fieldbackground="white",
        )
        style.map("Treeview", background=[("selected", "#347083")])
        style.configure("Treeview.Heading", background="#347083", foreground="white")
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
        style.configure("TCombobox", fieldbackground="#D3D3D3")
        self.frame_update.configure(background="#D3D3D3")

        admin = Admin()
        data = admin.get_data()

        self.users_data = data
        columns = ["id", "name", "surname", "num_cuenta", "num_placa", "finger"]
        self.tree = ttk.Treeview(self.frame_update, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=100)

        for user in self.users_data:
            self.tree.insert("", "end", values=user)

        self.tree.pack(pady=20)

        self.user_combobox = ttk.Combobox(
            self.frame_update,
            values=[f"{user[0]}: {user[1]} {user[2]}" for user in self.users_data],
        )
        self.user_combobox.pack(pady=10)

        # Botones "Update" y "Delete"
        self.update_button = tk.Button(
            self.frame_update, text="Update", command=self.update_user
        )
        self.update_button.pack(padx=10)
        self.update_button.place(x=320, y=370)

        self.delete_button = tk.Button(
            self.frame_update, text="Delete", command=self.delete_user
        )
        self.delete_button.pack(padx=10)
        self.delete_button.place(x=420, y=370)

        self.boton_principal_back_crud = ttk.Style()
        self.boton_principal_back_crud.configure(
            "Estilo.TButton",
            font=("Agency FB", 15),
            background="#4CAF50",
            foreground="Black",
        )
        self.boton_principal_back_crud = ttk.Button(
            self.frame_update,
            text="Regresar",
            style="Estilo.TButton",
            command=self.open_menu_admin,
        )
        self.boton_principal_back_crud.pack(pady=20)
        self.boton_principal_back_crud.place(x=350, y=500)

    def update_user_1(self):
        # self.frame_update.destroy()
        self.frame_update.destroy()
        self.frame_update_window.destroy()
        # self.frame_update.grid_forget()  # Esto oculta el frame anterior
        self.root.title("Update")
        self.root.geometry("790x580")
        self.root.resizable(False, False)

        self.frame_update_window = tk.Frame(
            self.root,
            highlightbackground="#66CDAA",
            highlightcolor="#66CDAA",
            highlightthickness=5,
        )
        self.frame_update_window.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        image_crud = Image.open("img/background_crud.jpg")
        self.background_image_crud = ImageTk.PhotoImage(image_crud)
        self.background_label_crud = tk.Label(
            self.frame_update_window, image=self.background_image_crud
        )
        self.background_label_crud.place(x=0, y=0, relwidth=1, relheight=1)

        self.boton_principal_back_update = ttk.Style()
        self.boton_principal_back_update.configure(
            "Estilo.TButton",
            font=("Agency FB", 15),
            background="#4CAF50",
            foreground="Black",
        )
        self.boton_principal_back_update = ttk.Button(
            self.frame_update_window,
            text="Regresar",
            style="Estilo.TButton",
            command=self.open_menu_admin,
        )
        self.boton_principal_back_update.pack(pady=20)
        self.boton_principal_back_update.place(x=350, y=500)

        # Obtener el índice del usuario seleccionado en el ComboBox
        # selected_index = self.user_combobox.current()

        # if selected_index >= 0:
        # Obtener el usuario correspondiente al índice seleccionado
        # selected_user = self.users_data[selected_index]
        # print(f"Update user with ID: {selected_user[0]}")

    def update_user_1(self):
        # create top level window
        window_update = tk.Toplevel(self.root)
        window_update.title("Update")
        window_update.geometry("790x580")
        window_update.resizable(False, False)

        self.frame_update_window = tk.Frame(
            window_update,
            highlightbackground="#66CDAA",
            highlightcolor="#66CDAA",
            highlightthickness=5,
        )
        self.frame_update_window.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        admin = Admin()
        user = self.user_combobox.get()
        user = user.split(":")
        user_id = user[0]
        user = admin.get_user(user_id)
        # print(user)
        # print(user[-1])

        # set the labels
        labels = ["id", "name", "surname", "num_cuenta", "num_placa"]
        for label in labels:
            tk.Label(self.frame_update_window, text=label).pack()
            entry_new = tk.Entry(self.frame_update_window)
            entry_new.insert(0, str(user[labels.index(label)]))
            entry_new.pack()

        # set the button
        self.boton_principal_back_update = ttk.Style()
        self.boton_principal_back_update.configure(
            "Estilo.TButton",
            font=("Agency FB", 15),
            background="#4CAF50",
            foreground="Black",
        )
        self.boton_principal_back_update = ttk.Button(
            self.frame_update_window,
            text="Update",
            style="Estilo.TButton",
            # command=,
        )
        self.boton_principal_back_update.pack(pady=20)
        self.boton_principal_back_update.place(x=350, y=500)

        # print new entry values
        # print(entry_new.get())

    def update_user(self):
        # create top level window
        window_update = tk.Toplevel(self.root)
        window_update.title("Update")
        window_update.geometry("790x580")
        window_update.resizable(False, False)

        self.frame_update_window = tk.Frame(
            window_update,
            highlightbackground="#66CDAA",
            highlightcolor="#66CDAA",
            highlightthickness=5,
        )
        self.frame_update_window.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        admin = Admin()
        user = self.user_combobox.get()
        user = user.split(":")
        user_id = user[0]
        user = admin.get_user(user_id)

        # Diccionario para almacenar los nuevos datos ingresados
        new_data = {}

        # Función para manejar el evento del botón de actualización
        def update_data():
            for label in labels:
                new_data[label] = entry_vars[label].get()
                # print(new_data[label])
                list_data = tuple(new_data.values())
            print(
                list_data
            )  # lista que se mandara al metodo update_user de la clase Admin para actualizar los datos del usuario

            # Cierra la ventana después de actualizar
            window_update.destroy()

        # set the labels
        labels = ["id", "name", "surname", "num_cuenta", "num_placa"]

        # Diccionario para almacenar las variables de las Entry widgets
        entry_vars = {}

        for label in labels:
            tk.Label(self.frame_update_window, text=label).pack()
            entry_var = tk.StringVar()
            entry_var.set(str(user[labels.index(label)]))
            entry_vars[label] = entry_var
            entry_new = tk.Entry(self.frame_update_window, textvariable=entry_var)
            entry_new.pack()

        # set the button
        self.boton_principal_back_update = ttk.Style()
        self.boton_principal_back_update.configure(
            "Estilo.TButton",
            font=("Agency FB", 15),
            background="#4CAF50",
            foreground="Black",
        )
        self.boton_principal_back_update = ttk.Button(
            self.frame_update_window,
            text="Update",
            style="Estilo.TButton",
            command=update_data,  # Asigna la función de actualización al botón
        )
        self.boton_principal_back_update.pack(pady=20)
        self.boton_principal_back_update.place(x=350, y=500)

        # print(new_data)
        # print(entry_vars)

    def delete_user(self):
        admin = Admin()

        id_ = self.user_combobox.get()
        user = id_[0]

        admin.drop_user(user)

        self.boton_principal_back_delete = ttk.Style()
        self.boton_principal_back_delete.configure(
            "Estilo.TButton",
            font=("Agency FB", 15),
            background="#4CAF50",
            foreground="Black",
        )
        self.boton_principal_back_delete = ttk.Button(
            self.frame_update,
            text="Regresar",
            style="Estilo.TButton",
            command=self.open_menu_admin,
        )
        self.boton_principal_back_delete.pack(pady=20)
        self.boton_principal_back_delete.place(x=350, y=500)

        self.frame_update.destroy()
        self.crud()

    def open_window_user(self):
        window_user = tk.Toplevel(self.root)
        window_user.title("Ventana Secundaria")
        window_user.geometry("790x580")
        window_user.resizable(False, False)

        frame_user = tk.Frame(
            window_user,
            highlightbackground="#66CDAA",
            highlightcolor="#66CDAA",
            highlightthickness=5,
        )
        frame_user.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        self.label_title = tk.Label(
            frame_user,
            text="Sing in",
            font=("Agency FB", 30),
            bg="#66CDAA",
            fg="white",
        )
        self.label_title.pack(pady=20)

        label_finger_scan = tk.Label(
            frame_user,
            text="Presione el detector de huella",
            font=("Agency FB", 15),
            bg="#66CDAA",
            fg="white",
        )
        label_finger_scan.pack(pady=20)
        label_finger_scan.place(x=305, y=450)

        # create a label with a image huella
        image_finger = Image.open("img/huella_3.png")
        # change the zoom of the image
        image_finger = image_finger.resize((200, 200), Image.LANCZOS)
        # set the image to be used
        self.huella_image_1 = ImageTk.PhotoImage(image_finger)
        # display image without label
        self.huella_label_1 = tk.Label(window_user, image=self.huella_image, bg=None)
        self.huella_label_1.place(x=300, y=200)

        print("abrir ventana user")

    def open_window_guest(self):
        window_guest = tk.Toplevel(self.root)
        window_guest.title("Ventana Secundaria")
        window_guest.geometry("550x580")
        window_guest.resizable(False, False)

        header_title = tk.Frame(
            window_guest,
        )
        header_title.pack(expand=False, fill=tk.BOTH, side=tk.TOP)

        data_parking = tk.Frame(
            window_guest,
        )
        data_parking.pack(expand=False, fill=tk.BOTH, side=tk.TOP)

        key_parking = tk.Frame(
            window_guest,
        )
        key_parking.pack(expand=False, fill=tk.BOTH, side=tk.TOP)

        image = Image.open("img/logo_car_1.png")
        image = image.resize((120, 120), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        etiqueta_imagen = tk.Label(header_title, image=image)
        etiqueta_imagen.image = image
        etiqueta_imagen.pack(side=tk.LEFT, padx=10, pady=10)

        self.label_title = tk.Label(
            header_title,
            text="Parking System UAEMEX",
            font=("Agency FB", 35),
        )
        self.label_title.pack(side=tk.TOP, padx=10, pady=10)
        label_separator = tk.Label(
            header_title,
            text="_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _",
            font=("Agency FB", 15),
        )
        label_separator.pack(side=tk.BOTTOM, padx=10, pady=10)

        hour = time.strftime("%I:%M %p")
        date = time.strftime("%Y-%m-%d")

        self.label_title = tk.Label(
            data_parking,
            text=f"Bienvenido\n{date}",
            font=("Agency FB", 22),
        )
        self.label_title.pack(side=tk.TOP, padx=10, pady=10)

        image = Image.open("img/car.png")
        image = image.resize((100, 100), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        etiqueta_imagen = tk.Label(data_parking, image=image)
        etiqueta_imagen.image = image
        etiqueta_imagen.pack(side=tk.LEFT, padx=10, pady=10)
        etiqueta_imagen.place(x=50, y=70)

        label_time = tk.Label(
            data_parking,
            text=f"Llegada: {time.strftime('%I:%M %p')}",
            font=("Agency FB", 15),
        )
        label_time.pack(side=tk.TOP, padx=10, pady=10)

        label_separator = tk.Label(
            data_parking,
            text="_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _",
            font=("Agency FB", 15),
        )
        label_separator.pack(side=tk.BOTTOM, padx=10, pady=10)

        # generar una contraseña aleatoria
        password = Password.generar_contrasena(self)

        label_numer_client = tk.Label(
            key_parking,
            text=f"CODIGO: \n{password}",
            font=("Agency FB", 28),
        )
        label_numer_client.pack(side=tk.TOP, padx=10, pady=10)

        self.boton_cerrar = tk.Button(
            key_parking, text="Cerrar", command=window_guest.destroy
        )
        # poner el boton en la parte de abajo del frame
        self.boton_cerrar.pack(side=tk.BOTTOM, padx=0, pady=0)

        # generar un nuevo folio para guest
        guest = Guest(fecha=date, hora=hour, password=password)
        guest.save()

    def open_window_guest_exit(self, hour_in, hour_exit, semifinal_tax, folio):
        window_guest_exit = tk.Toplevel(self.root)
        window_guest_exit.title("window_guest_exit")
        window_guest_exit.geometry("550x580")
        window_guest_exit.resizable(False, False)

        header_title = tk.Frame(
            window_guest_exit,
        )
        header_title.pack(expand=False, fill=tk.BOTH, side=tk.TOP)

        data_parking = tk.Frame(
            window_guest_exit,
        )
        data_parking.pack(expand=False, fill=tk.BOTH, side=tk.TOP)

        key_parking = tk.Frame(
            window_guest_exit,
        )
        key_parking.pack(expand=False, fill=tk.BOTH, side=tk.TOP)

        # agregr una imagen en la parte izquierda del header title frame
        image = Image.open("img/logo_car_1.png")
        image = image.resize((120, 120), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        etiqueta_imagen = tk.Label(header_title, image=image)
        etiqueta_imagen.image = image
        etiqueta_imagen.pack(side=tk.LEFT, padx=10, pady=10)

        # agregar un label en la parte derecha del header title frame
        self.label_title = tk.Label(
            header_title,
            text="Parking System UAEMEX",
            font=("Agency FB", 35),
        )
        self.label_title.pack(side=tk.TOP, padx=10, pady=10)
        label_separator = tk.Label(
            header_title,
            text="_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _",
            font=("Agency FB", 15),
        )
        label_separator.pack(side=tk.BOTTOM, padx=10, pady=10)

        date = time.strftime("%Y-%m-%d")

        # agregar un label en la parte de arriba de data parking frame
        self.label_title = tk.Label(
            data_parking,
            text=f"Vuelva Pronto\n{date}",
            font=("Agency FB", 22),
        )
        self.label_title.pack(side=tk.TOP, padx=10, pady=10)

        # agregar una imagen a la izquierda de data parking frame
        image = Image.open("img/car.png")
        image = image.resize((100, 100), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        etiqueta_imagen = tk.Label(data_parking, image=image)
        etiqueta_imagen.image = image
        etiqueta_imagen.pack(side=tk.LEFT, padx=10, pady=10)
        # position of the image
        etiqueta_imagen.place(x=50, y=70)

        image_ = Image.open("img/car.png")
        image_ = image_.resize((100, 100), Image.LANCZOS)
        image_ = ImageTk.PhotoImage(image_)
        etiqueta_imagen_ = tk.Label(data_parking, image=image_)
        etiqueta_imagen_.image = image_
        etiqueta_imagen_.pack(side=tk.RIGHT, padx=10, pady=10)
        # position of the image
        etiqueta_imagen_.place(x=380, y=120)

        label_time = tk.Label(
            data_parking,
            text=f"Llegada: {hour_in}",
            font=("Agency FB", 15),
        )
        label_time.pack(side=tk.TOP, padx=10, pady=10)

        label_time_exit = tk.Label(
            data_parking,
            text=f"Salida: {hour_exit}",
            font=("Agency FB", 15),
        )
        label_time_exit.pack(side=tk.TOP, padx=10, pady=10)

        label_separator = tk.Label(
            data_parking,
            text="_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _",
            font=("Agency FB", 15),
        )
        label_separator.pack(side=tk.BOTTOM, padx=10, pady=10)

        label_numer_client = tk.Label(
            key_parking,
            text=f"Folio: {folio}\nTotal a pagar:\n {semifinal_tax}",
            font=("Agency FB", 28),
        )
        label_numer_client.pack(side=tk.TOP, padx=10, pady=10)

        self.boton_cerrar = tk.Button(
            key_parking, text="Cerrar", command=window_guest_exit.destroy
        )
        self.boton_cerrar.pack(side=tk.BOTTOM, padx=0, pady=0)

    def reg_exit_guest(self):
        toplevel = tk.Toplevel(self.root)
        toplevel.title("Input Box")
        toplevel.geometry("250x150")
        toplevel.resizable(False, False)

        self.label_title = tk.Label(
            toplevel,
            text="Ingrese el Codigo de salida",
            font=("Agency FB", 15),
            bg="#66CDAA",
            fg="white",
        )
        self.label_title.pack(pady=0)
        self.entry_pass = tk.Entry(
            toplevel,
        )
        self.entry_pass.pack(pady=10)

        self.button_pass = tk.Button(
            toplevel,
            text="Entrar",
            command=lambda: self.check_password_exit(self.entry_pass.get(), toplevel),
        )
        self.button_pass.pack()

    # def check_tax_price(self, hour_in, hour_exit):
    #     try:
    #         # Convertir a cadena de texto antes de usar strptime
    #         time_in = datetime.datetime.strptime(hour_in, "%H:%M:%S")
    #         time_exit = datetime.datetime.strptime(hour_exit, "%H:%M:%S")
    #         time_parked = time_exit - time_in

    #         # Calcular el precio a pagar
    #         if time_parked > datetime.timedelta(hours=1):
    #             price = 15.0
    #         else:
    #             # Precio base si el tiempo es menor o igual a una hora
    #             price = 5.0

    #         # Mostrar el precio a pagar
    #         print(price)
    #         return price

    #     except ValueError as e:
    #         # Manejar errores de formato de hora
    #         print(f"Error al analizar las horas: {e}")
    #         return None

    def check_password_exit(self, input_text, toplevel):
        guest = Guest().get_guest(input_text)

        if guest and input_text == str(guest[3]):
            folio = guest[0]
            new_hour = time.strftime("%H:%M:%S")
            # print(new_hour)
            new_tax = 10.0
            # new_tax_1 = self.check_tax_price(guest[2], new_hour)
            # print(guest[2])
            # print(new_tax_1)

            guest_exit = Guest().update_guest(
                new_hour,
                new_tax,
                input_text,
            )
            hour_in = guest_exit[2]
            hour_exit = guest_exit[4]
            semifinal_tax = guest_exit[5]
            self.open_window_guest_exit(hour_in, hour_exit, semifinal_tax, folio)
            toplevel.destroy()
        else:
            popup = tk.Toplevel(self.root)
            popup.title("Error")
            popup.geometry("250x100")
            popup.resizable(False, False)
            popup.configure(bg="cyan")
            etiqueta_popup = tk.Label(
                popup,
                text="Codigo Incorrecto.",
                fg="black",
                bg="cyan",
            )
            etiqueta_popup.pack(padx=20, pady=10)

    def recopilar_texto(self):
        texto_nombre = self.textbox_nombre.get()
        texto_apellido = self.textbox_apellido.get()
        texto_num_cuenta = self.textbox_numero_cuenta.get()
        texto_num_placa = self.textbox_numero_placa.get()

        if (
            texto_nombre == ""
            or texto_apellido == ""
            or texto_num_cuenta == ""
            or texto_num_placa == ""
        ):
            popup = tk.Toplevel(self.root)
            popup.title("Error")
            popup.geometry("250x100")
            popup.resizable(False, False)
            popup.configure(bg="cyan")
            etiqueta_popup = tk.Label(
                popup,
                text="Debe llenar todos los campos \npara registrarse.",
                fg="black",
                bg="cyan",
            )
            etiqueta_popup.pack(padx=20, pady=10)
            self.boton_cerrar = tk.Button(popup, text="Cerrar", command=popup.destroy)
            self.boton_cerrar.pack(pady=10)
        else:
            popup = tk.Toplevel(self.root)
            popup.title("Usuario registrado")
            popup.geometry("200x200")
            popup.resizable(False, False)
            etiqueta_popup = tk.Label(
                popup, text=f"¡Hola! {texto_nombre}, tu lugar te espera 😊."
            )
            etiqueta_popup.pack(padx=20, pady=10)
            self.boton_cerrar = tk.Button(popup, text="Cerrar", command=popup.destroy)
            self.boton_cerrar.pack(pady=10)

        persona = Person(
            texto_nombre, texto_apellido, texto_num_cuenta, texto_num_placa
        )
        persona.save()


if __name__ == "__main__":
    root = tk.Tk()
    app = Windows(root)
    root.mainloop()
