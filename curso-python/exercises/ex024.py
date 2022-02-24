city = str(input('Em que cidade você nasceu? ')).strip().title()

# list_city = city.split()
# print(list_city)
#
# if list_city[0] == 'Santo':
#     print(True)

print(city.find('Santo') == 0)
print(city[0:5] == 'Santo')
