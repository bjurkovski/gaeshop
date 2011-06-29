from google.appengine.ext import db

class ShippingCalculator:
	def compute(self, address):
		return 15.00

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
		words = search.lower().split(" ")
		myWords = self.name.lower().split(" ")
		myWords.extend(self.description.lower().split(" "))
		for mw in myWords:
			if mw in words:
				return True
		return False

	def addView(self):
		self.views += 1
		self.put()

class Order(db.Model):
	user = db.UserProperty()
	paymentMethod = db.StringProperty()
	shippingAddress = db.StringProperty()
	state = db.StringProperty()
	
	def getShipping(self):
		sc = ShippingCalculator()
		value = sc.compute(self.shippingAddress)
		return "R$ %0.2f" % (value)

	def getState(self):
		strings = { 'wait' : 'Em espera', 'paid' : 'Pago', 'canceled' : 'Cancelado'}
		
		return strings[self.state]

	def getPaymentMethod(self):
		strings = { 'card' : 'Cartao de Credito', 'billet' : 'Boleto Bancario', 'paypal' : 'PayPal'}
		
		return strings[self.paymentMethod]

	def create(self,user,paymentMethod=None,shippingAddress=None,state='wait'):
		self.user = user
		self.paymentMethod = paymentMethod
		self.shippingAddress = shippingAddress
		self.state = state

	def addItem(self,product,quantity):
		item = OrderItem()
		item.product = product
		item.quantity = quantity
		item.orderCode = self
		item.put()

class OrderItem(db.Model):

	product = db.ReferenceProperty(Product)
	quantity = db.IntegerProperty()
	orderCode = db.ReferenceProperty()


class PaymentReceiver(db.Model):
	pass

class CartItem(db.Model):

	user = db.UserProperty()
	product = db.ReferenceProperty(Product)
	quantity = db.IntegerProperty()

	def totalPrice(self):
		return self.product.price*self.quantity

	def create(self,user,product,quantity):
		if quantity == 0:
			return False

		alreadyAdded = False
		for item in CartItem.all().filter('user =', user):
			if item.product.key() == product.key():
				item.quantity += quantity
				item.put()
				alreadyAdded = True

		if not alreadyAdded:
			item = CartItem()
			item.product = product
			item.quantity = quantity
			item.user = user
			item.put()

		return True


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
