class Pessoa:
    def __init__(self,nome,sexo,cpf,ativo):
        self._nome = nome
        self._sexo = sexo
        self._cpf = cpf
        self._ativo = ativo

    #metodo desativada
    def desativar (self):
        self._ativo  = False;
        print("a pessoa foi desativada com sucesso!")

    #metodo ativar 
    def desativar(self):
        self._ativo = True
        print("a pessoa foi ativada com sucesso!")

    #metodo que retorna o nome 
    def get_nome(self):
        return self._nome

    #metodo que altera  o nome
    def set_nome(self,nome):
        self._nome = nome

    #metodo que retorna o sexo
    def get_sexo(self):
        return self._sexo

    #metodo que altera o sexo
    def set_sexo(self,sexo):
        self._sexo = sexo 

    #metodo que retotorna o cpf
    def get_cpf(self):
        return self._cpf

    #metodo que altera o cpf
    def set_cpf(self,cpf):
        self._cpf = cpf


    