from tkinter import *

def converter_cm_para_metros():
    try:
        cm = float(entry_cm.get())
        metros = cm / 100
        label_resultado.config(text=f"{cm} cm é igual a {metros} metros.")
    except ValueError:
        label_resultado.config(text="Por favor, insira um valor numérico.")


janela = Tk()
janela.title("Conversor de Centímetros para Metros")


label_instrucao = Label(janela, text="Digite o valor em centímetros:")
label_instrucao.pack()

entry_cm = Entry(janela)
entry_cm.pack()

button_converter = Button(janela, text="Converter", command=converter_cm_para_metros)
button_converter.pack()

label_resultado = Label(janela, text="")
label_resultado.pack()

janela.mainloop()