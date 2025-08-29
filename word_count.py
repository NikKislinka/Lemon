def cnt(usin):
    usin = usin.lower()
    puncts = '.,!?;:'
    for ch in puncts:
        usin = usin.replace(ch, ' ')
    words = usin.split()
    wcount = {}
    for w in words:
        wcount[w] = wcount.get(w, 0)+1
    wsort = sorted(wcount.items(), key=lambda item: item[1], reverse=True)
    print('\nТоп 3 частых слов: ')
    for i, (w, c) in enumerate(wsort[:3]):
        print(f'{i+1}. {w} {c} раз')

while True:
    usin = input('Введите текст: ')
    if usin=='':
        print('Пустой ввод.')
    else:
        cnt(usin)
