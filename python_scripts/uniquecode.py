import random
import os
def add(code):
	with open('logcodes.txt', 'a', encoding='utf-8') as f:
		f.write(f'{code}\n')
def search(codefind, filename='logcodes.txt'): 
	found = False
	if os.path.exists(filename):
		with open(filename,'r', encoding='utf-8') as f:
			for line in f:
				if line.strip() == codefind:
					found = True
					break
	return found
ulen=int(input('Длина кодов: '))
alph16 = '0123456789abcdef'
while True:
	if input() == 'clear':
		os.remove('logcodes.txt')
	else:
		gencode=''
		for _ in alph16:
			if len(gencode) < ulen:
				gencode += random.choice(alph16)
		if search(gencode):
			continue
		print(gencode)
		add(gencode)
