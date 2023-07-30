import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Esconde a janela principal, mostrando apenas a caixa de diálogo.

# Exibe uma caixa de diálogo de informação.
messagebox.showinfo("Olá!!", "Esse é um teste de caixas de dialogo em Python")

# Exibe uma caixa de diálogo de pergunta com opções 'Sim' ou 'Não'.
resultado = messagebox.askquestion("Escolhe ai", "Escolha um")

if resultado == 'yes':
    messagebox.showinfo("Você escolheu 'Sim'.", "Você escolheu 'Sim'.")
else:
    messagebox.showinfo("Você escolheu 'Não'.", "Você escolheu 'Não'.")

root.mainloop()
