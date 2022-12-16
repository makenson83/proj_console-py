from Pessoa import *
import os
def clear():
    os.system('clear')

pessoa1 = Pessoa("Gustavo","M","1349038",True)
pessoa2 = Pessoa("Makenson","M","4893020",True)

clear()
pessoa2.set_nome("ana")
pessoa2.set_sexo("F")
pessoa2.set_cpf("5352672")
pessoa2.desativar()

print(pessoa2.get_nome(),pessoa2.get_sexo(),pessoa2.get_cpf(),pessoa2._ativo)
print(pessoa1.get_nome(),pessoa1.get_sexo(),pessoa1.get_cpf(),pessoa1._ativo)


