#método open recebe por parametro
#e - Abre o arquivo apenas para leitura (read). Você não pode inserir ou modificar o conteúdo
#w - Abre o arquivo apenas para escrita. O arquivo que existia será sobrescrito pelo atual.
#a – append - Abre o arquivo para inserção de dados que serão escritos no final do arquivo
#r+ - Abre o arquivo para leitura e escrita.
#a = open('C:\\Users\\Italo\\Downloads\\Outros\\MEGA-RECOVERYKEY.txt', 'r')

#for linha in a:
#    print(linha)

#faz a leitura do arquivo
#conteudo = a.read()
#print(conteudo)

#faz a leitura de todas as linhas do arquivo retornando uma lista
#lista = a.readlines()
#print(lista)


#faz a leitura de uma linha e armazena o ponteiro ao final da linha,
# e cada vez que executa a função avança o ponteiro junto com a linha

#lin1 = a.readline()
#lin2 = a.readline()
#lin3 = a.readline()

#print(lin1, lin2, lin3)

#criar um arquivo vazio (necessário passar w como segundo parametro)
#b = open("c:\\users\\italo\\novoarquivo.txt","w")

#escrever em um arquivo
#b.write("Ouviram do Ipiranga as margens plácidas")

#c = open("c:\\users\\italo\\novoarquivo.txt","r")
#content = c.readlines()
#print(content)

#TODO: está dando erro,
#inserindo mais conteudo
#a = open('C:\\Users\\Italo\\Downloads\\Outros\\MEGA-RECOVERYKEY.txt', 'r')
#dados = a.readlines()
#print(dados)
#dados.append("<p>Nova linha inserida</p>")
#a = open('C:\\Users\\Italo\\Downloads\\Outros\\MEGA-RECOVERYKEY.txt', 'r')
#a.writelines(dados)