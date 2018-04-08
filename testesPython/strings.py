#strings
str1 = "nabucodonozor"

#exibir tudo maiusculo
print(str1.upper())
#exibir tudo minusculo
print(str1.lower())

#converter numero pra string
x = 666
print(type(x))
x1 = str(x)
print(type(x1))

#Verificar se a string contém caracteres não alfabéticos
print(str1.isalpha())
str1="Nabucodonosor123"
print(str1.isalpha())

#Retirar espaços em branco no início e no fim da string
str2 = " Nabucodonosor "
print(str2)
print(str2.strip())

#Juntar cada item da string por meio de um delimitador especificado
print("-".join(str2))

#centralizar strings
str='python'
print(str.center(15,'*'))

