def etanol(opcao):
        print("\nCódigo selecionado:  - ",opcao)
        print("Produto selecionado: é o etanol")
        pagamento = int(input("\ndigite 1 pra o total em reais \ndigite 2 para total em litros:\n"))
        if(pagamento==1):
            valor=int(input("\ndigite o total em reais : "))
            total = float(valor/3.50)
            return print("o valor total em litros de R$",valor,valor ," é de  " ,total," litros.")
        else:
            litros=int(input("\ndigite o total em litros: "))
            total = float(litros*3.5)
            return print("o valor total em reais de ",litros,"é de R$",total,".")


def gasolina(opcao):
        print("\nCódigo selecionado: - ",opcao)
        print("Produto selecionado: gasolina")
        pagamento = int(input("\ndigite 1 pra o total em reais \ndigite 2 para total em litros:\n"))
        if(pagamento==1):
            valor=int(input("\ndigite o total em reais : "))
            total = float(valor/4.65)
            return print("o valor total em litros de R$",valor,valor ," é de  " ,total," litros.")
        else:
            litros=int(input("\ndigite o total em litros: "))
            total = float(litros*4.65)
            return print("o valor total em reais de ",litros,"é de R$",total,".")