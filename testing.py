import tkinter as tk
from PIL import Image, ImageTk
import serial
import time
from datetime import datetime


class MiPrograma:
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
            self.root, text="Bienvenido", font=("Arial", 30), bg="white"
        )
        title_label.place(x=300, y=140)

        # Crear el botón en la pantalla principal
        self.boton_principal = tk.Button(
            root, text="Registrarse", command=self.abrir_ventana
        )
        self.boton_principal.pack(pady=20)
        self.boton_principal.place(x=350, y=450)

    def abrir_ventana(self):
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
            font=("Arial", 20),
            bg="#66CDAA",
            fg="white",
        )
        label_registro.pack(pady=20)
        label_registro.place(x=15, y=50)

        label_registro_nombre = tk.Label(
            label_verde,
            text="Nombre",
            font=("Arial", 10),
            bg="#66CDAA",
            fg="white",
        )
        label_registro_nombre.pack(pady=20)
        label_registro_nombre.place(x=50, y=130)

        # Agregar un Entry (cuadro de texto) y un botón dentro del Label, ponerle texto al textbox
        self.textbox_nombre = tk.Entry(label_verde)
        self.textbox_nombre.pack(padx=5)
        self.textbox_nombre.place(x=50, y=150)

        label_registro_apellido = tk.Label(
            label_verde,
            text="Apellido",
            font=("Arial", 10),
            bg="#66CDAA",
            fg="white",
        )
        label_registro_apellido.pack(pady=20)
        label_registro_apellido.place(x=50, y=170)

        self.textbox_apellido = tk.Entry(label_verde)
        self.textbox_apellido.pack(padx=5)
        self.textbox_apellido.place(x=50, y=190)

        label_registro_numero_cuenta = tk.Label(
            label_verde,
            text="Numero de cuenta",
            font=("Arial", 10),
            bg="#66CDAA",
            fg="white",
        )
        label_registro_numero_cuenta.pack(pady=20)
        label_registro_numero_cuenta.place(x=50, y=210)

        self.textbox_numero_cuenta = tk.Entry(label_verde)
        self.textbox_numero_cuenta.pack(padx=5)
        self.textbox_numero_cuenta.place(x=50, y=230)

        label_registro_numero_placa = tk.Label(
            label_verde,
            text="Numero de placa",
            font=("Arial", 10),
            bg="#66CDAA",
            fg="white",
        )
        label_registro_numero_placa.pack(pady=20)
        label_registro_numero_placa.place(x=50, y=250)

        self.textbox_numero_placa = tk.Entry(label_verde)
        self.textbox_numero_placa.pack(padx=5)
        self.textbox_numero_placa.place(x=50, y=270)

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
            popup.geometry("200x200")
            # set the window to not be resizable
            popup.resizable(False, False)

            # Agregar contenido al popup
            etiqueta_popup = tk.Label(
                popup, text="Debe llenar todos los campos para registrarse."
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

        return texto_nombre, texto_apellido, texto_num_cuenta, texto_num_placa

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

    def calcular_hora_de_salida(self):
        # calcular la hora de entrada
        hora_entrada = datetime.now().strftime("%I:%M %p")
        # calcular la hora de salida
        # hora_salida = datetime.now().strftime("%I:%M %p")
        # calcular la fecha
        fecha = datetime.now().strftime("%Y-%m-%d")
        # calcular el tiempo de estadia
        # tiempo_de_estadia = hora_salida - hora_entrada
        # calcular el tiempo de estadia en horas
        # tiempo_de_estadia_en_horas = tiempo_de_estadia.total_seconds() / 3600.0
        print(hora_entrada)
        print(fecha)


if __name__ == "__main__":
    root = tk.Tk()
    app = MiPrograma(root)
    app.calcular_hora_de_salida()
    root.mainloop()
