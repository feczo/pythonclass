days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday']

for day in days:
    for hour in range(1, 24):
        if not(day == 'Monday' or hour == 12):
            print "%s %d" % (day, hour)
