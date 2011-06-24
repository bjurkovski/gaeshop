from google.appengine.ext import db

class Produto(db.Model):
    preco = db.FloatProperty()
    nome = db.StringProperty()
    estoque = db.IntegerProperty()
    visualizacoes = db.IntegerProperty()

class Pedido(db.Model):
    usuario = db.UserProperty()
    estado = db.StringProperty()
    formaDePagamento = db.StringProperty()
    enderecoEntrega = db.StringProperty()

class ReceptorPagamento(db.Model):
    pass

class Carrinho(db.Model):
    pass

class Usuario(db.Model):
    nome = db.StringProperty()
    endereco = db.StringProperty()
    telefone = db.StringProperty()
    email = db.StringProperty()
    CEP = db.StringProperty()
    senha = db.StringProperty()
    codigo = db.StringProperty()
