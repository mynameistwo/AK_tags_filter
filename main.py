# import mysql.connector

units = {
    'Exusiai': ['Top Operator', 'Ranged', 'Sniper', 'DPS'],
    'SilverAsh': ['Top Operator', 'Melee', 'Guard', 'DPS', 'Support']
}
tagCount = 0
tags = []
while tagCount != 5:
    search = input('Enter tags here: ')
    tags.append(search)
    tagCount += 1
# for x in tags:
#    for keys in units.items():
#        if
