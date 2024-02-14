def first(date1, date2):
    date1 = list(map(int, date1.split('-')))
    date2 = list(map(int, date2.split('-')))
    if date1[0] < date2[0]:
        return True
    if date1[0] > date2[0]:
        return False
    if date1[1] < date2[1]:
        return True
    if date1[1] > date2[1]:
        return False
    if date1[2] < date2[2]:
        return True
    if date1[2] > date2[2]:
        return False
    return False
with open('scientist.txt') as file:
    answer = []
    scientist_origin = {}
    file.readline()
    for i in file:
        scientistName, preparation, date, components = i.split('#')
        scientist = [scientistName, preparation, date, components]
        if preparation == 'Аллопуринол':
            answer.append([scientistName,date])
        if not(first(scientist_origin.get(preparation, scientist)[2], date)):
            scientist_origin[preparation] = scientist
for i in range(len(answer)):
    for j in range(len(answer)-1):
        if first(answer[j + 1][1], answer[j][1]):
            answer[j + 1], answer[j] = answer[j], answer[j + 1]
print("Разработчиками Аллопуринола были такие люди (результаты выведите в порядке возрастания даты):")
for i in answer:
    print(i[0] + ' - ' + i[1])
print(f'Оригинальный рецепт принадлежит: {scientist_origin["Аллопуринол"][0]}')
scientist_origin = list(scientist_origin.values())
for i in range(len(scientist_origin)):
    for j in range(len(scientist_origin)-1):
        if first(scientist_origin[j + 1][2], scientist_origin[j][2]):
            scientist_origin[j + 1], scientist_origin[j] = scientist_origin[j], scientist_origin[j + 1]
with open('scientist_origin.txt', 'w') as file:
    file.write('ScientistName#preparation#date#components\n')
    for i in scientist_origin:
        file.write('#'.join(i))





