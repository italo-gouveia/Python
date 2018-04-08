class Pessoa:
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade
    def getIdade(self):
        return self.idade

class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome="", idade=0):
        Pessoa.__init__(self, nome, idade)
        self.cpf = cpf

class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, nome="", idade=0):
        super(). __init__(nome, idade)
        self.cnpj = cnpj

p = Pessoa("italo", 20)
pf = PessoaFisica("João", 50, 118)
pj = PessoaJuridica("Maria", 30, 125)

print(p.getIdade())
print(p.nome, p.idade)
print(pf.nome, pf.idade, pf.cpf)
print(pj.nome, pj.idade, pj.cnpj)

