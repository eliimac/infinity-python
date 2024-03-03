class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return litros_abastecidos
        else:
            print("Quantidade de combustível insuficiente na bomba.")
            return 0

    def abastecer_por_litro(self, litros):
        valor_pagar = litros * self.valor_litro
        return valor_pagar

    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro

    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade_combustivel):
        self.quantidade_combustivel = nova_quantidade_combustivel


bomba = BombaCombustivel("Gasolina", 5.0, 100)

print("Abastecimento por valor:")
litros_abastecidos = bomba.abastecer_por_valor(50)
print(f"Foram abastecidos {litros_abastecidos:.2f} litros de {bomba.tipo_combustivel}.")
print(f"Quantidade restante na bomba: {bomba.quantidade_combustivel:.2f} litros.")

print("\nAbastecimento por litro:")
valor_pagar = bomba.abastecer_por_litro(20)
print(f"O cliente deverá pagar R$ {valor_pagar:.2f}.")

print("\nAlteração de valor do litro:")
bomba.alterar_valor(5.5)
print(f"Novo valor do litro: R$ {bomba.valor_litro:.2f}.")

print("\nAlteração de tipo de combustível:")
bomba.alterar_combustivel("Álcool")
print(f"Novo tipo de combustível: {bomba.tipo_combustivel}.")

print("\nAlteração de quantidade de combustível na bomba:")
bomba.alterar_quantidade_combustivel(120)
print(f"Nova quantidade de combustível: {bomba.quantidade_combustivel:.2f} litros.")