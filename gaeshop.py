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

application = webapp.WSGIApplication(
									[
									# URLs go here
									 ('/', Home),
									 ('/home', Home),
									 ('/.*', Home)
									],
									debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
