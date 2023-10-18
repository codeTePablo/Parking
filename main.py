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

# database
from db import get_connection
import db


class Windows:
    def __init__(self, root):
        self.root = root
        self.root.title("Programa con Tkinter")

        self.root.geometry("790x580")
        # set the window to not be resizable
        self.root.resizable(False, False)

        # set background image of the window
        image = Image.open("img/background.jpg")
        self.background_image = ImageTk.PhotoImage(image)
        # Crear el label de fondo con la imagen
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # create a label with a image huella
        image = Image.open("img/huella_3.png")
        # change the zoom of the image
        image = image.resize((200, 200), Image.LANCZOS)
        # set the image to be used
        self.huella_image = ImageTk.PhotoImage(image)
        # display image without label
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
            text="Registrarse",
            style="Estilo.TButton",
            command=self.abrir_ventana_login,
        )
        self.boton_principal_login.pack(pady=20)
        self.boton_principal_login.place(x=370, y=450)

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
            text="invitado",
            style="Estilo.TButton",
            command=self.open_window_guest,
        )
        self.boton_principal_guest.pack(pady=20)
        self.boton_principal_guest.place(x=570, y=300)

    def abrir_ventana_login(self):
        # Crear una nueva ventana
        ventana_secundaria = tk.Toplevel(self.root)
        ventana_secundaria.title("Ventana Secundaria")

        # set the size of the window
        ventana_secundaria.geometry("790x580")
        # set the window to not be resizable
        ventana_secundaria.resizable(False, False)

        frame1 = tk.Frame(
            ventana_secundaria,
            highlightbackground="#66CDAA",
            highlightcolor="#66CDAA",
            highlightthickness=5,
        )
        frame1.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        # Agregar un Label con color verde en el primer Frame
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

        # Agregar un Entry (cuadro de texto) y un botón dentro del Label, ponerle texto al textbox
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
            label_verde, text="Escanear huella", command=self.escanear_huella_arduino
        )
        boton_escanear.pack(side=tk.BOTTOM)
        boton_escanear.place(x=60, y=340)

        boton_recopilar = tk.Button(
            label_verde, text="Registrar", command=self.recopilar_texto
        )
        boton_recopilar.pack(side=tk.BOTTOM)
        boton_recopilar.place(x=65, y=480)

        # Agregar un botón para cerrar la ventana
        boton_cerrar = tk.Button(
            ventana_secundaria, text="Cerrar", command=ventana_secundaria.destroy
        )
        boton_cerrar.pack(side=tk.BOTTOM)
        boton_cerrar.place(x=75, y=540)
        ###
        # Crear el segundo Frame (puedes personalizar según tus necesidades)
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
        # Crear una nueva ventana
        window_user = tk.Toplevel(self.root)
        window_user.title("Ventana Secundaria")

        # set the size of the window
        window_user.geometry("790x580")
        # set the window to not be resizable
        window_user.resizable(False, False)

        frame_user = tk.Frame(
            window_user,
            highlightbackground="#66CDAA",
            highlightcolor="#66CDAA",
            highlightthickness=5,
        )
        frame_user.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        # crear un label dentro del frame1 con el texto "Registro"
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
        # Crear una nueva ventana
        window_guest = tk.Toplevel(self.root)
        window_guest.title("Ventana Secundaria")

        # set the size of the window
        window_guest.geometry("790x580")
        # set the window to not be resizable
        window_guest.resizable(False, False)

        frame_guest = tk.Frame(
            window_guest,
            highlightbackground="#66CDAA",
            highlightcolor="#66CDAA",
            highlightthickness=5,
        )
        frame_guest.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        # crear un label dentro del frame1 con el texto "Registro"
        label_registro = tk.Label(
            frame_guest,
            text="Nuevo invitado",
            font=("Agency FB", 25),
            bg="#66CDAA",
            fg="white",
        )
        label_registro.pack(pady=20)

        # create a label with a image huella
        image_finger_guest = Image.open("img/huella_3.png")
        # change the zoom of the image
        image_finger_guest = image_finger_guest.resize((200, 200), Image.LANCZOS)
        # set the image to be used
        self.huella_image_2 = ImageTk.PhotoImage(image_finger_guest)
        # display image without label
        self.huella_label_2 = tk.Label(window_guest, image=self.huella_image, bg=None)
        self.huella_label_2.place(x=300, y=200)

        # ///////////////////////////////
        time = datetime.datetime.now()
        hour = time.strftime("%I:%M %p")
        date = time.strftime("%Y-%m-%d")
        print(date)
        print(hour)
        print(time)
        print("abrir ventana guest")

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
            # Crear una nueva ventana (popup)
            popup = tk.Toplevel(self.root)
            popup.title("Error")

            # set the size of the window
            popup.geometry("250x100")
            # set the window to not be resizable
            popup.resizable(False, False)

            # color de fondo
            popup.configure(bg="cyan")

            # Agregar contenido al popup
            etiqueta_popup = tk.Label(
                popup,
                text="Debe llenar todos los campos \npara registrarse.",
                fg="black",
                bg="cyan",
            )
            etiqueta_popup.pack(padx=20, pady=10)

            # Agregar un botón para cerrar el popup
            boton_cerrar = tk.Button(popup, text="Cerrar", command=popup.destroy)
            boton_cerrar.pack(pady=10)
        else:
            # al accionar el boton de recopilar se debe mostrar un popup con el mensaje de que el usuario se registro correctamente
            # Crear una nueva ventana (popup)
            popup = tk.Toplevel(self.root)
            popup.title("Usuario registrado")

            # set the size of the window
            popup.geometry("200x200")
            # set the window to not be resizable
            popup.resizable(False, False)

            # Agregar contenido al popup
            etiqueta_popup = tk.Label(
                popup, text=f"¡Hola! {texto_nombre}, tu lugar te espera 😊."
            )
            etiqueta_popup.pack(padx=20, pady=10)

            # Agregar un botón para cerrar el popup
            boton_cerrar = tk.Button(popup, text="Cerrar", command=popup.destroy)
            boton_cerrar.pack(pady=10)

        # Crear un objeto de tipo People
        persona = Person(
            texto_nombre, texto_apellido, texto_num_cuenta, texto_num_placa
        )
        persona.save()

    def escanear_huella_arduino(self):
        # Enviar comando al Arduino para iniciar el escaneo
        try:
            # Configura el puerto serie (ajusta el nombre del puerto según tu sistema)
            ser = serial.Serial("COM3", 9600, timeout=1)

            # Envía el comando al Arduino
            ser.write(b"StartScan\n")

            # Espera la respuesta del Arduino (ajusta según tu necesidad)
            time.sleep(2)

            # Lee la respuesta del Arduino
            respuesta = ser.readline().decode("utf-8")

            # Actúa en consecuencia
            if "HuellaEscaneada" in respuesta:
                print("Huella escaneada con éxito")
                # Puedes realizar otras acciones aquí
            else:
                print("Error al escanear la huella")
        except Exception as e:
            print(f"Error de comunicación con Arduino: {e}")
        finally:
            # Cierra el puerto serie
            ser.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = Windows(root)
    # app.calcular_hora_de_salida()
    # with get_connection() as connection:
    # db.create_tables(connection)
    root.mainloop()
