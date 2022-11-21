import os

class veículo:
    def __init__(self, marca, modelo, ano, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa


cadastro = []
x = 0
def clear(): os.system('clear')

def tela():  
    clear()
    print("_________________________________")
    print("__________cadastro de veiculo_________")
    print("_________________________________________")

    cadastro.sort(key=lambda x: x.marca)

    print("{:<14} {:<8} {:<10} {:<9}".format(
        "marca", "modelo", "ano", "placa"))

    y = 0
    while (y <= x):
        for v in cadastro:
            print("{:<14} {:<8} {:<10} {:<9}".format(
                v.marca, v.modelo, v.ano, v.placa))
            y += 1


res = int(input("\ndeseja cadastrar um novo veiculo? sim(1) / não(0) "))

while (res == 1):
   
    cadmarca = input("\ndigite a marca do veículo ")
    cadmodelo = input("digite o modelo do veículo ")
    cadano = input("digite o ano do veículo ")
    cadplaca = input("digite a placa do veículo ")
    cadastro.append(veículo(cadmarca, cadmodelo, cadano, cadplaca))
    tela()
    x += 1

    res = int(input("\ndeseja cadastrar um novo veículio? sim(1) / não(0)"))
