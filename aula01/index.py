print("cadastro")
print("_"*60)

emailCad = input('Cadastre o email: ')
emailConf = input('Confirme o email: ')
print("_"*60)
senhaCad = input('Cadastre a senha: ')
senhaConf = input('Confirme a senha: ')
print("_"*60)

while emailCad.lower() != emailConf.lower() or senhaCad != senhaConf:
    print('Email ou senha diferente, digite novamente')
    emailConf = input('Confirme o email: ')
    senhaConf = input('Confirme a senha: ')

print("_"*60)
print('Cadastro feito com sucesso!')   
print("_"*60)

emailDig = input('Digite o email para logar: ')
senhaDig = input('Digite a senha para logar: ')

if emailDig.lower() == emailCad.lower() and senhaDig == senhaCad:
    print('Bem vindo.')

else:
    for numeroTent in range(1, 10):
        print('Email ou senha diferente, digite novamente')
        emailDig = input('Digite o email para logar: ')
        senhaDig = input('Digite a senha para logar: ')
        if emailDig.lower() == emailCad.lower() and senhaDig == senhaCad:
            break
    print('Bem vindo')       
           )         
#             break   
#             print("Bloqueado!")
