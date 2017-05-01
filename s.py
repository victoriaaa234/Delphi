seconds = 192
for second in range(int(seconds)):
    minutes = int(second / 60)
    hours = int(minutes / 60)
    hours_str = str(hours)
    minutes_str = str(minutes)
    seconds_str = str(second % 60)
    print(second % 60)
    if second % 60 < 10:
        print('uip')
        seconds_str = '0' + str(second % 60)
    if minutes < 10:
        minutes_str = '0' + str(minutes)
    if hours < 10:
        hours_str = '0' + str(hours)
    print('min ' + minutes_str)
    print('hour ' + hours_str)
    print('seconds ' + seconds_str)
    print (hours_str + minutes_str + seconds_str)