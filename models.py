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
		self.put()

class Order(db.Model):
	user = db.UserProperty()
	state = db.StringProperty()
	paymentMethod = db.StringProperty()
	shippingAddress = db.StringProperty()

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
