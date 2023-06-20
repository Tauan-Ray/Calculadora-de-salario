from tkinter import *
from PIL import Image, ImageTk

# Cores
white = '#FFFFFF'
gray = '#919191'
font = '#3e4146'

# Configurando janela
app = Tk()
app.title('Calculadora de Salário')
app.geometry('500x270')
app.config(bg=white)

# Criando cabeçalho
header = Frame(app, width=501, height=30, bg=white, relief='raised', borderwidth=1)
header.place(x=0, y=0)

# Criando labels
name = Label(app, text='Escreva seu nome completo: ',width=30, height=1, anchor='w', font=('Ivy 9 bold'), bg=white, fg=font)
name.place(x=5, y=50)

nameEntry = Entry(app, width=25, justify='left', relief='solid' ,borderwidth=1)
nameEntry.place(x=175, y=50)


app.mainloop()
