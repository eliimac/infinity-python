
# def CalcularMedia(nota1, nota2, nota3, nota4):
#     resultado = (nota1 + nota2 + nota3 + nota4) / 4
#     return resultado

# def VerificarSituacao(CalcularMedia):
#     if resultado >= 7:
#        return "Aprovado"
#     elif resultado == 10:
#         return "Parebén, sua média é 10"
#     else:
#         return 'Reprovado'



# notas = []

# def CalcularMedia(notas):
#     resultado = sum(notas) / len(notas)
#     return resultado

# def VerificarSituacao(resultado):
#     # situacao = resultado.pop()
#     if resultado == 10:
#         return "Parabéns, sua média é 10!"    
#     elif resultado >= 7:
#         return "Aprovado!"
#     else:
#         return "Reprovado!"


# while True:
#     for n in range(4):
#         nota = input('Digite a nota: ')
#         notas.append(nota)
#     resultado = CalcularMedia(notas)
#     # situacao = VerificarSituacao(resultado)
#     print(f'Média: {resultado} - ')



# def saudacao():
#     print('olá')

# saudacao()    

# def saudacao(nome):
#     print('Olá,', nome)

# saudacao('Maria')    

# def saudacao(nome):
#     return "Olá, " + nome

# print(saudacao('Maria'))    

# def mostrarMensagem():
#     print('Esta é uma rotina!')

# mostrarMensagem()    

# def somar(a, b):
#     return a+b

# # atribui valores para a def
# resultado = somar(2, 3)
# print(resultado)


# ######### atividade 1 ##############
# def saudacao(nome):
#     return "Olá, " + nome

# nome = input('Digite seu nome: ')

# print(saudacao(nome))

 ######### atividade 2 ##############

# def horario(horas):
#     if horas <= 0 or horas <= 5:
#         return 'Boa madrugada'
#     elif horas < 12:
#         return "Bom dia"
#     elif horas < 17:
#         return 'Boa tarde'
#     elif horas < 24:
#         return "Boa noite"      
#     else:
#         return 'Não existe'

# horas = int(input("Digite o horario: ")) 

# print(horario(horas))

 ######### atividade 3 ##############

# def soma(a, b):
#     return a+b

# a = int(input('Digite um numero: '))  
# b = int(input('Digite um numero: '))  
# print(soma(a, b))

 ######### atividade 4 ##############

# def subtracao(a, b):
#     return a - b

# a = int(input('Digite um numero: '))  
# b = int(input('Digite um numero: '))  

# print(subtracao(a, b))

 ######### atividade 5 ##############

# def multiplicacao(a, b):
#     return a * b

# num1 = int(input('Digite um numero: '))  
# num2 = int(input('Digite um numero: '))     

# print(multiplicacao(num1, num2))


######### desafio pratico #######

# def soma(a, b):
#     return a+b

# def sub(a, b):
#     return a-b

# def multi(a, b):
#     return a*b

# def div(a, b):
#     return a/b

# while True:
#     print('Calculadora')
#     print('_'*60)
#     print("""
#     A = adição
#     S = subtração
#     M = multiplicação
#     D = Divisão
#     P = parar
#     """)
#     print('_'*60)
#     letra = input('Digite a operação que deseja: \n').lower()
#     match letra:
#         case "a":
#             num1 = int(input('Digite um numero: '))
#             num2 = int(input('Digite um numero: '))

#             print(soma(num1, num2))
#         case "s":
#             num1 = int(input('Digite um numero: '))
#             num2 = int(input('Digite um numero: '))

#             print(sub(num1, num2))
#         case 'm':
#             num1 = int(input('Digite um numero: '))
#             num2 = int(input('Digite um numero: '))

#             print(multi(num1, num2))
#         case 'd':
#             num1 = int(input('Digite um numero: '))
#             num2 = int(input('Digite um numero: '))

#             print(div(num1, num2))   
#         case 'p':
#             break
#         case _:
#             print("Caracter não identificado")
#             continue

def joao(abracadabra):
    print('magica')

   