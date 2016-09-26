from app.livingspace import LivingSpace 
from app.office import Office 

class Room(LivingSpace, Office):
	'''Class inherits LivingSpace and Office properties and uses them to
	   create a room, obtain allocated & unallocated rooms and also
	   occupants of a room
	   '''
	def __init__(self):
		pass

	def create_room(self, room_name, room_type):
		pass

	# def get_allocations(self, filename=''):
	def get_allocations(self):
		pass

	# def get_unallocated(self, filename):
	def get_unallocated(self):
		pass

	def get_room(self, room_name):
		pass