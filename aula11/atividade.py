class Elevador:
    def __init__(self, cap_t, cap_a, andar_t, andar_a):
        self.capacidade_total = cap_t
        self.capacidade_atual = cap_a
        self.andar_total = andar_t
        self.andar_atual = andar_a

    def subir(self):
        if self.andar_atual == self.andar_total:
            print("Você está no andar mais alto!")
        else:
            self.andar_atual += 1
            print("Subindo um andar.")

    def descer(self):
        if self.andar_atual == 0:
            print("Você já está no térreo")
        else:
            self.andar_atual -= 1
            print("Descendo um andar.")

    def entrar(self):
        if self.capacidade_atual == self.capacidade_total:
            print("O elevador já está cheio!")
        else:
            self.capacidade_atual += 1
            print("Entrando uma pessoa.")

    def sair(self):
        if self.capacidade_atual == 0:
            print("Não há ninguém.")
        else:
            self.capacidade_atual -= 1
            print("Saindo uma pessoa.")


def inicializar():
    print(
        """
====|Elevador|====
    """
    )
    ct = int(input("Digite a capacidade total do elevador:\n"))
    ca = int(input("Digite a capacidade atual do elevador:\n"))
    at = int(input("Digite o total de andares do elevador:\n"))
    aa = int(input("Digite o andar atual do elevador:\n"))
    elevador = Elevador(ct, ca, at, aa)
    while True:

        op = input(
            """
_____________________________________________
Deseja entrar, subir, descer, sair ou fechar?\n"""
        ).lower()

        if op not in ["entrar", "subir", "descer", "sair", "fechar"]:
            print("Opção não identificada.")
        else:
            match op:
                case "entrar":
                    elevador.entrar()
                case "subir":
                    elevador.subir()
                case "descer":
                    elevador.descer()
                case "sair":
                    elevador.sair()
                case "fechar":
                    print("fechando...")
                    break


inicializar()
