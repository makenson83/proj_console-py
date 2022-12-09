def etanol(opcao):
        print("\nCódigo selecionado:  - ",opcao)
        print("Produto selecionado: é o etanol")
        pagamento = int(input("\ndigite 1 pra o total em reais \ndigite 2 para total em litros:\n"))
        if(pagamento==1):
            valor=float(input("\ndigite o total em reais : "))
            total = float(valor/3.50)
            return print(f'o valor total em litros de R${valor: .2f} é de {total: .2f} litros.')
        else:
            litros=float(input("\ndigite o total em litros: "))
            total = float(litros*3.5)
            return print(f'o valor total em reais de {litros: .2f} é de R${total: .2f}')


def gasolina(opcao):
        print("\nCódigo selecionado: - ",opcao)
        print("Produto selecionado: gasolina")
        pagamento = int(input("\ndigite 1 pra o total em reais \ndigite 2 para total em litros:\n"))
        if(pagamento==1):
            valor=float(input("\ndigite o total em reais : "))
            total = float(valor/4.65)
            return print(f'o valor total em litros de R${valor: .2f} é de {total: .2f} litros.')
        else:
            litros=float(input("\ndigite o total em litros: "))
            total = float(litros*4.65)
            return print(f'o valor total em reais de {litros: .2f} é de R${total: .2f}')

def aditivada(opcao):
        print("\nCódigo selecionado: - ",opcao)
        print("Produto selecionado: gasolina aditivada")
        pagamento = int(input("\ndigite 1 pra o total em reais \ndigite 2 para total em litros:\n"))
        if(pagamento==1):
            valor=float(input("\ndigite o total em reais : "))
            total = float(valor/4.99)
            return print(f'o valor total em litros de R${valor: .2f} é de {total: .2f} litros.')
        else:
            litros=float(input("\ndigite o total em litros: "))
            total = float(litros*4.99)
            return print(f'o valor total em reais de {litros: .2f} é de R${total: .2f}')

def s500(opcao):
        print("\nCódigo selecionado: - ",opcao)
        print("Produto selecionado: diesel s500")
        pagamento = int(input("\ndigite 1 pra o total em reais \ndigite 2 para total em litros:\n"))
        if(pagamento==1):
            valor=int(input("\ndigite o total em reais : "))
            total = float(valor/6.59)
            return print(f'o valor total em litros de R${valor: .2f} é de {total: .2f} litros.')
        else:
            litros=int(input("\ndigite o total em litros: "))
            total = float(litros*6.59)
            return print(f'o valor total em reais de {litros: .2f} é de R${total: .2f}')

def s10(opcao):
        print("\nCódigo selecionado: - ",opcao)
        print("Produto selecionado: diesel s10")
        pagamento = int(input("\ndigite 1 pra o total em reais \ndigite 2 para total em litros:\n"))
        if(pagamento==1):
            valor=float(input("\ndigite o total em reais : "))
            total = float(valor/6.20)
            return print(f'o valor total em litros de R${valor: .2f} é de {total: .2f} litros.')
        else:
            litros = float(input("\ndigite o total em litros: "))
            total = float(litros*6.20)
            return print(f'o valor total em reais de {litros: .2f}litros é de R${total: .2F}')
    