
'''
Limit order = 0.5% == 0.005
Sniping = 1% == 0.01
Copy trade = 2% == 0.02
Уровни: 10%, 15%, 20%, 25%, 30%, 35%, 40%, 45%, 50%
'''

# Инициатор операции
buyer = []
userLvl = 0
line = 1
# Процент комиссии за тип операции
limitOrder, sniping, copyTrade = 0.005, 0.01, 0.02
# Тип операции
platformAction = ['limit order', 'sniping', 'copy trade']
# Юзер, уровень, сумма операции
userInfo = [
    [1, 5, 0], # 30%
    [2, 1, 0], # 10%
    [3, 3, 0], # 30%
    [4, 2, 0], # 15%
    [5, 1, 1],
    [6, 1, 0],
    [7, 1, 0],
    [8, 1, 0],
    [9, 1, 0]
]
# шаблон {уровень: комиссия}
levels = {
    1: 0.1,
    2: 0.15,
    3: 0.2,
    4: 0.25,
    5: 0.3,
    6: 0.35,
    7: 0.4,
    8: 0.45,
    9: 0.5
}

# выборка юзера, проводившего операцию
for i in userInfo[1:]:
    if i[2] > 0:
        buyer = i
        userLvl = i[1]
        break

# перевод массива в обратный порядок
userInfo.reverse()

# рассчет комиссии в лестничном порядке при реверсивном массиве
for i in userInfo:
    if i[0] < buyer[0]:
        if line == 1:
            line += 1
            print(f'Сумма реферальной награды за первую линию равна: ${round((buyer[2] * limitOrder) * levels[i[1]], 5)}')
        else:
            if userLvl >= i[1]: # если уровень
                continue
            else:
                print(f'Сумма реферальной награды для юзера {i[0]} равна: ${round((buyer[2] * limitOrder) * (levels[i[1]] - levels[buyer[1]]), 5)}')
