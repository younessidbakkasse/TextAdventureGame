def add_time(start, duration, current_day = ''):
    day_time, day_half = start.split() 
    start_hour, start_minute = day_time.split(':') 
    add_hour, add_minute = duration.split(':')

    days = 0
    minutes_to_hours = 0
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    current_day_i = None

    result_minute = int(start_minute) + int(add_minute)

    while result_minute >= 60:
        minutes_to_hours += 1
        result_minute -= 60
    
    result_hour = int(start_hour) + int(add_hour) + minutes_to_hours
    # days = result_hour // 24
    # changing houres
    while result_hour >= 12: 
        if result_hour >= 12 and day_half == 'AM':
            day_half = 'PM'
            if result_hour == 12:
                break 
            result_hour -= 12
        elif result_hour >= 12 and day_half == 'PM':
            day_half = 'AM'
            days += 1
            if result_hour == 12:
                break 
            result_hour -= 12 
    #adding 0 to minutes if there below 10
    if result_minute < 10:
        result_minute = '0' + str(result_minute)
    
    new_time = f'{result_hour}:{result_minute} {day_half}'
    if current_day:
        for i, day in enumerate(week):
            if day == current_day.capitalize():
                current_day_i = i
        if days == 0:
            new_time += f', {week[current_day_i]}'
        elif days == 1:
            new_time += f', {week[current_day_i + 1]} (next day)'
        
        elif days > 1:
            print(current_day_i)
            try:
                new_time += f', {week[current_day_i + days % 7]} ({days} days later)'
            except:
                new_time += f', {week[current_day_i - 1]} ({days} days later)'
    else:
        if days == 1:
            new_time += ' (next day)'
        elif days > 1:
            new_time += f' ({days} days later)'
        
    print(new_time) 
 
add_time("8:16 PM", "466:02", "tuesday")
# # 6:18 AM, Monday (20 days later)
 
# add_time("3:30 PM", "2:12")
# 5:42 PM

# add_time("11:55 AM", "3:12")
# # 3:07 PM

# add_time("9:15 PM", "5:30")
# # 2:45 AM (next day)

# add_time("11:40 AM", "0:25")
# # 12:05 PM

# add_time("2:59 AM", "24:00")
# # 2:59 AM (next day)

# add_time("11:59 PM", "24:05")
# # 12:04 AM (2 days later)

# add_time("8:16 PM", "466:02")
# # 6:18 AM (20 days later)

# add_time("5:01 AM", "0:00")
# # 5:01 AM

# add_time("3:30 PM", "2:12", "Monday")
# # 5:42 PM, Monday

# add_time("2:59 AM", "24:00", "saturDay")
# # 2:59 AM, Sunday (next day)

# add_time("11:59 PM", "24:05", "Wednesday")
# # 12:04 AM, Friday (2 days later)


