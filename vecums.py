import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
from datetime import datetime

class Person:
    def __init__(self, master):
        self.master = master
        self.master.title("Vecumu aprēķināšana")
        self.master.geometry("650x600")
        self.vards = ""
        self.gads = 0
        self.menesis = 0
        self.diena = 0

    
    def labeli(self):
        self.label1 = Label(text = "Vārds:")
        self.label1.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.label2 = Label(text = "Gads:")
        self.label2.grid(row = 3, column = 1, padx = 10, pady = 10)
        self.label3 = Label(text = "Mēnesis:")
        self.label3.grid(row = 4, column = 1, padx = 10, pady = 10)
        self.label4 = Label(text = "Diena:")
        self.label4.grid(row = 5, column = 1, padx = 10, pady = 10)
        self.teksts = Text(self.master, height = 20, width = 40)
        self.teksts.grid(row=7, column = 2, padx = 10, pady = 10)

    def entries(self):
        self.entry1 = Entry()
        self.entry1.grid(row=2, column = 2, padx = 10, pady = 10)
        self.entry2 = Entry()
        self.entry2.grid(row=3, column = 2, padx = 10, pady = 10)
        self.entry3 = Entry()
        self.entry3.grid(row=4, column = 2, padx = 10, pady = 10)
        self.entry4 = Entry()
        self.entry4.grid(row=5, column = 2, padx = 10, pady = 10)

    def getting_values(self):
        self.vards = self.entry1.get()
        self.gads = self.entry2.get()
        self.menesis = self.entry3.get()
        self.diena = self.entry3.get()
        return self.vards, self.gads, self.menesis, self.diena

    def maths(self):
        self.year = datetime.now()
        #self.year.strftime('%Y-%m-%d')
        self.current = datetime(int(self.gads), int(self.menesis), int(self.diena))
        #self.current.strftime('%Y-%m-%d')
        self.old = self.year - self.current
        self.old = int(float(self.old.days/365))
        #self.old.strftime('%Y')
        #self.old = datetime.datetime(self.year-self.current)
        #self.old = self.old.year
        return self.old


    def outputs(self):
        self.text = "Sveiki, "+ str(self.vards)+"! Jūs esat "+str(self.old)+" gadus veci."
        self.teksts.insert(tk.END, self.text)

    def buttoni(self):
        self.button = Button(text = "Aprēķināt vecumu")
        self.button.grid(row=6, column = 2, padx = 10, pady = 10)
        self.button.configure(command=lambda: [Person.getting_values(self), Person.maths(self), Person.outputs(self)])

    def attels(self):
        self.image = Image.open("pfp.jpg")
        self.image = self.image.resize((200, 200))
        self.image2 = ImageTk.PhotoImage(self.image)
 
        self.labelss = tk.Label(self.master, image=self.image2)
        self.labelss.grid(row=2, column= 3, padx =10, pady=10, rowspan=5)

logs = Tk()
a = Person(logs)
a.labeli()
a.entries()
a.buttoni()
a.attels()


logs.mainloop()