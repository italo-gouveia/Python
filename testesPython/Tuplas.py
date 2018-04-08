#tuplas são bem similares as listas com uma pequena diferença, elas são imutaveis

minhaTupla = (0, 1, 2)

#slice, fatiando uma lista ou tupla para exibir apenas os valores desejados
#defini-se o indice inicial à partir do qual sera feita a fatia e até qual indice essa fatia irá
print(minhaTupla[0:3])

#fatia tudo desde o indice zero até o que foi definido no segundo paramêtro
print(minhaTupla[:3])

#fatia tudo a partir do indice definido no primeiro paramêtro até o fim da lista ou tupla
print(minhaTupla[1:])

#fatia a tupla inteira
print(minhaTupla[:])

#verificar tamanho da tupla
print(len(minhaTupla))

#concatenar tuplas
parte1=("Ouviram","do","Ipiranga")
parte2=("as","margens","plácidas")
verso1 = parte1+parte2
print(verso1)

#Quando definimos uma tupla com um único elemento, devemos inserir a vírgula,
#como fizemos aqui. Se apenas criarmos uma tupla com um único elemento – como,
#por exemplo, mi2 = (‘mi’) –, a linguagem Python entenderá que se trata de uma string entre parênteses.
#Neste código, repetimos o elemento da tupla 10 vezes, mas sem modificar a original.
mi=('mi',)         #← Note o detalhe da vírgula!
print(mi*10)
print(mi)

#pode-se verificar se há determinado elemento na tupla assim como nas listas
print("as" in verso1)

#utilização do for/foreach
for i in minhaTupla:
    print(i)

