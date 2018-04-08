class Contato:
    todos_contatos = []
    def __init__ (self, nome, email):
        self.nome = nome
        self.email = email
        Contato.todos_contatos.append (self)

class Fornecedor (Contato):
    def pedido (self, pedido):
        print('pedido {} feito por {}'.format(pedido, self.nome))

c = Contato("Fullano", "fullano@gmail.com")
f = Fornecedor("Beltrano", "beltrano@gmail.com")

print(c.nome,c.email,f.nome,f.email)

f.pedido("coca cola")

class Amigo (Contato):
    def __init__ (self, nome, email, telefone):
        super(). __init__ (nome,email)
        self.telefone = telefone

a = Amigo("italo", "italo@gmail.com", "8888-8888")