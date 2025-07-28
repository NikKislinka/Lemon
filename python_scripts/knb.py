import random
opt = ['камень', 'ножницы', 'бумага']
win = {
        'камень': 'ножницы',
        'ножницы': 'бумага',
        'бумага': 'камень'
}
while True:
    u = input('выбери камень/ножницы/бумага/выход: ').lower()
    if u == 'выход':
        break
    elif u in opt:
        comp = random.choice(opt)
    else:
        print('неверный ход')
        continue
    print(f'вы: {u}\nкомп: {comp}')
    if u == comp:
        print('ничья')
    elif win[u] == comp:
        print('победа')
    else:
        print('проигрыш')
