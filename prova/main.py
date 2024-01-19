from modulo import *


print("""
===============================
Sistema de matrículas
===============================
""")
while True:
    print("""
    1 - Adiconar novo aluno;
    2 - Remover aluno;
    3 - Atualizar aluno;
    4 - Visualizar dicionário de alunos;
    5 - Sair.

    """)
    opcao = int(input('Digite a opção desejada:\n'))
    if opcao not in [1,2,3,4,5]:
        print('Opção não identificada')
    elif opcao == 1:
        adicionar_aluno()
    elif opcao == 2:
        print("""
        ============================
        Alunos existentes no sistema
        ============================
        """)
        ver_alunos()
        print("_"*60)
        remover_aluno()
    elif opcao == 3:
        print("""
        ============================
        Alunos existentes no sistema
        ============================
        """)
        ver_alunos()
        print("_"*60)
        atualizar()
    elif opcao == 4:
        ver_alunos()
    else:
        print('Até mais!')       
        break
