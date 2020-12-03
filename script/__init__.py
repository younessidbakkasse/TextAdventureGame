import json

def add_time(start, duration, day = ''):
    day_time, day_half = start.split() 
    start_hour, start_minute = day_time.split(':') 
    add_hour, add_minute = duration.split(':')

    minutes_to_hours = 0

    result_minute = int(start_minute) + int(add_minute)

    while result_minute >= 60:
        minutes_to_hours += 1
        result_minute -= 60
    
    result_hour = int(start_hour) + int(add_hour) + minutes_to_hours

    # changing houres
    while result_hour >= 12:
        if result_hour >= 12 and day_half == 'AM':
            day_half = 'PM'
            if result_hour > 12:
                result_hour -= 12
        elif result_hour >= 12 and day_half == 'PM':
            result_hour -= 12
            day_half = 'AM'

    #adding 0 to hours and minutes if there below 10
    if result_hour < 10:
        result_hour = '0' + str(result_hour)
    if result_minute < 10:
        result_minute = '0' + str(result_minute)
    
    new_time = f'{result_hour}:{result_minute} {day_half}'

    return new_time

 
 
# print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday
 
# print(add_time("11:43 PM", "24:20", "tueSday"))
# # Returns: 12:03 AM, Thursday (2 days later)
 
# print(add_time("6:30 PM", "205:12"))
# # Returns: 7:42 AM (9 days later)

with open('./assets/data/file.json') as file:
    data = json.load(file)


for person in data['people']:
    print(person['email'])
