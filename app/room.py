from app.livingspace import LivingSpace 
from app.office import Office 

class Room(LivingSpace, Office):
	def __init__(self):
		pass

	def create_room(self, room_name, room_type):
		pass

	def print_allocations(self, filename):
		pass

	def print_unallocated(self, filename):
		pass

	def print_room(self, room_name):
		pass