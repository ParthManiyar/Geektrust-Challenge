from booking import Booking


class MeetingRoom:
	def __init__(self, room_name, capacity):
		self.room_name = room_name
		self.capacity = capacity
		self.bookings = []
	
	def vacant(self, start_time, end_time):
		for booking in self.bookings:
			if booking.overlap(start_time, end_time):
				return False
		return True
	
	def book(self, start_time, end_time):
		found_vacant = self.vacant(start_time, end_time)
		if found_vacant:
			booking = Booking(start_time, end_time)
			self.bookings.append(booking)
		return found_vacant
