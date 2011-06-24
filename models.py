from google.appengine.ext import db

class Product(db.Model):
    price = db.FloatProperty()
    name = db.StringProperty()
    description = db.StringProperty()
    stock = db.IntegerProperty()
    views = db.IntegerProperty()

    def __init__(self, name, description, price, stock)
        pass

    def getStock(self):
        return 0

    def match(self, search):
        return True

    def addView(self):
        self.view += 1

class Order(db.Model):
    user = db.UserProperty()
    state = db.StringProperty()
    paymentMethod = db.StringProperty()
    shippingAddress = db.StringProperty()

class PaymentReceiver(db.Model):
    pass

class ShoppingCart(db.Model):

    def addProduct(self,product): 
        return True

    def getProducts(self)
        return []

class User(db.Model):
    name = db.StringProperty()
    address = db.StringProperty()
    phone = db.StringProperty()
    email = db.StringProperty()
    zipcode = db.StringProperty()
    password = db.StringProperty()
    code = db.StringProperty()

    def addProductToShoppingCart(self,product):
        pass
        
    def getAccount(self):
        pass

    def getShoppingCart(self):
        pass

    def getOrders(self):
        pass

    def addOrder(self,paymentMethod,shippingAddress):
        return True
