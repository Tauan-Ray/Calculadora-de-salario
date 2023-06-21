from tkinter import *
from PIL import Image, ImageTk

# Cores
white = '#FFFFFF'
gray = '#919191'
font = '#3e4146'

# Configurando janela
app = Tk()
app.title('Calculadora de Salário')
app.geometry('550x350')
app.config(bg=white)
app.resizable(False, False)

# Criando cabeçalho
header = Frame(app, width=551, height=30, bg=white,
               relief='raised', borderwidth=1)
header.place(x=0, y=0)


# Fazendo header
iconHeader = Image.open('CalculadoraSalario/images/money.png')
iconHeader = iconHeader.resize((28, 28))
iconHeader = ImageTk.PhotoImage(iconHeader)

iconHead = Label(header, image=iconHeader, width=20, height=23,
                 compound=CENTER, anchor=CENTER, bg=white, relief=FLAT)
iconHead.place(x=4, y=0)

nameApp = Label(header, text='Calculadora de salário', width=20,
                height=1, anchor=CENTER, font=('Ivy 12 bold'), bg=white, fg=font)
nameApp.place(x=30, y=3)


# Criando labels e entrys
name = Label(app, text='Escreva seu nome completo: ', width=30,
             height=1, anchor='w', font=('Ivy 9 bold'), bg=white, fg=font)
name.place(x=5, y=50)

nameEntry = Entry(app, width=25, justify='left', relief='solid', borderwidth=1)
nameEntry.place(x=190, y=50)

hoursDay = Label(app, text='Quantas horas você trabalha por dia? ',
                 width=40, height=1, anchor='w', font=('Ivy 9 bold'), bg=white, fg=font)
hoursDay.place(x=5, y=85)

hoursEntry = Entry(app, width=15, justify='center',
                   relief='solid', borderwidth=1)
hoursEntry.place(x=246, y=85)

daysWeek = Label(app, text='Quantos dias você trabalha por semana? ',
                 width=40, height=1, anchor='w', font=('Ivy 9 bold'), bg=white, fg=font)
daysWeek.place(x=5, y=120)

daysEntry = Entry(app, width=15, justify='center',
                  relief='solid', borderwidth=1)
daysEntry.place(x=246, y=120)

yearSalary = Label(app, text='Qual é o seu salário anual ?', width=30,
                   height=1, anchor='w', font=('Ivy 9 bold'), bg=white, fg=font)
yearSalary.place(x=5, y=155)

yearEntry = Entry(app, width=15, justify='center',
                  relief='solid', borderwidth=1)
yearEntry.place(x=246, y=155)

# Criando função


def calc():
    # Coletando informações dos entrys
    nameGet = nameEntry.get()
    hoursGet = hoursEntry.get()
    daysGet = daysEntry.get()
    yearGet = int(yearEntry.get())

    nameShow = Label(app, text=nameGet, width=28, height=1, anchor='w', font=(
        'Ivy 10'), relief=RAISED, bg=gray, fg=font)
    nameShow.place(x=5, y=190)

    hoursShow = Label(app, text=f'Horas de trabalho por dia: {hoursGet}', width=28, height=1, anchor='w', font=(
        'Ivy 10'), relief=RAISED, bg=gray, fg=font)
    hoursShow.place(x=5, y=212)

    daysShow = Label(app, text=f'Dias de trabalho por semana: {daysGet}', width=28, height=1, anchor='w', font=(
        'Ivy 10'), relief=RAISED, bg=gray, fg=font)
    daysShow.place(x=5, y=234)

    yearShow = Label(app, text=f"R${yearGet:,.2f}", width=28, height=1, anchor='w', font=(
        'Ivy 10'), relief=RAISED, bg=gray, fg=font)
    yearShow.place(x=5, y=234)


# Colocando imagem e botãao de calcular
iconBig = Image.open('calculadoraSalario/images/money.png')
iconBig = iconBig.resize((100, 100))
iconBig = ImageTk.PhotoImage(iconBig)

img = Label(app, image=iconBig, width=114, height=100,
            compound=CENTER, anchor=CENTER, bg=white, relief=FLAT)
img.place(x=380, y=40)

calc_button = Button(app, command=calc, text='Calcular', width=17, height=1, anchor='center', font=(
    'Ivy 9 bold'), relief='raised', overrelief='sunken', bg=gray, fg=font, borderwidth=2,)
calc_button.place(x=370, y=151)

app.mainloop()
