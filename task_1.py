minutes = 0

string = '1h 45m,360s,25m,30m 120s,2h 60s'

parts = string.split(',')

for part in parts:
    units = part.split()

    for unit in units:
        if 'h' in unit:
            hours_string = unit.replace('h', '')

            hours = int(hours_string)

            hours_in_minutes = hours * 60

            minutes = minutes + hours_in_minutes

        elif 'm' in unit:
           
            minutes_string = unit.replace('m', '')

            current_minutes = int(minutes_string)

            minutes = minutes + current_minutes

        elif 's' in unit:

            seconds_string = unit.replace('s', '')

            seconds = int(seconds_string)

            seconds_in_minutes = seconds // 60

            minutes = minutes + seconds_in_minutes

print(minutes)

