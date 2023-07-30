import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  

messagebox.showinfo("Olá!!", "Esse é um teste de caixas de dialogo em Python")

resultado = messagebox.askquestion("Escolhe ai", "Escolha um")

if resultado == 'yes':
    messagebox.showinfo("Você escolheu 'Sim'.", "Você escolheu 'Sim'.")
else:
    messagebox.showinfo("Você escolheu 'Não'.", "Você escolheu 'Não'.")

root.mainloop()
