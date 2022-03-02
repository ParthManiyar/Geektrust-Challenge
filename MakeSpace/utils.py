from meeting_room import MeetingRoom
from datetime import time
FIFTEEN_MINUTE_INTERVAL = 15
room_details = [
    {'name': 'C-Cave', 'capacity': 3},
    {'name': 'D-Tower', 'capacity': 7},
    {'name': 'G-Mansion', 'capacity': 20}
]

buffer_intervals = [
    {'start_time': time(9, 0, 0), 'end_time': time(9, 15, 0)},
    {'start_time': time(13, 15, 0), 'end_time': time(13, 45, 0)},
    {'start_time': time(18, 45, 0), 'end_time': time(19, 0, 0)}
]
meeting_rooms = []


def check_fifteen_minute_interval(interval_time):
    return (interval_time.minute % FIFTEEN_MINUTE_INTERVAL) == 0


def check_interval_valid(start_time, end_time):
    return end_time > start_time \
            and check_fifteen_minute_interval(start_time)\
            and check_fifteen_minute_interval(end_time)


def add_buffer_times(meeting_room):
    for buffer_time in buffer_intervals:
        meeting_room.book(buffer_time['start_time'], buffer_time['end_time'])


def create_meeting_room(name, capacity):
    meeting_room = MeetingRoom(name, capacity)
    return meeting_room


def initialize_meeting_rooms():
    for room_detail in room_details:
        meeting_room = create_meeting_room(room_detail['name'],
                                           room_detail['capacity'])
        add_buffer_times(meeting_room)
        meeting_rooms.append(meeting_room)
    return meeting_rooms


def parse_input(line):
    line = line.split(' ')
    start_hour, start_minute = (map(int, line[1].split(':')))
    end_hour, end_minute = map(int, line[2].split(':'))
    input_dict = {
        'command': line[0],
        'start_time': time(start_hour, start_minute, 0),
        'end_time': time(end_hour, end_minute, 0),
    }
    if input_dict['command'] == 'BOOK':
        input_dict['number_of_peoples'] = int(line[3])

    return input_dict


def check_capacity(meeting_room, number_of_peoples):
    return meeting_room.capacity >= number_of_peoples


def book_meeting_room(start_time, end_time, number_of_peoples):
    for meeting_room in meeting_rooms:
        if check_capacity(meeting_room, number_of_peoples):
            booked = meeting_room.book(start_time, end_time)
            if booked:
                print(meeting_room.room_name)
                return
    print('NO_VACANT_ROOM')


def find_vacant_room(start_time, end_time):
    vacant_rooms = []
    for meeting_room in meeting_rooms:
        vacant = meeting_room.vacant(start_time, end_time)
        if vacant:
            vacant_rooms.append(meeting_room.room_name)

    if len(vacant_rooms) == 0:
        print('NO_VACANT_ROOM')
    else:
        print(' '.join(vacant_rooms))
