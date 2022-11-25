import os
class produto:
    def __init__(self,cod,produto,valor):
        self.cod = cod
        self.produto = produto
        self.valor = valor

loja = []
x = 0

loja.append(produto(1,"camisa","R$ 100,00"))
loja.append(produto(2,"calça","R$ 150,00"))
loja.append(produto(3,"sapato","R$ 499,00"))

def clear(): os.system('clear')

def tabela():
    print("------------------------")
    print("|{:<3}|{:<12}|{:<12}".format("cod","produto","valor"))
    print("========================")
    for v in loja
        print("|{:<3}|{:<12}|{:<12}|".format(v.cod, v.produto, v.valor))
    print("-----------------------")

class compra:
    def switch(self,produto):
        default = "produto não encntrado"
        return getattr(self,'caseS)
        print

    
S