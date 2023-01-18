from tkinter import *
import requests

URL = "https://cdn.discordapp.com/attachments/721617203283361806/1065297437348073624/original.gif"
response = requests.get(URL)
open("melody.ico", "wb").write(response.content)

URL_2 = "https://cdn.discordapp.com/attachments/721617203283361806/1065308182311870587/black-heart_1f5a4.gif"
response = requests.get(URL_2)
open("corazon.ico", "wb").write(response.content)

ventana = Tk()
imagen = PhotoImage(file='melody.ico')
ventana.geometry("520x480")
ventana.title("Acertijo")
ventana.config(background="black")
icono = PhotoImage(file='corazon.ico')
ventana.iconphoto(True, icono)
label = Label(ventana, text="Sharis es la niña mas linda de todas!",
              font='Wingdings',
              bg='black',
              fg='white')

mensaje = Label(ventana, text="Decifra el mensaje, buena suerte! "
                              "Pista: Sharis",

                fg='pink',
                bg='black',
                image=imagen,
                compound='bottom')

label.place(x=0, y=0)
mensaje.place(x=0, y=20)

ventana.mainloop()
