from google.appengine.ext import db

class Product(db.Model):
	name = db.StringProperty()
	description = db.StringProperty()
	price = db.FloatProperty()
	stock = db.IntegerProperty()
	views = db.IntegerProperty()

	def create(self, name, description, price, stock):
		self.name = name
		self.description = description
		self.price = price
		self.stock = stock
		self.views = 0

	def getStock(self):
		return self.stock

	def match(self, search):
		return True

	def addView(self):
		self.views += 1

class Order(db.Model):
	user = db.UserProperty()
	state = db.StringProperty()
	paymentMethod = db.StringProperty()
	shippingAddress = db.StringProperty()

class PaymentReceiver(db.Model):
	pass

class ShoppingCart(db.Model):
	def addProduct(self, product): 
		return True

	def getProducts(self):
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

	def addOrder(self, paymentMethod, shippingAddress):
		return True