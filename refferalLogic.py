
'''
Limit order = 0.5% == 0.005
Sniping = 1% == 0.01
Copy trade = 2% == 0.02
Уровни: 10%, 15%, 20%, 25%, 30%, 35%, 40%, 45%, 50%
'''

# Массив для итогового результата
lvlResult = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# Уровень пользователя
userLevel = ''
# Процент комиссии за тип операции
limitOrder, sniping, copyTrade = 0.005, 0.01, 0.02
# Уровни и сумма покупки
reffUserPercentLevel = [
    ['1', 1, 10, 20, 50, 100, 1000],
    ['2', 1, 10, 20, 50, 100, 1000],
    ['3', 1, 10, 20, 50, 100, 1000],
    ['4', 1, 10, 20, 50, 100, 1000],
    ['5', 1, 10, 20, 50, 100, 1000],
    ['6', 1, 10, 20, 50, 100, 1000],
    ['7', 1, 10, 20, 50, 100, 1000],
    ['8', 1, 10, 20, 50, 100, 1000],
    ['9', 1, 10, 20, 50, 100, 1000]
]

for i in reffUserPercentLevel[1:]:
    for j in i[1:]:
        userLevel = i[0]
        match userLevel:
            case '1':
                resultComission = round((j * limitOrder) * 0.1, 5)
                print(f'Уровень {userLevel}: ${resultComission}')
                lvlResult[0] += resultComission
            case '2':
                resultComission = round((j * limitOrder) * 0.15, 5)
                print(f'Уровень {userLevel}: ${resultComission}')
                lvlResult[1] += resultComission
            case '3':
                resultComission = round((j * limitOrder) * 0.2, 5)
                print(f'Уровень {userLevel}: ${resultComission}')
                lvlResult[2] += resultComission
            case '4':
                resultComission = round((j * limitOrder) * 0.25, 5)
                print(f'Уровень {userLevel}: ${resultComission}')
                lvlResult[3] += resultComission
            case '5':
                resultComission = round((j * limitOrder) * 0.3, 5)
                print(f'Уровень {userLevel}: ${resultComission}')
                lvlResult[4] += resultComission
            case '6':
                resultComission = round((j * limitOrder) * 0.35, 5)
                print(f'Уровень {userLevel}: ${resultComission}')
                lvlResult[5] += resultComission
            case '7':
                resultComission = round((j * limitOrder) * 0.4, 5)
                print(f'Уровень {userLevel}: ${resultComission}')
                lvlResult[6] += resultComission
            case '8':
                resultComission = round((j * limitOrder) * 0.45, 5)
                print(f'Уровень {userLevel}: ${resultComission}')
                lvlResult[7] += resultComission
            case '9':
                resultComission = round((j * limitOrder) * 0.5, 5)
                print(f'Уровень {userLevel}: ${resultComission}')
                lvlResult[8] += resultComission

# Общая сумма полученной рефералом награды за каждый уровень
print(*[f'Общая сумма комиссии за уровень: $' + str(i) for i in lvlResult], sep='\n')
