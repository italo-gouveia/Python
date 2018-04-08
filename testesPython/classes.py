class Empregado:
    'Classe base para empregados'

    contador = 0

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        Empregado.contador +=1

    def mostra_contador(self):
        print("Número de empregados: %d" % Empregado.contador)
    def mostra_empregado(self):
        print("Nome: ", self.nome, ", Salário: ", self.salario)

emp1 = Empregado("Fabiano",1000)
emp1.mostra_contador()
emp1.mostra_empregado()
emp1.idade = 5
emp2 = Empregado("João Neves", 1500)
emp2.mostra_contador()
emp2.mostra_empregado()
del emp2.idade


