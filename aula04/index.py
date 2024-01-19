dicionario = {
    'modulo':'python',
    'instituição':'Infinity'
}

# Dict comprehension

dicionario = {num: num * 10 for num in range(1,11)}

# metodo construtor 
dicionario = dict()# Dicionario Vazio

dicionario = dict([('Modulo', 'Python'), ('institução', 'Infinity School')])

dicionario = dict(Modulo = 'Python', Institucao = 'infinity School')

#dicionario = dict({'Modulo':'Python', 'Institucao':'Infiniti school'} Modulo = 'Logica de programação')

list(dicionario)
#retorna uma lista com todas as chaves usadas no dicionario

dicionario[chave]
#Retorna o valor da chave especiifcada entre colchetes

del dicionario[chave]
#Remove a chave e seu respectivo valor do dicionario

len(dicionario)
#Retorna o numero de itens de um dicionario

dicionario[chave] = valor 
#Se a chave já existir no dicionario, terá seu valor sobrescrito. Se achave não existir, ela será criada e o valor será atribuido a ela 

chave in dicionario
#Retorna True se a chave for encontrada no dicionario, senão, retornará False

#list(Dicionario)

dicionario = {
    'Modulo': 'Python', 
    'Instituição':'Infinity School'
}

print(list(dicionario))

#len(Dicionario)

dicionario = {
    'Modulo': 'Python', 
    'Instituição':'Infinity School'
}

print(len(dicionario))

#Dicionario[chave]
dicionario = {
    'Modulo': 'Python', 
    'Instituição':'Infinity School'
}

print(dicionario['Modulo'])

#dicionario[chave] = valor
dicionario = {
    'Modulo': 'Python',
    'Instituição': 'Infinity School'
}
dicionario['Modulo'] = 'Logica da Programação'
dicionario['Numero da aula'] = 3
print(dicionario)


#del dicionario[chave]
dicionario = {
    'modulo': 'python',
    'instituição':'infinity school'
}

del dicionario['modulo']
print(dicionario)

#chave in dicionario
dicionario = {
    'modulo': 'python',
    'instituição':'infinity school'
}
print('Modulo' in dicionario)
print('Numero da aula' in dicionario)

chave not in dicionario
#Retorna True se a chave não for encontrada no dicionário, senão, retornará False

dicionario.clear()
#Remove todos os itens do dicionário

dict.fromkeys(iteravel)
#Cria um novo dicionário com chaves proveniente do iteravel(uma lista, um dicionário), os valores por padrão serão None

iter()
#Retorna um iterador para as chaves do dicionário. Retorna o mesmo que dicionario.keys()

dicionario.copy()
#Retorna uma cópia do dicionário

dicionario.get(chave, valorpadrao)
#Retorna o valor para a chave especificada se esta existir no dicionário, senão, será retornado um valor padrão definido. Caso este valor não seja definido, a função retornará None

#chave nor in dicionario
dicionario = {
    'modulo': 'python',
    'instituição':'infinity school'
}
print('Modulo' not in dicionario)
print('Numero da aula'not in dicionario)

#iter(dicionario)
print(iter(dicionario))
print(list(iter(dicionario)))

#dicionario.clear()
dicionario = {
    'modulo': 'python',
    'instituição':'infinity school'
}
dicionario.clear()
print(dicionario)

#dicionario.copy()
dicionario = {
    'modulo': 'python',
    'instituição':'infinity school'
}

dicionario2 = dicionario.copy()
print(dicionario2)

#dict.fromkeys(iteravel)
dicionario = ['modulo', 'instituicao']
print(dict.fromkeys(dicionario))

#dicionario.get(chave)
dicionario = {
    'modulo': 'python',
    'instituição':'infinity school'
}
print(dicionario.get('modulo', 'Chave Inexistente'))
print(dicionario.get('Numero da Aula', "Chave inexistente"))

dicionario.items()
#Retorna uma lista contendo pares de tuplas, onde, em cada uma dessas tuplas, o primeiro elemento será a chave do dicionário e o segundo elemento o valor.

dicionario.values()
#Retorna uma lista dos valores do diconário

dicionario.update(dicionario)
#Atualiza o dicionário com os elementos de outro objeto de dicionário ou de um iterável de pares chave / valor.

dicionario.keys()
#Retorna uma lista das chaves do dicionário

dicionario.pop(chave, valorpadrao)
#Remove a chave se esta existir no dicionário, senão, retornará o valor padrão. Caso a chave não exista e não existir um valor padrão, um erro do tipo KeyError será lançado

OBS
#Existem diversas funções para os dicionários em Python, experimente-as e veja o que cada função faz.


#dicionario.items()
dicionario = {
    'modulo': 'python',
    'instituição':'infinity school'
}
print(dicionario.items())
for chave, valor in dicionario.items():
    print(f'{chave} - {valor}')


#dicionario.keys()
dicionario = {
    'modulo': 'python',
    'instituição':'infinity school'
}
print(dicionario.key())


#dicionario.values()
dicionario = {
    'modulo': 'python',
    'instituição':'infinity school'
}
print(dicionario.values())


#dicionario.pop(chave, valor padrao)
dicionario = {
    'modulo': 'python',
    'instituição':'infinity school'
}
dicionario.pop('modulo', 'chave inexistente')
print(dicionario)

#dicionario.update(iteravel)
dicionario = {
    'modulo': 'python',
    'instituição':'infinity school'
}
dicionario.update([('modulo', 'logica da programacao')])
dicionario.update([('modulo', 'logica da programacao')])
dicionario.update([('modulo', 'logica da programacao')])

conjunto = {'python', 'infinity school', 3}

#usando compreensão de conjuntos
conjunto = {letra for letra in 'Infinity' if letra not in 'aeiou'}

#usando o metodo construtos
conjunto = (['python', 'infinity school', 3])

elemento in conjunto
#Retorna True se o elemento exsitir naquele conjunto, senão, retorna False

elemento not in conjunto
#Retorna True se o elemento não exsitir naquele conjunto, senão, retorna False

conjunto.update()
#Atualiza o conjunto, adicionando os elementos entre parênteses

len(conjunto)
#Retorna o número de itens de um conjunto

conjunto.copy()
#Retorna uma cópia do conjunto

conjunto.add(elemento)
#Adiciona um elemento ao conjunto

conjunto.remove(elemento)
#Remove o elemento do conjunto. Uma exceção do tipo KeyError será lançada se o elemento não existir no conjunto

conjunto.clear()
#Remove todos os elementos do conjunto

conjunto.discard(elemento)
#Remove o elemento se o mesmo existir no conjunto