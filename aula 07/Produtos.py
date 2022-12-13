class Produtos:
    def __init__(self,cod,produto,valor,quantidade,disponivel):
        self.cod=cod
        self.produto = produto
        self.valor = valor
        self.quantidade = quantidade
        self.disponivel = disponivel

    def estoque(self,qtd):
        if(qtd==0):
            self.disponivel = False
            return self.disponivel 
        else:
            self.disponivel = True
            return self.disponivel
        
    def cabecalho():
        print("{:<4}{:<10}{:<10}{:<5}{:<7}".format("cod","produto","valor","quantidade disponivel"))    
        print("===============================")


        

