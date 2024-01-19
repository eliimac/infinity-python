bancoDeAlunos = [
    {
        'nome':'julia',
        'notas': [7.0, 5.5, 6.9],
        'media': 7.0,
        'situacao': True
    },
        {
        'nome':'roberto',
        'notas': [7.0, 5.5, 6.9],
        'media': 7.0,
        'situacao': True
    }

]
# percorrendo o dicionario
print(bancoDeAlunos[1]['media'])
for u in bancoDeAlunos:
    #primeiro é a chave K e o segundo é o valor V
    for k,v in u.itens():
        print(f'{k} - {v} ')