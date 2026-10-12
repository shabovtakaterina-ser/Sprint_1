minutes = 0

string = '1h 45m,360s,25m,30m 120s,2h 60s'

parts = string.split(',')

for part in parts:
    units = part.split()

    for unit in units:
        if 'h' in unit:
            # Удаляем символ h.
            hours_string = unit.replace('h', '')

            # Преобразуем строку в целое число.
            hours = int(hours_string)

            # Переводим часы в минуты.
            hours_in_minutes = hours * 60

            # Добавляем полученные минуты к общей сумме.
            minutes = minutes + hours_in_minutes

        elif 'm' in unit:
            # Удаляем символ m.
            minutes_string = unit.replace('m', '')

            # Преобразуем строку в целое число.
            current_minutes = int(minutes_string)

            # Добавляем минуты к общей сумме.
            minutes = minutes + current_minutes

        elif 's' in unit:
            # Удаляем символ s.
            seconds_string = unit.replace('s', '')

            # Преобразуем строку в целое число.
            seconds = int(seconds_string)

            # Переводим секунды в минуты.
            seconds_in_minutes = seconds // 60

            # Добавляем полученные минуты к общей сумме.
            minutes = minutes + seconds_in_minutes

print(minutes)

