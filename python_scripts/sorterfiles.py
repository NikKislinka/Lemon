import os

if not os.path.exists('txts'):
    os.mkdir('txts')
if not os.path.exists('imgs'):
    os.mkdir('imgs')
for f in (files := os.listdir(".")):
    if os.path.isfile(f):
        if f.endswith('.txt'):
            os.rename(f, (os.path.join('txts', f)))
        elif f.endswith('.jpg'):
            os.rename(f, (os.path.join('imgs', f)))
