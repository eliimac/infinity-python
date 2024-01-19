n = []
par = []
impar = []
z = []


for i in range(1, 11):
    num = int(input("Digite "))
    n.append(num)
    sabern = n.pop()
    if sabern % 2 == 0:
        par.append(sabern)
        # lendo a lista para saber se têm zeros
        for zero in par:
            if zero == 0:
                par.remove(zero)
                z.append(zero)
    else:
        impar.append(sabern)    


tuplaI = tuple(impar)
   # summ soma todos os itens das listas 
somaI = sum(impar)
somaP = sum(par)

print(f"Número(s) par(es) {par}, número(s) na lista {len(par)} e a soma {somaP}")
print(f"Número(s) ímpar(es) {tuplaI}, número(s) na tupla {len(tuplaI)} e a soma {somaI}")
print(f'{z}, zero(s) digitado(s) {len(z)}')
