#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os
import urllib
from django.utils import simplejson as json

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.ext.db import Key

from models import *

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates/')

class Home(webapp.RequestHandler):
	def get(self):
		user = users.get_current_user()

		products = Product.all()

		param = {'user': user,
				 'isAdmin': users.is_current_user_admin(),
				 'loginURL': users.create_login_url("/"),
				 'logoutURL': users.create_logout_url("/"),
				 'products': products
				}

		self.response.out.write(template.render(TEMPLATES_DIR + "main.html", param))

class ViewCart(webapp.RequestHandler):
	def get(self):
		user = users.get_current_user()

		param = {'user': user,
				 'isAdmin': users.is_current_user_admin(),
				 'loginURL': users.create_login_url("/"),
				 'logoutURL': users.create_logout_url("/")
				}

		self.response.out.write(template.render(TEMPLATES_DIR + "cart.html", param))

class ViewProduct(webapp.RequestHandler):
	def get(self, productId):
		productId = urllib.unquote(urllib.unquote(productId))

		try:
			product = Product.get(Key(productId))
		except:
			product = None

		param = {'user': users.get_current_user(),
				 'isAdmin': users.is_current_user_admin(),
				 'loginURL': users.create_login_url("/"),
				 'logoutURL': users.create_logout_url("/"),
				 'product': product
				}

		self.response.out.write(template.render(TEMPLATES_DIR + "viewProduct.html", param))

class RegisterProduct(webapp.RequestHandler):
	def get(self):
		user = users.get_current_user()

		param = {'user': user,
				 'isAdmin': users.is_current_user_admin(),
				 'loginURL': users.create_login_url("/"),
				 'logoutURL': users.create_logout_url("/")
				}

		self.response.out.write(template.render(TEMPLATES_DIR + "registerProduct.html", param))

	def post(self):
		user = users.get_current_user()
		isAdmin = users.is_current_user_admin()

		retData = {"success": False, "message": "Not an Admin."}
		if isAdmin:
			data = json.loads(self.request.get("json"))
			if data and float(data["price"])>=0 and int(data["stock"])>=0:
				product = Product()
				product.create(data["name"], data["description"], float(data["price"]), int(data["stock"]))
				product.put()
				retData = {"success": True}
			else:
				retData["message"] = "Invalid values."

		return self.response.out.write(json.dumps(retData))

class RegisterCartItem(webapp.RequestHandler):
	def post(self):
		user = users.get_current_user()

		retData = {"success": False, "message": "Not logged in."}
		if user:
			data = json.loads(self.request.get("json"))
			if data:
				product = Product.get(Key(data["key"]))
				quantity = int(data["quantity"])

#				product = Product()
#				product.put()
				retData = {"success": True}
			else:
				retData["message"] = "Invalid values."

		return self.response.out.write(json.dumps(retData))

class Admin(webapp.RequestHandler):
	def get(self):
		user = users.get_current_user()
		isAdmin = users.is_current_user_admin()

		if isAdmin:
			param = {'user': user,
					 'isAdmin': isAdmin,
					 'loginURL': users.create_login_url("/"),
					 'logoutURL': users.create_logout_url("/")
					}

			self.response.out.write(template.render(TEMPLATES_DIR + "admin.html", param))

application = webapp.WSGIApplication(
									[
									# URLs go here
									 ('/', Home),
									 ('/view/cart', ViewCart),
									 ('/view/product/([^/]+)', ViewProduct),
									 ('/register/product', RegisterProduct),
									 ('/register/cart_item', RegisterCartItem),
									 ('/admin', Admin),
									 ('/.*', Home)
									],
									debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()