import re
import os
import json
import datetime
from jsonmerge import merge

class colors:
	RED_BG = '\033[41m\033[1m'
	GREEN_BG = '\033[0;102m'
	PURPLE_BG = '\033[45m'
	GREEN = '\033[1;92m'
	ENDC = '\033[m'

Pricy = []
Foody = []
location = f'./{str(datetime.datetime.now().strftime("%Y%m%d"))}.json'

allin = 0
num_file = 1

print('')
with open('foodie3.json') as f:
	data = json.load(f)
	for x, y in data.items():
		print(x)
		for key, value in data[x].items():
			Foody.append(key)
			Pricy.append(value)
			decim = value / 1000
			print(str(num_file) + ') ' + key + ': [' + colors.PURPLE_BG  + f' {value} ' + colors.ENDC + '] / [' + colors.PURPLE_BG + f' {decim} ' + colors.ENDC + ']')
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

if os.path.isfile(location) is False:
	with open(location, 'w') as f:
		f.write('{}')
with open(location, 'r+') as f:
	json_content = json.load(f)