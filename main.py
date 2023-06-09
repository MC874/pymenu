import json
import re

class colors:
	RED_BG = '\033[41m\033[1m'
	GREEN_BG = '\033[0;102m'
	GREEN = '\033[1;92m'
	ENDC = '\033[m'

Pricy = []
Foody = []

allin = 0
num_file = 1

kali = '*'

with open('foodie.json') as f:
	data = json.load(f)
	for key, value in data.items():
		Foody.append(key)
		Pricy.append(value)
		print(str(num_file) + ') ' + key + ': ' + str(value))
		num_file = num_file + 1
print('')
ask = input(' Pilih Menu: ')
result = [str(x) for x in re.split(', |,| , | ,|; |;| ; | ;', ask)]
for i in result:
	if re.search('\*', i):
		result = [int(x) for x in re.split('\*| \*| \* |\* ', i)]
		allin = allin + Pricy[result[0]-1] * result[1]
	else:
		allin = allin + Pricy[int(i)-1]
print('Total Harga: ' + colors.GREEN_BG + f' {str(allin)} ' + colors.ENDC )
print()
umoney = input(' Uang Pelanggan: ')
if int(umoney) < 999:
	kembalian = int(umoney) * 1000 - int(allin)
else:
	kembalian = int(umoney) - int(allin)
kembali = int(kembalian) / 1000
print('Kembalian: '+ colors.RED_BG + f' {str(kembalian)} ' + colors.ENDC + ' / ' + colors.RED_BG + f' {str(kembali)} ' + colors.ENDC)