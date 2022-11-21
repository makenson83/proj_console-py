class veiculo:
    def __init__(self, marca, modelo, ano, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa


cadastro = []
x = 0


def tela():
    def clear(): return os.system('clear')
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
            print("{:<14} {:<8} {:<19} {:<9}".format(
                v.marca, v.modelo, v.ano, v.placa))
