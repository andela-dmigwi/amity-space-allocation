from app.fellow import Fellow
from app.staff import Staff

class Person(Fellow,Staff):
	def __init__(self):
		pass

	def add_person(self, person_id, type_person, wants_accomodation):
		pass

	def load_people(self):
		pass

	def reallocate_person(self, person_id, room_name):
		pass