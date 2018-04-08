import random

lista = ["oi", 123]

print(lista[1])

#verificar se existe um valor na lista
print("oi" in lista)

lista_num=[10,50,40,30,50,90,70]

#método para obter valor minimo/menor da lista
print(min(lista_num))

#método para obter valor maximo/maior da lista
print(max(lista_num))

#método para obter a soma dos valores da lista
print(sum(lista_num))

estados = ['SP','RJ','ES']

#utilizamos o método append para adicionar valores a lista
estados.append('MG')
print(estados)

#utilizamos o método pop para remover da lista um valor/objeto que sabemos sua posição
estados.pop(0)
print(estados)

#utilizamos o método remove caso não soubermos a posição
estados.remove('RJ')
print(estados)

#utilizamos o método insert para adionar um valor à uma posição especifica na lista
estados.insert(1,'SP')
print(estados)

#utilizamos o sort para ordenar
estados.sort()
print(estados)

#para reverter a ordem de exibição(atenção, ele só inverte as posições e não faz ordenação decrescente como dia no SIA)
estados.reverse()
print(estados)

#para misturar aleatóriamente os valores da lista importa-se o random e utiliza-se o método shuffle
random.shuffle(estados)
print(estados)

#contador de ocorrências de um valor
print(estados.count('RJ'))

#verificar indice do valor
print(estados.index('MG'))

#prolongação de uma lista para dentro de outra
sul = ["RS", "SC", "PR"]
estados.extend(sul)
print(estados, sul)