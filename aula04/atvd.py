def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

def verificar_situacao(media):
    if media is None:
        return "Nenhuma nota foi inserida"
    elif media == 10:
        return "Parabéns, sua média é 10"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


while True:
    notas_str = input("Digite as notas, separadas por vírgula: ")
    notas = [float(nota) for nota in notas_str.split(",")]

    media = calcular_media(notas)
    situacao = verificar_situacao(media)

    print(f"Nota: {media:.2f}; Situação: {situacao}")

    continuar = input("Deseja continuar? (S/N)").lower()
    if continuar == 's':
        continue
    elif continuar == 'n':
        print('Até logo.')
        break
    else:
        print('caracter desconhecido.')
        for i in range(1):
            continuar = input("Deseja continuar? (S/N)").lower()
            if continuar == 's':
                continue
            elif continuar == 'n':
                print('Até logo.')
                break
            else:
                print('Caracter desconhecido.')
                break
