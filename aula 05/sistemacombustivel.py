import os
from Combutivel import *
def  clear():
    os.system('clear')

def tabela():
    print("-------------------")
    print("|{:<3}|{:<12}|{:<7}|".format("cod","combustivel","valor"))
    print("====================")
    for v in posto:
        print("|{:<3}|{:<12}|{:<7}|".format(v.cod, v.combustivel, v.valor)) 
    print("----------------")


class combustivel:
    def __init__(self,cod,combustivel,valor):
        self.cod = cod
        self.combustivel = combustivel
        self.valor = valor

class abastecer:
    def switch(self,combustivel):
        defaut = "combustivel não encontrado"
        return getattr(self, 'case_'+str(combustivel), lambda:defaut)()

    def case_1(self):
        etanol(opcao)
        
posto=[]
x=0

posto.append(combustivel(1,"etanol","R$ 3,50"))
posto.append(combustivel(2,"gasolina", "R$ 4,65"))
posto.append(combustivel(3,"g. aditivada","R$ 6,59"))
posto.append(combustivel(4,"diesel s500", "R$ 4,99"))
posto.append(combustivel(5,"diesel s10","R$ 6,29"))
s=abastecer()
while(x==0):
    clear()
    tabela()
    opcao= int(input("\ndigite o código do produto: "))
    print("\nsegue o resultado: " ,s.switch(opcao))
    x=int(input("deseja realizar novo abastecimento? sim (0) ou não (1): "))