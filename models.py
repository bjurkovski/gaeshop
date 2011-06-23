from google.appengine.ext import db

class A_Model(db.Model):
	userExample = db.UserProperty()
	boolExample = db.BooleanProperty()
	stringExample = db.StringProperty()

class Another_Model(db.Model):
	pointerExample = db.ReferenceProperty(A_Model)
	integerExample = db.IntegerProperty()
	listExample = db.ListProperty(db.Key)
