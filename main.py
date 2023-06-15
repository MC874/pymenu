import os
import re
import json
import datetime
from jsonmerge import merge

location = f'./foodie3.json'
export = f'{str(datetime.datetime.now().strftime("%Y%m%d"))}.json'

class colors:
	RED_BG = '\033[41m\033[1m'
	GREEN_BG = '\033[0;102m'
	PURPLE_BG = '\033[45m'
	GREEN = '\033[1;92m'
	ENDC = '\033[m'

def menu():
	line = 1
	total_price = 0
	hold_price = {}
	hold_item = {}
	selected_item = []
	with open(location, 'r') as file:
		json_content = json.load(file)
	for key, value in json_content.items():
		print(key)
		for key, value in value.items():
			print(f'{line}). {key}: [{colors.PURPLE_BG} {value} {colors.ENDC}]')
			hold_price[line] = value
			hold_item[line] = key
			line += 1
		print('')
	selected_menu = [int(x) for x in re.split(', |,| , | ,|; |;| ; | ;', input('Choose Menu: '))]
	for selection in selected_menu:
		total_price += hold_price[selection]
		item_name = hold_item[selection]
		if ']' in item_name:
			selected_item.append(re.search('\]\ ([a-zA-Z\ \&]*)$', item_name).group(1))
		else:
			selected_item.append(item_name)
	print(f'Total Price: {colors.GREEN_BG} {total_price} {colors.ENDC}')
	customer_price = int(input('Customer Price: ')) * 1000
	kembalian = customer_price - total_price
	print(f'Paybacks: {colors.RED_BG} {customer_price - total_price} {colors.ENDC}')
	profits = customer_price - kembalian
	print(f'Profits: {colors.GREEN_BG} {profits} {colors.ENDC}')
	print('')
	with open(export, 'r+') as file:
		json_content = json.load(file)
		file.seek(0)
		file.write(json.dumps(merge(json_content, {str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')):{'received': customer_price, 'given': kembalian, 'profits': profits, 'products': selected_item}}), sort_keys = True, indent = 4))

if os.path.isfile(export) is False:
	with open(export, 'w') as file:
		file.write('{}')
while True:	
	menu()