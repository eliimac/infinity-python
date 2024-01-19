 # # #Desenvolva um programa em Python que permita ao usuário digitar várias notas. Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno. Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.
#from back import *


# notas = []

# def CalcularMedia(nota1, nota2, nota3, nota4):
#     resultado = (nota1+nota2+nota3+nota4) / 4
#     return resultado

# def VerificarSituacao(resultado):
#     situacao = resultado.pop()
#     if situacao >= 7:
#         return "Aprovado!"
#     elif situacao == 10:
#         return "Parabéns, sua média é 10!"    

#     else:
#         return "Reprovado!"


# # for n in range(4):
# #     nota = float(input('Digite a nota: '))
# #     notas.append(nota)


# nota1 = float(input("digite a nota: "))
# nota2 = float(input("digite a nota: "))
# nota3 = float(input("digite a nota: "))
# nota4 = float(input("digite a nota: "))


# # print(CalcularMedia(notas)) 

# print(f'{CalcularMedia(nota1, nota2, nota3, nota4)}')
# print(f'{VerificarSituacao(resultado)}')


# def calcular_media(notas):
#     # Calcula a média das notas
#     media = sum(notas) / len(notas)
#     return media

# def verificar_situacao(media):
#     # Verifica a situação do aluno com base na média
#     if media == 10:
#         return "Parabéns, sua média é 10"
#     elif media >= 7:
#         return "Aprovado"
#     else:
#         return "Reprovado"

# # def main():
#     # Solicita ao usuário que digite as notas, separadas por vírgula
# notaStr = input("Digite as notas, separadas por vírgula: ")
# # Converte a string de notas em uma lista de floats
# notas = [float(nota) for nota in notaStr.split(",")]
# # Chama a função calcular_media
# media = calcular_media(notas)

# # Chama a função verificar_situacao e exibe o resultado
# situacao = verificar_situacao(media)
# print(f"Média: {media:.2f} - {situacao}")

# # # Chama a função principal
# if __name__ == "__main__":
#     main()


# def calcular_media(notas):
#     media = sum(notas) / len(notas)
#     return media

# def verificar_situacao(media):
#     if media is None:
#         return "Nenhuma nota foi inserida"
#     elif media == 10:
#         return "Parabéns, sua média é 10"
#     elif media >= 7:
#         return "Aprovado"
#     else:
#         return "Reprovado"


# while True:
#     notas_str = input("Digite as notas, separadas por vírgula: ")
#     notas = [float(nota) for nota in notas_str.split(",")]

#     media = calcular_media(notas)
#     situacao = verificar_situacao(media)

#     print(f"Nota: {media:.2f}; Situação: {situacao}")

#     continuar = input("Deseja continuar? (S/N)").lower()
#     if continuar == 's':
#         continue
#     elif continuar == 'n':
#         print('Até logo.')
#         break
#     else:
#         print('caracter desconhecido.')
#         for i in range(1):
#             continuar = input("Deseja continuar? (S/N)").lower()
#             if continuar == 's':
#                 continue
#             elif continuar == 'n':
#                 print('Até logo.')
#                 break
#             else:
#                 print('Caracter desconhecido.')
#                 break










# def NomeDaFuncao():

#     print("Print da função")

#     x = 10



# resultado = NomeDaFuncao()

# print(NomeDaFuncao())
num1 = 10

num2= 20



def print_message(num1,num2):

    if(num1 >= 15):

        num2 += 15

    else:

        num1 += 40

    return f"numero 1 = {num1}, numero 2 = {num2}"



print(print_message(num1, num2))