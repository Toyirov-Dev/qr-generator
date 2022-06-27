import random 
from tkinter import*
from tkinter  import messagebox
import qrcode
import random
import time


# Dastur oynasi:
qr_win = Tk()
qr_win.title("QR-maker")
qr_win.geometry('450x300')
qr_win.config(bg='#19498D')
qr_win.iconbitmap("icon/icon.ico")

text = "qwertyuioplkjhgfdsazxcvbnm"
num = "1234567890"

string = text + num
qator = 6 

malaqa = "".join(random.sample(string, qator))
ismi = malaqa + ".png"
t_ism = "fotos/"+ismi
# print(t_ism)


# Functions:
def make():
	ol = input1.get()
	yasa = qrcode.make(ol)
	yasa.save(t_ism)
	
	time.sleep(.2)
	saqlandi = Label(qr_win, text="qr saqlandi!",
		fg='red',                              
		font=("Colibri", 18, 'italic'),        
		bg='#19498D')                          
	saqlandi.place(x=160, y=240)               
	
	


def cmdExit():     
    quit()

def About():     
    label = messagebox.showinfo("About", "Dastur Toyirov Ziyodullo tomonidan\n 03.06.2202 - sanada yartildi.\n\n Dastur vazifasi: qr yasash. \n\nTelegram: @Desperados_partfolio")



# Sarlavha:
Sarlavha = Label(qr_win, text="QR-maker",
	fg='Black',
	font=('Ink Free', 20, 'bold'),
	bg='#19498D')
Sarlavha.place(x=160, y=20)

# tavsif:
tavsif = Label(qr_win, text="text kiriting:",
	fg='Black',
	font=("Colibri", 18, 'italic'),
	bg='#19498D')
tavsif.place(x=160, y=100)




# Entry
input1 = Entry(qr_win, bg='#DFDFDF',
	fg = 'black',
	font = ('Colibri', 15, 'italic'),
	relief = SOLID,
	width = 31)
input1.place(x=50, y=135)

# Tugma:
Tugma = Button(qr_win, text='Yasash',
	bg = 'black',
	fg ='white',
	width = 20,
	font = ("Ink Free", 10, 'bold'),
	relief = SOLID,
	command=make)
Tugma.place(x=140, y=180)

# Menu:

qr_Menu = Menu(qr_win)
qr_win.configure(menu=qr_Menu)


helpMenu = Menu(qr_Menu, tearoff = False)
qr_Menu.add_cascade(label='Help', menu = helpMenu)

helpMenu.add_command(label='About', command=About) 
helpMenu.add_separator()
helpMenu.add_command(label='Chiqish', command = cmdExit) 


qr_win.mainloop()