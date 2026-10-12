world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
    2022: 'Аргентина'
}

for year, champion in world_champions.items():
     print(f'{year} - {champion}')
country = 'Италия'

# Проверяем, есть ли страна среди всех значений словаря
if country in world_champions.values():
    print(f'{country} становилась чемпионом мира по футболу в 21 веке!')
else:
    print(f'{country} не выигрывала чемпионат мира по футболу в 21 веке.')