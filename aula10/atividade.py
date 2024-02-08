from tkinter import *
from tkinter import messagebox

def login():
    email = entry_email.get()
    password = entry_password.get()

    if len(password) < 6:
        messagebox.showerror("Erro", "A senha deve ter pelo menos 6 caracteres.")
    elif "@" not in email:
        messagebox.showerror("Erro", "O e-mail deve conter o caractere '@'.")
    else:
        messagebox.showinfo("Login", "Login bem-sucedido!")

janela = Tk()
janela.title("Login")

frame = Frame(janela)
frame.pack(padx=20, pady=20)

label_email = Label(frame, text="E-mail:")
label_email.grid(row=0, column=0, sticky="w")

entry_email = Entry(frame)
entry_email.grid(row=0, column=1)

label_password = Label(frame, text="Senha:")
label_password.grid(row=1, column=0, sticky="w")

entry_password = Entry(frame, show="*")
entry_password.grid(row=1, column=1)

btn_login = Button(frame, text="Login", command=login)
btn_login.grid(row=2, columnspan=2, pady=10)

janela.mainloop()