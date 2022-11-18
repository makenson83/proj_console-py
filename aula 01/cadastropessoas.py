print("-------------------------------------------------")
print("---------cadastro de pessoas----------------------")
print("--------------------------------------------------")

res = int(input("deseja cadastrar uma nova pessoas? 1 - sim ou 0 - não"))

class pessoa:
    def __int__(self, nome, idade, cargo, cidade):  
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.cidade = cidade
      
cadastro = []
x=0

while(res == 1):
   
    cadNome = input("digite o seu nome: ")
    cadIdade = input("digite a sua idade: ")
    cadCargo = input("digite o seu cargo autual: ")
    cadCidade = input("digite a sua cidade: ")

    cadastro.append(pessoa(
        cadNome,
        cadIdade,
        cadCargo,
        cadCidade
    ))

    cadastro.sort(key=lambda x: x.nome)

    print("\n{:<10} {:<6} {:<16} {:<12}".format("nome","idade","cargo","cidade"))
    y = 0
    while(y<=x):
        for v in cadastro:
            print("{:<10} {:<6} {:<16} {:<12}".format(v.nome, v.idade, v.cargo, v.cidade))
            y += 1


    x += 1
    res = int(input("\ndeseja cadastra uma nova pessoa? 1 -sim ou 0 - não:"))




