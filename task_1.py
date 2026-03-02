time_data = '1h 45m,360s,25m,30m 120s,2h 60s'

total_minutes = 0

time_lst = time_data.split(',')

for lst in time_lst:
    minute = 0
    meanings = lst.split()
    for meaning in meanings:
        if 'h' in meaning:
            hour = int(meaning.replace('h', ''))
            minute += hour * 60
        elif 'm' in meaning:
            minutes = int(meaning.replace('m', ''))
            minute += minutes
        elif 's' in meaning:
            sec = int(meaning.replace('s', ''))
            minute += sec // 60
    total_minutes += minute

print("Общее количество минут", + total_minutes)