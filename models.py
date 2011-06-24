from google.appengine.ext import db

class Produto(db.Model):
    preco = dbself.FloatProperty()
    nome = dbself.StringProperty()
    estoque = dbself.IntegerProperty()
    visualizacoes = dbself.IntegerPropery()

class Pedido(db.Model):
    usuario = dbself.UserProperty()
    estado = dbself.StringProperty()
    formaDePagamento = dbself.StringProperty()
    enderecoEntrega = dbself.StringProperty()

class ReceptorPagamento(db.Model):
    pass

class Carrinho(db.Model):
    pass

class Usuario(db.Model):
    nome = dbself.StringProperty()
    endereco = dbself.StringProperty()
    telefone = dbself.StringProperty()
    email = dbself.StringProperty()
    CEP = dbself.StringProperty()
    senha = dbself.StringProperty()
    codigo = dbself.StringProperty()
