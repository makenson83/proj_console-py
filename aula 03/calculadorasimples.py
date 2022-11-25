import os
def clear(): os.system('clear')

class operador:
    def __init__(self,opcao,operador,info):
        self.opcao = opcao
        self.operador = operador
        self.info = info

calculadora = []
x = 0
calculadora.append(operador(1,"+","adição"))
calculadora.append(operador(2,"-","substração"))
calculadora.append(operador(3,"x","multiplicação"))
calculadora.append(operador(4,"÷","divição"))

def calc():
    print("==========================")
    print("|{:<3}|{:<4}|{:<15}|".format("Nº","Op","informação "))
    print("|---+----+---------------|")
    for v in calculadora:
        print("|{:<3}|{:<4}|{:<15}|".format(v.opcao, v.operador, v.info))
    print("==========================")
while(x==0):
    clear()
    calc()
    res = int(input("\nselecione o numero da operação que realizar: "))

    class calculo:
        def switch(self,operacao):
            default = "valor não encontrado"
            return getattr(self, 'case_'+str(operacao), lambda:default)()
        def case_1(self):
            print("\n",res,"- A sua opção foi adição!")
            v1 = int(input("\ndigite o valor 1: "))
            v2 = int(input("digite o valor 2: "))
            return v1+v2
        def case_2(self):
            print("\n",res,"- A sua opção foi subtração!")
            v1 = int(input("\ndigite o valor 1: "))
            v2 = int(input("digite o valor 2: "))
            return v1-v2
        def case_3(self):
            print("\n",res,"- A sua opção foi multiplicação!")
            v1 = int(input("\ndigite o valor 1: "))
            v2 = int(input("digite o valor 2: "))
            return v1*v2
        def case_4(self):
            print("\n",res,"- A sua opção foi divisão!")
            v1 = int(input("\ndigite o valor 1: "))
            v2 = int(input("digite o valor 2: "))
            return v1/v2
    s = calculo() 
    print("\n o valor resultante é: ",s.switch(res))
    x=int(input("\nDeseja realizar outra operação? sim (0) ou não (1): "))
clear()

    


