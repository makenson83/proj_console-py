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
    print("|{:<3}|{:<4}|{:<14}|".format("Nº","Op","informação"))
    print("|--------------------------|")
    for v in calculadora:
        print("|{:<3}|{:<4}|{:<15}|".format(v.opcao, v.operador, v.info))
while(x==0):
    calc()
    res = int(input("\nselecione o numero da operação que realizar o 0 para sair"))

    class calculo:
        def switch(self,operacao):
            default = "valor não encontrado"
            return getattr(self, 'case_'+str(operacao), lambda:default)()
        def case_1(self):
            v1 = int(input("\ndigite o valor 1: "))
            v2 = int(input("\ndigite o valor 1: "))
            return v1+v2
        def case_2(self):
            v1 = int(input("\ndigite o valor 1: "))
            v2 = int(input("\ndigite o valor 1: "))
            return v1-v2
        def case_3(self):
            v1 = int(input("\ndigite o valor 1: "))
            v2 = int(input("\ndigite o valor 1: "))
            return v1*v2
        def case_4(self):
            v1 = int(input("\ndigite o valor 1: "))
            v2 = int(input("\ndigite o valor 1: "))
            return v1/v2
    s = calculo() 
    print("\n",s.switch(res))


