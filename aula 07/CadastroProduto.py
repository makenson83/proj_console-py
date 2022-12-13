from Produtos import *
import os
def clear():
    os.system('clear')

pratileira=[]
    
def cadastrar():
    x = 0 
    y = 0
    while(x==0): 
        Produto =str(input("digite o nome do Produto: "))
        qtd = float(input("digite o valor unitario: "))
        valor = int(input("digite o quantidade: "))
        pratileira.append(Produtos(y,Produto,valor,qtd,Produtos.estoque(qtd)))
        y += 1
        tabela()
        x=int(input('deseja cadastrar novo produto?\n 0 - (sim)\n 1 (não)\nsua decisão foi: '))

def tabela():
    Produtos.cabecalho
    for v in pratileira:
        print("{:<6}{:<4}{:<5}{:<4}{:<4}".format(v.cod,v.produto,v.valor,v.quantidade,v.disponivel))
    


    


    

    





