import os
def clear():
    os.system('clear')

def tabela():
    print("{:<4} {:<10} {:<10} {:<5}".format("cod","produto","valor","quantidade"))
    for v in mercadinho:    
        print("{:<4} {:<10} R${: .2f} {:>4}".format(v.cod,v.produto,v.valor,v.quantidade))  


class produtos:
    def __init__(self,cod,produto,valor,quantidade):
        self.cod=cod
        self.produto = produto
        self.valor = valor
        self.quantidade = quantidade
    

clear()
x=0
mercadinho=[]
codigo=0
while(x==0):
    produto=str(input("\ndigite um produto: "))
    valor=float(input("digite o valor: "))
    quantidade=int(input("\ndigite a quantidade: "))
    mercadinho.append(produtos(codigo,produto,valor,quantidade))
    codigo +=1
    clear()
    tabela()
    x=int(input("\ndeseja cadastrar outro produto?\n 0 - sim\n 1 - não\n\nsua opção foi: "))
    clear()




     