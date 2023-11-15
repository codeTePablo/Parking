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

        title_label = tk.Label(
            self.root,
            text="Bienvenido",
            font=("Agency FB", 40),
            bg="#EEC591",
            fg="white",
        )
        title_label.place(x=340, y=140)

        title_label_login = tk.Label(
            self.root,
            text="Login as ",
            font=("Agency FB", 15),
            bg="#EEC591",
            fg="white",
        )
        title_label_login.place(x=590, y=180)

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
        self.boton_principal_guest_exit.place(x=370, y=450)

    def admin_window(self):
        toplevel = tk.Toplevel(self.root)
        toplevel.title("Input Box")
        toplevel.geometry("250x150")
        toplevel.resizable(False, False)

        show_password_var = tk.BooleanVar()
        show_password_var.set(False)

        # generar un label con texto
        label_title = tk.Label(
            toplevel,
            text="Ingrese la contraseña",
            font=("Agency FB", 15),
            bg="#66CDAA",
            fg="white",
        )
        label_title.pack(pady=0)

        # Crear el cuadro de entrada en el Toplevel
        entry = tk.Entry(
            toplevel,
            show="*",
        )
        entry.pack(pady=10)

        # agregar un checkbox para pocer ver la contraseña
        checkbutton = tk.Checkbutton(
            toplevel,
            text="Mostrar Contraseña",
            variable=show_password_var,
            command=lambda: self.toggle_show_password(entry, show_password_var),
        )
        checkbutton.pack()

        # Crear el botón en el Toplevel
        button = tk.Button(
            toplevel,
            text="Entrar",
            command=lambda: self.check_password(entry.get(), toplevel),
        )
        button.pack()

    def toggle_show_password(self, entry, show_password_var):
        # Mostrar u ocultar la contraseña según el estado del Checkbutton
        show_password = show_password_var.get()
        if show_password:
            entry.config(show="")
        else:
            entry.config(show="*")

    def check_password(self, input_text, toplevel):
        password = "1234"
        if input_text == password:
            # print("contraseña correcta")
            self.abrir_ventana_login()
            toplevel.destroy()
        else:
            popup = tk.Toplevel(self.root)
            popup.title("Error")
            label_error = tk.Label(
                popup,
                text="Contraseña incorrecta",
                fg="black",
                bg="cyan",
            )
            label_error.pack(padx=20, pady=10)

    def abrir_ventana_login(self):
        ventana_secundaria = tk.Toplevel(self.root)
        ventana_secundaria.title("Ventana Secundaria")
        ventana_secundaria.geometry("790x580")
        ventana_secundaria.resizable(False, False)

        frame1 = tk.Frame(
            ventana_secundaria,
            highlightbackground="#66CDAA",
            highlightcolor="#66CDAA",
            highlightthickness=5,
        )
        frame1.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        label_verde = tk.Label(frame1, text="", bg="#66CDAA")
        label_verde.pack(expand=True, fill=tk.BOTH)

        # crear un label dentro del frame1 con el texto "Registro"
        label_registro = tk.Label(
            label_verde,
            text="Nuevo usuario",
            font=("Agency FB", 27),
            bg="#66CDAA",
            fg="white",
        )
        label_registro.pack(pady=0)
        label_registro.place(x=15, y=50)

        label_registro_nombre = tk.Label(
            label_verde,
            text="Nombre",
            font=("Agency FB", 13),
            bg="#66CDAA",
            fg="white",
        )
        label_registro_nombre.pack(pady=0)
        label_registro_nombre.place(x=50, y=120)

        self.textbox_nombre = tk.Entry(label_verde)
        self.textbox_nombre.pack(padx=5)
        self.textbox_nombre.place(x=50, y=150)

        label_registro_apellido = tk.Label(
            label_verde,
            text="Apellido",
            font=("Agency FB", 13),
            bg="#66CDAA",
            fg="white",
        )
        label_registro_apellido.pack(pady=0)
        label_registro_apellido.place(x=50, y=170)

        self.textbox_apellido = tk.Entry(label_verde)
        self.textbox_apellido.pack(padx=5)
        self.textbox_apellido.place(x=50, y=195)

        label_registro_numero_cuenta = tk.Label(
            label_verde,
            text="Numero de cuenta",
            font=("Agency FB", 13),
            bg="#66CDAA",
            fg="white",
        )
        label_registro_numero_cuenta.pack(pady=0)
        label_registro_numero_cuenta.place(x=50, y=220)

        self.textbox_numero_cuenta = tk.Entry(label_verde)
        self.textbox_numero_cuenta.pack(padx=5)
        self.textbox_numero_cuenta.place(x=50, y=245)

        label_registro_numero_placa = tk.Label(
            label_verde,
            text="Numero de placa",
            font=("Agency FB", 13),
            bg="#66CDAA",
            fg="white",
        )
        label_registro_numero_placa.pack(pady=0)
        label_registro_numero_placa.place(x=50, y=270)

        self.textbox_numero_placa = tk.Entry(label_verde)
        self.textbox_numero_placa.pack(padx=0)
        self.textbox_numero_placa.place(x=50, y=295)

        boton_escanear = tk.Button(
            label_verde,
            text="Escanear huella",
            # command=self.escanear_huella_arduino
        )
        boton_escanear.pack(side=tk.BOTTOM)
        boton_escanear.place(x=60, y=340)

        boton_recopilar = tk.Button(
            label_verde, text="Registrar", command=self.recopilar_texto
        )
        boton_recopilar.pack(side=tk.BOTTOM)
        boton_recopilar.place(x=65, y=480)

        boton_cerrar = tk.Button(
            ventana_secundaria, text="Cerrar", command=ventana_secundaria.destroy
        )
        boton_cerrar.pack(side=tk.BOTTOM)
        boton_cerrar.place(x=75, y=540)

        frame2 = tk.Frame(ventana_secundaria)
        frame2.pack(pady=5, side=tk.RIGHT)

        # set into frame2 the image of the fingerprint
        image = Image.open("img/background_login.jpg")
        image = image.resize((580, 600), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        etiqueta_imagen_huella = tk.Label(frame2, image=image)
        etiqueta_imagen_huella.image = image
        etiqueta_imagen_huella.pack()

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

        label_title = tk.Label(
            frame_user,
            text="Sing in",
            font=("Agency FB", 30),
            bg="#66CDAA",
            fg="white",
        )
        label_title.pack(pady=20)

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

        # ///////////////////////////////

        # mandar a ejecutar el programa del esp32 para que escanee la huella y coopie el dato en la variable
        # finger = "123456789"
        # si la huella coincide con la de la base de datos, entonces se debe mostrar un popup con el mensaje de que el usuario se registro correctamente
        # Crear una nueva ventana (popup)
        # popup = tk.Toplevel(self.root)
        # popup.title("Usuario registrado")

        # ademas si la hella coincide se debe de destruir la ventana de login y regresar a la ventana principal
        # self.root.destroy()

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

        label_title = tk.Label(
            header_title,
            text="Parking System UAEMEX",
            font=("Agency FB", 35),
        )
        label_title.pack(side=tk.TOP, padx=10, pady=10)
        label_separator = tk.Label(
            header_title,
            text="_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _",
            font=("Agency FB", 15),
        )
        label_separator.pack(side=tk.BOTTOM, padx=10, pady=10)

        hour = time.strftime("%I:%M %p")
        date = time.strftime("%Y-%m-%d")

        label_title = tk.Label(
            data_parking,
            text=f"Bienvenido\n{date}",
            font=("Agency FB", 22),
        )
        label_title.pack(side=tk.TOP, padx=10, pady=10)

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

        boton_cerrar = tk.Button(
            key_parking, text="Cerrar", command=window_guest.destroy
        )
        # poner el boton en la parte de abajo del frame
        boton_cerrar.pack(side=tk.BOTTOM, padx=0, pady=0)

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
        label_title = tk.Label(
            header_title,
            text="Parking System UAEMEX",
            font=("Agency FB", 35),
        )
        label_title.pack(side=tk.TOP, padx=10, pady=10)
        label_separator = tk.Label(
            header_title,
            text="_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _",
            font=("Agency FB", 15),
        )
        label_separator.pack(side=tk.BOTTOM, padx=10, pady=10)

        date = time.strftime("%Y-%m-%d")

        # agregar un label en la parte de arriba de data parking frame
        label_title = tk.Label(
            data_parking,
            text=f"Vuelva Pronto\n{date}",
            font=("Agency FB", 22),
        )
        label_title.pack(side=tk.TOP, padx=10, pady=10)

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

        boton_cerrar = tk.Button(
            key_parking, text="Cerrar", command=window_guest_exit.destroy
        )
        boton_cerrar.pack(side=tk.BOTTOM, padx=0, pady=0)

    def reg_exit_guest(self):
        toplevel = tk.Toplevel(self.root)
        toplevel.title("Input Box")
        toplevel.geometry("250x150")
        toplevel.resizable(False, False)

        label_title = tk.Label(
            toplevel,
            text="Ingrese el Codigo de salida",
            font=("Agency FB", 15),
            bg="#66CDAA",
            fg="white",
        )
        label_title.pack(pady=0)
        entry_pass = tk.Entry(
            toplevel,
        )
        entry_pass.pack(pady=10)

        button_pass = tk.Button(
            toplevel,
            text="Entrar",
            command=lambda: self.check_password_exit(entry_pass.get(), toplevel),
        )
        button_pass.pack()

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
        # Obtener el texto del Entry
        texto_nombre = self.textbox_nombre.get()
        texto_apellido = self.textbox_apellido.get()
        texto_num_cuenta = self.textbox_numero_cuenta.get()
        texto_num_placa = self.textbox_numero_placa.get()

        # si alguno de los cambios es vacio, mostrar un popup con el mensaje de que debe llenar todos los campos
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
            boton_cerrar = tk.Button(popup, text="Cerrar", command=popup.destroy)
            boton_cerrar.pack(pady=10)
        else:
            popup = tk.Toplevel(self.root)
            popup.title("Usuario registrado")
            popup.geometry("200x200")
            popup.resizable(False, False)
            etiqueta_popup = tk.Label(
                popup, text=f"¡Hola! {texto_nombre}, tu lugar te espera 😊."
            )
            etiqueta_popup.pack(padx=20, pady=10)
            boton_cerrar = tk.Button(popup, text="Cerrar", command=popup.destroy)
            boton_cerrar.pack(pady=10)

        # Crear un objeto de tipo People
        persona = Person(
            texto_nombre, texto_apellido, texto_num_cuenta, texto_num_placa
        )
        persona.save()

    # def escanear_huella_arduino(self):
    #     # Enviar comando al Arduino para iniciar el escaneo
    #     try:
    #         # Configura el puerto serie (ajusta el nombre del puerto según tu sistema)
    #         ser = serial.Serial("COM3", 9600, timeout=1)

    #         # Envía el comando al Arduino
    #         ser.write(b"StartScan\n")

    #         # Espera la respuesta del Arduino (ajusta según tu necesidad)
    #         time.sleep(2)

    #         # Lee la respuesta del Arduino
    #         respuesta = ser.readline().decode("utf-8")

    #         # Actúa en consecuencia
    #         if "HuellaEscaneada" in respuesta:
    #             print("Huella escaneada con éxito")
    #             # Puedes realizar otras acciones aquí
    #         else:
    #             print("Error al escanear la huella")
    #     except Exception as e:
    #         print(f"Error de comunicación con Arduino: {e}")
    #     finally:
    #         # Cierra el puerto serie
    #         ser.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = Windows(root)
    root.mainloop()
