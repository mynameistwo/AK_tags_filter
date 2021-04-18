def remove_duplicates(x):
    return list(dict.fromkeys(x))


units = {
    'Exusiai': ['Top Operator', 'Ranged', 'Sniper', 'DPS'],
    'SilverAsh': ['Top Operator', 'Melee', 'Guard', 'DPS', 'Support']
}
tagCount = 0
tags = []
results = []

while tagCount != 5:
    search = input('Enter tags here: ')
    tags.append(search)
    tagCount += 1

for operators in units:
    for affix in units[operators]:
        for filter in tags:
            if affix.lower() == filter:
                results.append(operators)

print(remove_duplicates(results))
