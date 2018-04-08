#Em Python, dicionário é um tipo de estrutura de dados em que há mapeamento entre uma chave (key) e um valor (value).
#criando dicionários em python
contatos = {}

#inserindo dados num dicionário
contatos["Felix"]=["1111-2222"]

#Também podemos fazer isso usando uma lista como valor:
tel_brito = ["2221-3321","3322-3333"]
contatos["Brito"]=tel_brito

contatos["Piazza"]=["4444-4441"]
contatos["Carlos Alberto"]=["4444-5541","7777-4545"]
tel_clodoaldo = ["3333-9999","8888-3333","8888-3434"]
contatos["Clodoaldo"]=tel_clodoaldo

print(contatos)

#acessar valores de uma chave/key(no nosso caso as chaves ou keys são os nomes)
print(contatos["Felix"])   #→ modo mais simples de acesso
tel_capitao = contatos["Carlos Alberto"]        #→ criamos uma variável para receber
print(tel_capitao)                              #→ o conteúdo de uma chave

#alterando o conteúdo de uma chave
contatos["Felix"] = ["9999-1010"]
print(contatos["Felix"])

#Métodos para ordenar dicionários
#Método keys() - identifica as chaves
print(contatos.keys())

#Método values() - vizualiza os valores armazenados
print(contatos.values())

#Método get() - obtem o conteudo associado a chave
print(contatos.get('Brito'))
print(contatos.get('Pele'))

#Método in - verifica se uma chave pertence á um dicionário
print("Piazza" in contatos)

#Método items() - retorna os elementos na forma de tuplas
print(contatos.items())

#Método copy() - copia um dicionário inteiro
jogadores = contatos.copy()
print(jogadores)

#Método clear()
contatos.clear()
print(contatos)

#também pode-se criar dicionários à partir do método dict - ele aceita tuplas e listas como paramêtros
camisas = dict([(7,"Jairzinho"),(9,"Tostao"),(10,"Pele"),(11,"Rivelino")])

#fromkeys permiti criar vários valores para uma mesma chave
{}.fromkeys([16,4,2,3],"defesa")

