from google.appengine.ext import db

class Product(db.Model):
    price = db.FloatProperty()
    name = db.StringProperty()
    stock = db.IntegerProperty()
    views = db.IntegerProperty()

class Order(db.Model):
    user = db.UserProperty()
    state = db.StringProperty()
    paymentMethod = db.StringProperty()
    shippingAddress = db.StringProperty()

class PaymentReceiver(db.Model):
    pass

class ShoppingCart(db.Model):
    pass

class User(db.Model):
    name = db.StringProperty()
    address = db.StringProperty()
    phone = db.StringProperty()
    email = db.StringProperty()
    zipcode = db.StringProperty()
    password = db.StringProperty()
    code = db.StringProperty()
