#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from models import *

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates/')

class Home(webapp.RequestHandler):
	def get(self):
		user = users.get_current_user()

		param = {'user': user,
				 'isAdmin': users.is_current_user_admin(),
				 'loginURL': users.create_login_url("/"),
				 'logoutURL': users.create_logout_url("/")
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
		productId = urllib.unquote(urllib.unquote(kind))

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
		return

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
									 ('/admin', Admin),
									 ('/.*', Home)
									],
									debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
