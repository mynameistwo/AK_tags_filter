# import mysql.connector
class TagFilterLoop:
    tagCount = 0
    tags = []
    while tagCount != 5:
        search = input('Enter tags here: ')
        tags.append(search)
        tagCount += 1
    for filter in tags:
        print(filter)


class TagLoop:
    units = {
        'Exusiai': ['Top Operator', 'Ranged', 'Sniper', 'DPS'],
        'SilverAsh': ['Top Operator', 'Melee', 'Guard', 'DPS', 'Support']
    }
    for operators in units:
        for affix in units[operators]:
            print(affix)
