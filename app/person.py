from app.fellow import Fellow
from app.staff import Staff

class Person(Fellow,Staff):
	'''class inherits from Fellow and Staff and uses them to 
	   add a person, load people from a file and also relocate
	   people to various rooms
	'''
	def __init__(self):
		pass

	def add_person(self, person_name, type_person, type_room ='Office'):
		'''By default someone needs an Office 
		   Two people should never share a name
		'''
		pass

	def load_people(self, filename = 'people.txt'):
		pass

	def reallocate_person(self, person_id, room_name):
		pass

	def get_person_id(self, person_name):
		pass