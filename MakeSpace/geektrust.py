import sys
from utils import initialize_meeting_rooms, parse_input, book_meeting_room, \
	find_vacant_room, check_interval_valid


def main():
	input_file = sys.argv[1]
	initialize_meeting_rooms()
	with open(input_file, 'r') as file:
		line = file.readline()
		while line:
			input_dict = parse_input(line)
			command = input_dict['command']
			start_time = input_dict['start_time']
			end_time = input_dict['end_time']
			if check_interval_valid(start_time, end_time):
				if command == 'BOOK':
					number_of_peoples = input_dict['number_of_peoples']
					book_meeting_room(start_time, end_time, number_of_peoples)
				elif command == 'VACANCY':
					find_vacant_room(start_time, end_time)
			else:
				print("INCORRECT_INPUT")
				
			line = file.readline()
	

if __name__ == "__main__":
	main()
