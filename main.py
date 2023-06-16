import os
import sys
import glob
import json
import datetime
from jsonmerge import merge, Merger
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit, QVBoxLayout, QMainWindow, QScrollArea
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt

location = f"./{str(datetime.datetime.now().strftime('%Y%m%d'))}.json"

def resource_path(relative_path):
	base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
	return os.path.join(base_path, relative_path)

def frostbite_templates():
	global choco_lava_mochi_label, strawberry_sakura_mochi_label, cookies_cream_mochi_label, vita_fruit_label, boba_milk_tea_label, strawberry_vanilla_label, tutti_frutti_label, chocolate_vanilla_label, cookies_cream_stick_label, choco_cashew_label, crunchy_double_choco_label

	def choco_lava_mochi_submit():
		if controllers['current_products'].get('Choco Lava Mochi') is not None:
			controllers['current_products']['Choco Lava Mochi'] += 1
		else:
			controllers['current_products']['Choco Lava Mochi'] = 1
			
		choco_lava_mochi_label.setText(str(controllers['current_products']['Choco Lava Mochi']))
		controllers['current_prices'] += 4000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	def strawberry_sakura_mochi_submit():
		if controllers['current_products'].get('Strawberry Sakura Mochi') is not None:
			controllers['current_products']['Strawberry Sakura Mochi'] += 1
		else:
			controllers['current_products']['Strawberry Sakura Mochi'] = 1
			
		strawberry_sakura_mochi_label.setText(str(controllers['current_products']['Strawberry Sakura Mochi']))
		controllers['current_prices'] += 4000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	def cookies_cream_mochi_submit():
		if controllers['current_products'].get('Cookies & Cream Mochi') is not None:
			controllers['current_products']['Cookies & Cream Mochi'] += 1
		else:
			controllers['current_products']['Cookies & Cream Mochi'] = 1
			
		cookies_cream_mochi_label.setText(str(controllers['current_products']['Cookies & Cream Mochi']))
		controllers['current_prices'] += 4000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	def vita_fruit_submit():
		if controllers['current_products'].get('Vita Fruit') is not None:
			controllers['current_products']['Vita Fruit'] += 1
		else:
			controllers['current_products']['Vita Fruit'] = 1
			
		vita_fruit_label.setText(str(controllers['current_products']['Vita Fruit']))
		controllers['current_prices'] += 4000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	choco_lava_mochi_layout = QVBoxLayout()
	choco_lava_mochi_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	choco_lava_mochi_button = QPushButton()
	choco_lava_mochi_label = QLabel()
	choco_lava_mochi_button.setFixedSize(100, 100)
	choco_lava_mochi_button.setIcon(QIcon('./img/frostbite/frostbite_mochi_choco_lava.jpg'))
	choco_lava_mochi_button.setIconSize(QSize(110, 110))
	choco_lava_mochi_button.clicked.connect(choco_lava_mochi_submit)
	choco_lava_mochi_layout.addWidget(choco_lava_mochi_button, alignment=Qt.AlignmentFlag.AlignCenter)
	choco_lava_mochi_layout.addWidget(choco_lava_mochi_label, alignment=Qt.AlignmentFlag.AlignCenter)

	strawberry_sakura_mochi_layout = QVBoxLayout()
	strawberry_sakura_mochi_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	strawberry_sakura_mochi_button = QPushButton()
	strawberry_sakura_mochi_label = QLabel()
	strawberry_sakura_mochi_button.setFixedSize(100, 100)
	strawberry_sakura_mochi_button.setIcon(QIcon('./img/frostbite/frostbite_mochi_strawberry_sakura.jpg'))
	strawberry_sakura_mochi_button.setIconSize(QSize(110, 110))
	strawberry_sakura_mochi_button.clicked.connect(strawberry_sakura_mochi_submit)
	strawberry_sakura_mochi_layout.addWidget(strawberry_sakura_mochi_button, alignment=Qt.AlignmentFlag.AlignCenter)
	strawberry_sakura_mochi_layout.addWidget(strawberry_sakura_mochi_label, alignment=Qt.AlignmentFlag.AlignCenter)

	cookies_cream_mochi_layout = QVBoxLayout()
	cookies_cream_mochi_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	cookies_cream_mochi_button = QPushButton()
	cookies_cream_mochi_label = QLabel()
	cookies_cream_mochi_button.setFixedSize(100, 100)
	cookies_cream_mochi_button.setIcon(QIcon('./img/frostbite/frostbite_mochi_cookies_cream.jpg'))
	cookies_cream_mochi_button.setIconSize(QSize(110, 110))
	cookies_cream_mochi_button.clicked.connect(cookies_cream_mochi_submit)
	cookies_cream_mochi_layout.addWidget(cookies_cream_mochi_button, alignment=Qt.AlignmentFlag.AlignCenter)
	cookies_cream_mochi_layout.addWidget(cookies_cream_mochi_label, alignment=Qt.AlignmentFlag.AlignCenter)

	vita_fruit_layout = QVBoxLayout()
	vita_fruit_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	vita_fruit_button = QPushButton()
	vita_fruit_label = QLabel()
	vita_fruit_button.setFixedSize(100, 100)
	vita_fruit_button.setIcon(QIcon('./img/frostbite/frostbite_vita_fruit.jpg'))
	vita_fruit_button.setIconSize(QSize(110, 110))
	vita_fruit_button.clicked.connect(vita_fruit_submit)
	vita_fruit_layout.addWidget(vita_fruit_button, alignment=Qt.AlignmentFlag.AlignCenter)
	vita_fruit_layout.addWidget(vita_fruit_label, alignment=Qt.AlignmentFlag.AlignCenter)

	frostbite_layout1 = QHBoxLayout()
	frostbite_layout1.setAlignment(Qt.AlignmentFlag.AlignLeft)
	frostbite_layout1.addLayout(choco_lava_mochi_layout)
	frostbite_layout1.addLayout(strawberry_sakura_mochi_layout)
	frostbite_layout1.addLayout(cookies_cream_mochi_layout)
	frostbite_layout1.addLayout(vita_fruit_layout)

	def chocolate_vanilla_submit():
		if controllers['current_products'].get('Chocolate Vanilla') is not None:
			controllers['current_products']['Chocolate Vanilla'] += 1
		else:
			controllers['current_products']['Chocolate Vanilla'] = 1
			
		chocolate_vanilla_label.setText(str(controllers['current_products']['Chocolate Vanilla']))
		controllers['current_prices'] += 5500
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	def strawberry_vanilla_submit():
		if controllers['current_products'].get('Strawberry Vanilla') is not None:
			controllers['current_products']['Strawberry Vanilla'] += 1
		else:
			controllers['current_products']['Strawberry Vanilla'] = 1
			
		strawberry_vanilla_label.setText(str(controllers['current_products']['Strawberry Vanilla']))
		controllers['current_prices'] += 5500
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	def tutti_frutti_submit():
		if controllers['current_products'].get('Tutti Frutti') is not None:
			controllers['current_products']['Tutti Frutti'] += 1
		else:
			controllers['current_products']['Tutti Frutti'] = 1
			
		tutti_frutti_label.setText(str(controllers['current_products']['Tutti Frutti']))
		controllers['current_prices'] += 5500
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	def boba_milk_tea_submit():
		if controllers['current_products'].get('Boba Milk Tea') is not None:
			controllers['current_products']['Boba Milk Tea'] += 1
		else:
			controllers['current_products']['Boba Milk Tea'] = 1
			
		boba_milk_tea_label.setText(str(controllers['current_products']['Boba Milk Tea']))
		controllers['current_prices'] += 5000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	chocolate_vanilla_layout = QVBoxLayout()
	chocolate_vanilla_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	chocolate_vanilla_button = QPushButton()
	chocolate_vanilla_label = QLabel()
	chocolate_vanilla_button.setFixedSize(100, 100)
	chocolate_vanilla_button.setIcon(QIcon('./img/frostbite/frostbite_cup_chocolate_vanilla.jpg'))
	chocolate_vanilla_button.setIconSize(QSize(110, 110))
	chocolate_vanilla_button.clicked.connect(chocolate_vanilla_submit)
	chocolate_vanilla_layout.addWidget(chocolate_vanilla_button, alignment=Qt.AlignmentFlag.AlignCenter)
	chocolate_vanilla_layout.addWidget(chocolate_vanilla_label, alignment=Qt.AlignmentFlag.AlignCenter)

	strawberry_vanilla_layout = QVBoxLayout()
	strawberry_vanilla_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	strawberry_vanilla_button = QPushButton()
	strawberry_vanilla_label = QLabel()
	strawberry_vanilla_button.setFixedSize(100, 100)
	strawberry_vanilla_button.setIcon(QIcon('./img/frostbite/frostbite_cup_strawberry_vanilla.jpg'))
	strawberry_vanilla_button.setIconSize(QSize(110, 110))
	strawberry_vanilla_button.clicked.connect(strawberry_vanilla_submit)
	strawberry_vanilla_layout.addWidget(strawberry_vanilla_button, alignment=Qt.AlignmentFlag.AlignCenter)
	strawberry_vanilla_layout.addWidget(strawberry_vanilla_label, alignment=Qt.AlignmentFlag.AlignCenter)

	tutti_frutti_layout = QVBoxLayout()
	tutti_frutti_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	tutti_frutti_button = QPushButton()
	tutti_frutti_label = QLabel()
	tutti_frutti_button.setFixedSize(100, 100)
	tutti_frutti_button.setIcon(QIcon('./img/frostbite/frostbite_cup_tutti_frutti.jpg'))
	tutti_frutti_button.setIconSize(QSize(110, 110))
	tutti_frutti_button.clicked.connect(tutti_frutti_submit)
	tutti_frutti_layout.addWidget(tutti_frutti_button, alignment=Qt.AlignmentFlag.AlignCenter)
	tutti_frutti_layout.addWidget(tutti_frutti_label, alignment=Qt.AlignmentFlag.AlignCenter)

	boba_milk_tea_layout = QVBoxLayout()
	boba_milk_tea_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	boba_milk_tea_button = QPushButton()
	boba_milk_tea_label = QLabel()
	boba_milk_tea_button.setFixedSize(100, 100)
	boba_milk_tea_button.setIcon(QIcon('./img/frostbite/frostbite_boba_milk_tea.jpg'))
	boba_milk_tea_button.setIconSize(QSize(110, 110))
	boba_milk_tea_button.clicked.connect(boba_milk_tea_submit)
	boba_milk_tea_layout.addWidget(boba_milk_tea_button, alignment=Qt.AlignmentFlag.AlignCenter)
	boba_milk_tea_layout.addWidget(boba_milk_tea_label, alignment=Qt.AlignmentFlag.AlignCenter)

	frostbite_layout2 = QHBoxLayout()
	frostbite_layout2.setAlignment(Qt.AlignmentFlag.AlignLeft)
	frostbite_layout2.addLayout(chocolate_vanilla_layout)
	frostbite_layout2.addLayout(strawberry_vanilla_layout)
	frostbite_layout2.addLayout(tutti_frutti_layout)
	frostbite_layout2.addLayout(boba_milk_tea_layout)

	def cookies_cream_stick_submit():
		if controllers['current_products'].get('Cookies & Cream Stick') is not None:
			controllers['current_products']['Cookies & Cream Stick'] += 1
		else:
			controllers['current_products']['Cookies & Cream Stick'] = 1
			
		cookies_cream_stick_label.setText(str(controllers['current_products']['Cookies & Cream Stick']))
		controllers['current_prices'] += 6000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	def choco_cashew_submit():
		if controllers['current_products'].get('Choco Nut & Cashew') is not None:
			controllers['current_products']['Choco Nut & Cashew'] += 1
		else:
			controllers['current_products']['Choco Nut & Cashew'] = 1
			
		choco_cashew_label.setText(str(controllers['current_products']['Choco Nut & Cashew']))
		controllers['current_prices'] += 6000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	def crunchy_double_choco_submit():
		if controllers['current_products'].get('Cruncy Double Choco') is not None:
			controllers['current_products']['Cruncy Double Choco'] += 1
		else:
			controllers['current_products']['Cruncy Double Choco'] = 1
			
		crunchy_double_choco_label.setText(str(controllers['current_products']['Cruncy Double Choco']))
		controllers['current_prices'] += 6000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	cookies_cream_stick_layout = QVBoxLayout()
	cookies_cream_stick_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	cookies_cream_stick_button = QPushButton()
	cookies_cream_stick_label = QLabel()
	cookies_cream_stick_button.setFixedSize(100, 100)
	cookies_cream_stick_button.setIcon(QIcon('./img/frostbite/frostbite_cookies_cream_stick.jpg'))
	cookies_cream_stick_button.setIconSize(QSize(110, 110))
	cookies_cream_stick_button.clicked.connect(cookies_cream_stick_submit)
	cookies_cream_stick_layout.addWidget(cookies_cream_stick_button, alignment=Qt.AlignmentFlag.AlignCenter)
	cookies_cream_stick_layout.addWidget(cookies_cream_stick_label, alignment=Qt.AlignmentFlag.AlignCenter)

	choco_cashew_layout = QVBoxLayout()
	choco_cashew_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	choco_cashew_button = QPushButton()
	choco_cashew_label = QLabel()
	choco_cashew_button.setFixedSize(100, 100)
	choco_cashew_button.setIcon(QIcon('./img/frostbite/frostbite_choco_cashew.jpg'))
	choco_cashew_button.setIconSize(QSize(110, 110))
	choco_cashew_button.clicked.connect(choco_cashew_submit)
	choco_cashew_layout.addWidget(choco_cashew_button, alignment=Qt.AlignmentFlag.AlignCenter)
	choco_cashew_layout.addWidget(choco_cashew_label, alignment=Qt.AlignmentFlag.AlignCenter)

	crunchy_double_choco_layout = QVBoxLayout()
	crunchy_double_choco_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	crunchy_double_choco_button = QPushButton()
	crunchy_double_choco_label = QLabel()
	crunchy_double_choco_button.setFixedSize(100, 100)
	crunchy_double_choco_button.setIcon(QIcon('./img/frostbite/frostbite_crunchy_double_choco.jpg'))
	crunchy_double_choco_button.setIconSize(QSize(110, 110))
	crunchy_double_choco_button.clicked.connect(crunchy_double_choco_submit)
	crunchy_double_choco_layout.addWidget(crunchy_double_choco_button, alignment=Qt.AlignmentFlag.AlignCenter)
	crunchy_double_choco_layout.addWidget(crunchy_double_choco_label, alignment=Qt.AlignmentFlag.AlignCenter)

	frostbite_layout3 = QHBoxLayout()
	frostbite_layout3.setAlignment(Qt.AlignmentFlag.AlignLeft)
	frostbite_layout3.addLayout(cookies_cream_stick_layout)
	frostbite_layout3.addLayout(choco_cashew_layout)
	frostbite_layout3.addLayout(crunchy_double_choco_layout)

	frostbite_wrapper = QVBoxLayout()
	frostbite_wrapper.setAlignment(Qt.AlignmentFlag.AlignTop)
	frostbite_label = QLabel('Frostbite')
	frostbite_wrapper.addWidget(frostbite_label)
	frostbite_wrapper.addLayout(frostbite_layout1)
	frostbite_wrapper.addLayout(frostbite_layout2)
	frostbite_wrapper.addLayout(frostbite_layout3)

	all_wrappers_layout.addLayout(frostbite_wrapper)

def jcone_templates():
	global choco_vanilla_rainbow_label, black_pink_label, cookies_cream_cone_label
	def choco_vanilla_rainbow_submit():
		if controllers['current_products'].get('Choco Vanilla Rainbow') is not None:
			controllers['current_products']['Choco Vanilla Rainbow'] += 1
		else:
			controllers['current_products']['Choco Vanilla Rainbow'] = 1
			
		choco_vanilla_rainbow_label.setText(str(controllers['current_products']['Choco Vanilla Rainbow']))
		controllers['current_prices'] += 4000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	def black_pink_submit():
		if controllers['current_products'].get('Black & Pink') is not None:
			controllers['current_products']['Black & Pink'] += 1
		else:
			controllers['current_products']['Black & Pink'] = 1
			
		black_pink_label.setText(str(controllers['current_products']['Black & Pink']))
		controllers['current_prices'] += 6000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	def cookies_cream_cone_submit():
		if controllers['current_products'].get('Cookies & Cream Cone') is not None:
			controllers['current_products']['Cookies & Cream Cone'] += 1
		else:
			controllers['current_products']['Cookies & Cream Cone'] = 1
			
		cookies_cream_cone_label.setText(str(controllers['current_products']['Cookies & Cream Cone']))
		controllers['current_prices'] += 6000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	choco_vanilla_rainbow_layout = QVBoxLayout()
	choco_vanilla_rainbow_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	choco_vanilla_rainbow_button = QPushButton()
	choco_vanilla_rainbow_label = QLabel()
	choco_vanilla_rainbow_button.setFixedSize(100, 100)
	choco_vanilla_rainbow_button.setIcon(QIcon('./img/frostbite_jcone/jcone_choco_vanilla_rainbow.jpg'))
	choco_vanilla_rainbow_button.setIconSize(QSize(110, 110))
	choco_vanilla_rainbow_button.clicked.connect(choco_vanilla_rainbow_submit)
	choco_vanilla_rainbow_layout.addWidget(choco_vanilla_rainbow_button, alignment=Qt.AlignmentFlag.AlignCenter)
	choco_vanilla_rainbow_layout.addWidget(choco_vanilla_rainbow_label, alignment=Qt.AlignmentFlag.AlignCenter)

	black_pink_layout = QVBoxLayout()
	black_pink_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	black_pink_button = QPushButton()
	black_pink_label = QLabel()
	black_pink_button.setFixedSize(100, 100)
	black_pink_button.setIcon(QIcon('./img/frostbite_jcone/jcone_black_pink.jpg'))
	black_pink_button.setIconSize(QSize(110, 110))
	black_pink_button.clicked.connect(black_pink_submit)
	black_pink_layout.addWidget(black_pink_button, alignment=Qt.AlignmentFlag.AlignCenter)
	black_pink_layout.addWidget(black_pink_label, alignment=Qt.AlignmentFlag.AlignCenter)

	cookies_cream_cone_layout = QVBoxLayout()
	cookies_cream_cone_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	cookies_cream_cone_button = QPushButton()
	cookies_cream_cone_label = QLabel()
	cookies_cream_cone_button.setFixedSize(100, 100)
	cookies_cream_cone_button.setIcon(QIcon('./img/frostbite_jcone/jcone_cookies_cream.jpg'))
	cookies_cream_cone_button.setIconSize(QSize(110, 110))
	cookies_cream_cone_button.clicked.connect(cookies_cream_cone_submit)
	cookies_cream_cone_layout.addWidget(cookies_cream_cone_button, alignment=Qt.AlignmentFlag.AlignCenter)
	cookies_cream_cone_layout.addWidget(cookies_cream_cone_label, alignment=Qt.AlignmentFlag.AlignCenter)

	jcone_layout1 = QHBoxLayout()
	jcone_layout1.setAlignment(Qt.AlignmentFlag.AlignLeft)
	jcone_layout1.addLayout(choco_vanilla_rainbow_layout)
	jcone_layout1.addLayout(black_pink_layout)
	jcone_layout1.addLayout(cookies_cream_cone_layout)

	jcone_wrappers = QVBoxLayout()
	jcone_label = QLabel('Frostbite JCone')
	jcone_wrappers.setAlignment(Qt.AlignmentFlag.AlignTop)
	jcone_wrappers.addWidget(jcone_label)
	jcone_wrappers.addLayout(jcone_layout1)

	all_wrappers_layout.addLayout(jcone_wrappers)

def waku_templates():
	global choco_pop_label, choco_loop_label, strawberry_loop_label, choco_berry_loop_label, mango_loop_label, cotton_candy_label, sweet_lychee_label, mixed_berry_label, choco_dino_label
	def choco_pop_submit():
		if controllers['current_products'].get('Choco Pop') is not None:
			controllers['current_products']['Choco Pop'] += 1
		else:
			controllers['current_products']['Choco Pop'] = 1
			
		choco_pop_label.setText(str(controllers['current_products']['Choco Pop']))
		controllers['current_prices'] += 2000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	choco_pop_layout = QVBoxLayout()
	choco_pop_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	choco_pop_button = QPushButton()
	choco_pop_label = QLabel()
	choco_pop_button.setFixedSize(100, 100)
	choco_pop_button.setIcon(QIcon('./img/waku/waku_choco_pop.jpg'))
	choco_pop_button.setIconSize(QSize(110, 110))
	choco_pop_button.clicked.connect(choco_pop_submit)
	choco_pop_layout.addWidget(choco_pop_button, alignment=Qt.AlignmentFlag.AlignCenter)
	choco_pop_layout.addWidget(choco_pop_label, alignment=Qt.AlignmentFlag.AlignCenter)

	def strawberry_loop_submit():
		if controllers['current_products'].get('Strawberry Loop') is not None:
			controllers['current_products']['Strawberry Loop'] += 1
		else:
			controllers['current_products']['Strawberry Loop'] = 1
			
		strawberry_loop_label.setText(str(controllers['current_products']['Strawberry Loop']))
		controllers['current_prices'] += 2000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	strawberry_loop_layout = QVBoxLayout()
	strawberry_loop_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	strawberry_loop_button = QPushButton()
	strawberry_loop_label = QLabel()
	strawberry_loop_button.setFixedSize(100, 100)
	strawberry_loop_button.setIcon(QIcon('./img/waku/waku_strawberry_loop.jpg'))
	strawberry_loop_button.setIconSize(QSize(110, 110))
	strawberry_loop_button.clicked.connect(strawberry_loop_submit)
	strawberry_loop_layout.addWidget(strawberry_loop_button, alignment=Qt.AlignmentFlag.AlignCenter)
	strawberry_loop_layout.addWidget(strawberry_loop_label, alignment=Qt.AlignmentFlag.AlignCenter)

	def choco_loop_submit():
		if controllers['current_products'].get('Choco Loop') is not None:
			controllers['current_products']['Choco Loop'] += 1
		else:
			controllers['current_products']['Choco Loop'] = 1
			
		choco_loop_label.setText(str(controllers['current_products']['Choco Loop']))
		controllers['current_prices'] += 3000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	choco_loop_layout = QVBoxLayout()
	choco_loop_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	choco_loop_button = QPushButton()
	choco_loop_label = QLabel()
	choco_loop_button.setFixedSize(100, 100)
	choco_loop_button.setIcon(QIcon('./img/waku/waku_choco_loop.jpg'))
	choco_loop_button.setIconSize(QSize(110, 110))
	choco_loop_button.clicked.connect(choco_loop_submit)
	choco_loop_layout.addWidget(choco_loop_button, alignment=Qt.AlignmentFlag.AlignCenter)
	choco_loop_layout.addWidget(choco_loop_label, alignment=Qt.AlignmentFlag.AlignCenter)

	def choco_berry_loop_submit():
		if controllers['current_products'].get('Choco Berry Loop') is not None:
			controllers['current_products']['Choco Berry Loop'] += 1
		else:
			controllers['current_products']['Choco Berry Loop'] = 1
			
		choco_berry_loop_label.setText(str(controllers['current_products']['Choco Berry Loop']))
		controllers['current_prices'] += 3000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	choco_berry_loop_layout = QVBoxLayout()
	choco_berry_loop_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	choco_berry_loop_button = QPushButton()
	choco_berry_loop_label = QLabel()
	choco_berry_loop_button.setFixedSize(100, 100)
	choco_berry_loop_button.setIcon(QIcon('./img/waku/waku_choco_berry_loop.jpg'))
	choco_berry_loop_button.setIconSize(QSize(110, 110))
	choco_berry_loop_button.clicked.connect(choco_berry_loop_submit)
	choco_berry_loop_layout.addWidget(choco_berry_loop_button, alignment=Qt.AlignmentFlag.AlignCenter)
	choco_berry_loop_layout.addWidget(choco_berry_loop_label, alignment=Qt.AlignmentFlag.AlignCenter)

	waku_layout1 = QHBoxLayout()
	waku_layout1.setAlignment(Qt.AlignmentFlag.AlignLeft)
	waku_layout1.addLayout(choco_pop_layout)
	waku_layout1.addLayout(strawberry_loop_layout)
	waku_layout1.addLayout(choco_loop_layout)
	waku_layout1.addLayout(choco_berry_loop_layout)

	def mango_loop_submit():
		if controllers['current_products'].get('Mango Loop') is not None:
			controllers['current_products']['Mango Loop'] += 1
		else:
			controllers['current_products']['Mango Loop'] = 1
			
		mango_loop_label.setText(str(controllers['current_products']['Mango Loop']))
		controllers['current_prices'] += 3000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	mango_loop_layout = QVBoxLayout()
	mango_loop_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	mango_loop_button = QPushButton()
	mango_loop_label = QLabel()
	mango_loop_button.setFixedSize(100, 100)
	mango_loop_button.setIcon(QIcon('./img/waku/waku_mango_loop.jpg'))
	mango_loop_button.setIconSize(QSize(110, 110))
	mango_loop_button.clicked.connect(mango_loop_submit)
	mango_loop_layout.addWidget(mango_loop_button, alignment=Qt.AlignmentFlag.AlignCenter)
	mango_loop_layout.addWidget(mango_loop_label, alignment=Qt.AlignmentFlag.AlignCenter)

	def cotton_candy_submit():
		if controllers['current_products'].get('Cotton Candy') is not None:
			controllers['current_products']['Cotton Candy'] += 1
		else:
			controllers['current_products']['Cotton Candy'] = 1
			
		cotton_candy_label.setText(str(controllers['current_products']['Cotton Candy']))
		controllers['current_prices'] += 4000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	cotton_candy_layout = QVBoxLayout()
	cotton_candy_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	cotton_candy_button = QPushButton()
	cotton_candy_label = QLabel()
	cotton_candy_button.setFixedSize(100, 100)
	cotton_candy_button.setIcon(QIcon('./img/waku/waku_cotton_candy.jpg'))
	cotton_candy_button.setIconSize(QSize(110, 110))
	cotton_candy_button.clicked.connect(cotton_candy_submit)
	cotton_candy_layout.addWidget(cotton_candy_button, alignment=Qt.AlignmentFlag.AlignCenter)
	cotton_candy_layout.addWidget(cotton_candy_label, alignment=Qt.AlignmentFlag.AlignCenter)

	def sweet_lychee_submit():
		if controllers['current_products'].get('Sweet Lychee') is not None:
			controllers['current_products']['Sweet Lychee'] += 1
		else:
			controllers['current_products']['Sweet Lychee'] = 1
			
		sweet_lychee_label.setText(str(controllers['current_products']['Sweet Lychee']))
		controllers['current_prices'] += 4000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	sweet_lychee_layout = QVBoxLayout()
	sweet_lychee_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	sweet_lychee_button = QPushButton()
	sweet_lychee_label = QLabel()
	sweet_lychee_button.setFixedSize(100, 100)
	sweet_lychee_button.setIcon(QIcon('./img/waku/waku_sweet_lychee.jpg'))
	sweet_lychee_button.setIconSize(QSize(110, 110))
	sweet_lychee_button.clicked.connect(sweet_lychee_submit)
	sweet_lychee_layout.addWidget(sweet_lychee_button, alignment=Qt.AlignmentFlag.AlignCenter)
	sweet_lychee_layout.addWidget(sweet_lychee_label, alignment=Qt.AlignmentFlag.AlignCenter)

	def mixed_berry_submit():
		if controllers['current_products'].get('Mixed Berry') is not None:
			controllers['current_products']['Mixed Berry'] += 1
		else:
			controllers['current_products']['Mixed Berry'] = 1
			
		mixed_berry_label.setText(str(controllers['current_products']['Mixed Berry']))
		controllers['current_prices'] += 4000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	mixed_berry_layout = QVBoxLayout()
	mixed_berry_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	mixed_berry_button = QPushButton()
	mixed_berry_label = QLabel()
	mixed_berry_button.setFixedSize(100, 100)
	mixed_berry_button.setIcon(QIcon('./img/waku/waku_mixed_berry.jpg'))
	mixed_berry_button.setIconSize(QSize(110, 110))
	mixed_berry_button.clicked.connect(mixed_berry_submit)
	mixed_berry_layout.addWidget(mixed_berry_button, alignment=Qt.AlignmentFlag.AlignCenter)
	mixed_berry_layout.addWidget(mixed_berry_label, alignment=Qt.AlignmentFlag.AlignCenter)

	waku_layout2 = QHBoxLayout()
	waku_layout2.setAlignment(Qt.AlignmentFlag.AlignLeft)
	waku_layout2.addLayout(mango_loop_layout)
	waku_layout2.addLayout(cotton_candy_layout)
	waku_layout2.addLayout(sweet_lychee_layout)
	waku_layout2.addLayout(mixed_berry_layout)

	def choco_dino_submit():
		if controllers['current_products'].get('Choco Dinosaur') is not None:
			controllers['current_products']['Choco Dinosaur'] += 1
		else:
			controllers['current_products']['Choco Dinosaur'] = 1
			
		choco_dino_label.setText(str(controllers['current_products']['Choco Dinosaur']))
		controllers['current_prices'] += 3000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	choco_dino_layout = QVBoxLayout()
	choco_dino_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	choco_dino_button = QPushButton()
	choco_dino_label = QLabel()
	choco_dino_button.setFixedSize(100, 100)
	choco_dino_button.setIcon(QIcon('./img/waku/waku_choco_dinosaur.jpg'))
	choco_dino_button.setIconSize(QSize(110, 110))
	choco_dino_button.clicked.connect(choco_dino_submit)
	choco_dino_layout.addWidget(choco_dino_button, alignment=Qt.AlignmentFlag.AlignCenter)
	choco_dino_layout.addWidget(choco_dino_label, alignment=Qt.AlignmentFlag.AlignCenter)

	waku_layout3 = QHBoxLayout()
	waku_layout3.setAlignment(Qt.AlignmentFlag.AlignLeft)
	waku_layout3.addLayout(choco_dino_layout)

	waku_wrappers = QVBoxLayout()
	waku_label = QLabel('Waku-Waku')
	waku_wrappers.setAlignment(Qt.AlignmentFlag.AlignTop)
	waku_wrappers.addWidget(waku_label)
	waku_wrappers.addLayout(waku_layout1)
	waku_wrappers.addLayout(waku_layout2)
	waku_wrappers.addLayout(waku_layout3)

	all_wrappers_layout.addLayout(waku_wrappers)

def haku_templates():
	global vanilla_crispy_choco_monaka_label, strawberry_crispy_choco_monaka_label, double_crispy_choco_monaka_label, tokyo_cheese_delight_label, tiramisu_label, blueberry_cheesecake_label, matcha_monaka_label, vanilla_monaka_label
	def vanilla_crispy_choco_monaka_submit():
		if controllers['current_products'].get('Vanilla & Crispy Choco Monaka') is not None:
			controllers['current_products']['Vanilla & Crispy Choco Monaka'] += 1
		else:
			controllers['current_products']['Vanilla & Crispy Choco Monaka'] = 1
			
		vanilla_crispy_choco_monaka_label.setText(str(controllers['current_products']['Vanilla & Crispy Choco Monaka']))
		controllers['current_prices'] += 6000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	vanilla_crispy_choco_monaka_layout = QVBoxLayout()
	vanilla_crispy_choco_monaka_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	vanilla_crispy_choco_monaka_button = QPushButton()
	vanilla_crispy_choco_monaka_label = QLabel()
	vanilla_crispy_choco_monaka_button.setFixedSize(100, 100)
	vanilla_crispy_choco_monaka_button.setIcon(QIcon('./img/haku/haku_vanilla_crispy_choco_monaka.jpg'))
	vanilla_crispy_choco_monaka_button.setIconSize(QSize(110, 110))
	vanilla_crispy_choco_monaka_button.clicked.connect(vanilla_crispy_choco_monaka_submit)
	vanilla_crispy_choco_monaka_layout.addWidget(vanilla_crispy_choco_monaka_button, alignment=Qt.AlignmentFlag.AlignCenter)
	vanilla_crispy_choco_monaka_layout.addWidget(vanilla_crispy_choco_monaka_label, alignment=Qt.AlignmentFlag.AlignCenter)

	def strawberry_crispy_choco_monaka_submit():
		if controllers['current_products'].get('Strawberry & Crispy Choco Monaka') is not None:
			controllers['current_products']['Strawberry & Crispy Choco Monaka'] += 1
		else:
			controllers['current_products']['Strawberry & Crispy Choco Monaka'] = 1
			
		strawberry_crispy_choco_monaka_label.setText(str(controllers['current_products']['Strawberry & Crispy Choco Monaka']))
		controllers['current_prices'] += 6000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	strawberry_crispy_choco_monaka_layout = QVBoxLayout()
	strawberry_crispy_choco_monaka_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	strawberry_crispy_choco_monaka_button = QPushButton()
	strawberry_crispy_choco_monaka_label = QLabel()
	strawberry_crispy_choco_monaka_button.setFixedSize(100, 100)
	strawberry_crispy_choco_monaka_button.setIcon(QIcon('./img/haku/haku_strawberry_crispy_choco_monaka.jpg'))
	strawberry_crispy_choco_monaka_button.setIconSize(QSize(110, 110))
	strawberry_crispy_choco_monaka_button.clicked.connect(strawberry_crispy_choco_monaka_submit)
	strawberry_crispy_choco_monaka_layout.addWidget(strawberry_crispy_choco_monaka_button, alignment=Qt.AlignmentFlag.AlignCenter)
	strawberry_crispy_choco_monaka_layout.addWidget(strawberry_crispy_choco_monaka_label, alignment=Qt.AlignmentFlag.AlignCenter)

	def double_crispy_choco_monaka_submit():
		if controllers['current_products'].get('Double Crispy Choco Monaka') is not None:
			controllers['current_products']['Double Crispy Choco Monaka'] += 1
		else:
			controllers['current_products']['Double Crispy Choco Monaka'] = 1
			
		double_crispy_choco_monaka_label.setText(str(controllers['current_products']['Double Crispy Choco Monaka']))
		controllers['current_prices'] += 6000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	double_crispy_choco_monaka_layout = QVBoxLayout()
	double_crispy_choco_monaka_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	double_crispy_choco_monaka_button = QPushButton()
	double_crispy_choco_monaka_label = QLabel()
	double_crispy_choco_monaka_button.setFixedSize(100, 100)
	double_crispy_choco_monaka_button.setIcon(QIcon('./img/haku/haku_double_crispy_choco_monaka.jpg'))
	double_crispy_choco_monaka_button.setIconSize(QSize(110, 110))
	double_crispy_choco_monaka_button.clicked.connect(double_crispy_choco_monaka_submit)
	double_crispy_choco_monaka_layout.addWidget(double_crispy_choco_monaka_button, alignment=Qt.AlignmentFlag.AlignCenter)
	double_crispy_choco_monaka_layout.addWidget(double_crispy_choco_monaka_label, alignment=Qt.AlignmentFlag.AlignCenter)

	def tokyo_cheese_delight_submit():
		if controllers['current_products'].get('Tokyo Cheese Delight') is not None:
			controllers['current_products']['Tokyo Cheese Delight'] += 1
		else:
			controllers['current_products']['Tokyo Cheese Delight'] = 1
			
		tokyo_cheese_delight_label.setText(str(controllers['current_products']['Tokyo Cheese Delight']))
		controllers['current_prices'] += 10000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	tokyo_cheese_delight_layout = QVBoxLayout()
	tokyo_cheese_delight_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	tokyo_cheese_delight_button = QPushButton()
	tokyo_cheese_delight_label = QLabel()
	tokyo_cheese_delight_button.setFixedSize(100, 100)
	tokyo_cheese_delight_button.setIcon(QIcon('./img/haku/haku_tokyo_cheese_delight.jpg'))
	tokyo_cheese_delight_button.setIconSize(QSize(110, 110))
	tokyo_cheese_delight_button.clicked.connect(tokyo_cheese_delight_submit)
	tokyo_cheese_delight_layout.addWidget(tokyo_cheese_delight_button, alignment=Qt.AlignmentFlag.AlignCenter)
	tokyo_cheese_delight_layout.addWidget(tokyo_cheese_delight_label, alignment=Qt.AlignmentFlag.AlignCenter)

	haku_layout1 = QHBoxLayout()
	haku_layout1.setAlignment(Qt.AlignmentFlag.AlignLeft)
	haku_layout1.addLayout(vanilla_crispy_choco_monaka_layout)
	haku_layout1.addLayout(strawberry_crispy_choco_monaka_layout)
	haku_layout1.addLayout(double_crispy_choco_monaka_layout)
	haku_layout1.addLayout(tokyo_cheese_delight_layout)

	def blueberry_cheesecake_submit():
		if controllers['current_products'].get('Blueberry Cheesecake') is not None:
			controllers['current_products']['Blueberry Cheesecake'] += 1
		else:
			controllers['current_products']['Blueberry Cheesecake'] = 1
			
		blueberry_cheesecake_label.setText(str(controllers['current_products']['Blueberry Cheesecake']))
		controllers['current_prices'] += 10000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	blueberry_cheesecake_layout = QVBoxLayout()
	blueberry_cheesecake_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	blueberry_cheesecake_button = QPushButton()
	blueberry_cheesecake_label = QLabel()
	blueberry_cheesecake_button.setFixedSize(100, 100)
	blueberry_cheesecake_button.setIcon(QIcon('./img/haku/haku_blueberry_cheesecake.jpg'))
	blueberry_cheesecake_button.setIconSize(QSize(110, 110))
	blueberry_cheesecake_button.clicked.connect(blueberry_cheesecake_submit)
	blueberry_cheesecake_layout.addWidget(blueberry_cheesecake_button, alignment=Qt.AlignmentFlag.AlignCenter)
	blueberry_cheesecake_layout.addWidget(blueberry_cheesecake_label, alignment=Qt.AlignmentFlag.AlignCenter)

	def tiramisu_submit():
		if controllers['current_products'].get('Tiramisu') is not None:
			controllers['current_products']['Tiramisu'] += 1
		else:
			controllers['current_products']['Tiramisu'] = 1
			
		tiramisu_label.setText(str(controllers['current_products']['Tiramisu']))
		controllers['current_prices'] += 10000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	tiramisu_layout = QVBoxLayout()
	tiramisu_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	tiramisu_button = QPushButton()
	tiramisu_label = QLabel()
	tiramisu_button.setFixedSize(100, 100)
	tiramisu_button.setIcon(QIcon('./img/haku/haku_tiramisu.jpg'))
	tiramisu_button.setIconSize(QSize(110, 110))
	tiramisu_button.clicked.connect(tiramisu_submit)
	tiramisu_layout.addWidget(tiramisu_button, alignment=Qt.AlignmentFlag.AlignCenter)
	tiramisu_layout.addWidget(tiramisu_label, alignment=Qt.AlignmentFlag.AlignCenter)

	def vanilla_monaka_submit():
		if controllers['current_products'].get('Vanilla Monaka') is not None:
			controllers['current_products']['Vanilla Monaka'] += 1
		else:
			controllers['current_products']['Vanilla Monaka'] = 1
			
		vanilla_monaka_label.setText(str(controllers['current_products']['Vanilla Monaka']))
		controllers['current_prices'] += 14000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	vanilla_monaka_layout = QVBoxLayout()
	vanilla_monaka_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	vanilla_monaka_button = QPushButton()
	vanilla_monaka_label = QLabel()
	vanilla_monaka_button.setFixedSize(100, 100)
	vanilla_monaka_button.setIcon(QIcon('./img/haku/haku_vanilla_monaka.jpg'))
	vanilla_monaka_button.setIconSize(QSize(110, 110))
	vanilla_monaka_button.clicked.connect(vanilla_monaka_submit)
	vanilla_monaka_layout.addWidget(vanilla_monaka_button, alignment=Qt.AlignmentFlag.AlignCenter)
	vanilla_monaka_layout.addWidget(vanilla_monaka_label, alignment=Qt.AlignmentFlag.AlignCenter)

	def matcha_monaka_submit():
		if controllers['current_products'].get('Matcha Monaka') is not None:
			controllers['current_products']['Matcha Monaka'] += 1
		else:
			controllers['current_products']['Matcha Monaka'] = 1
			
		matcha_monaka_label.setText(str(controllers['current_products']['Matcha Monaka']))
		controllers['current_prices'] += 14000
		moneys_label.setText(f'Total Moneys: {controllers["current_prices"]}')

	matcha_monaka_layout = QVBoxLayout()
	matcha_monaka_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
	matcha_monaka_button = QPushButton()
	matcha_monaka_label = QLabel()
	matcha_monaka_button.setFixedSize(100, 100)
	matcha_monaka_button.setIcon(QIcon('./img/haku/haku_matcha_monaka.jpg'))
	matcha_monaka_button.setIconSize(QSize(110, 110))
	matcha_monaka_button.clicked.connect(matcha_monaka_submit)
	matcha_monaka_layout.addWidget(matcha_monaka_button, alignment=Qt.AlignmentFlag.AlignCenter)
	matcha_monaka_layout.addWidget(matcha_monaka_label, alignment=Qt.AlignmentFlag.AlignCenter)

	haku_layout2 = QHBoxLayout()
	haku_layout2.setAlignment(Qt.AlignmentFlag.AlignLeft)
	haku_layout2.addLayout(blueberry_cheesecake_layout)
	haku_layout2.addLayout(tiramisu_layout)
	haku_layout2.addLayout(vanilla_monaka_layout)
	haku_layout2.addLayout(matcha_monaka_layout)

	haku_wrappers = QVBoxLayout()
	haku_label = QLabel('Haku')
	haku_wrappers.setAlignment(Qt.AlignmentFlag.AlignTop)
	haku_wrappers.addWidget(haku_label)
	haku_wrappers.addLayout(haku_layout1)
	haku_wrappers.addLayout(haku_layout2)

	all_wrappers_layout.addLayout(haku_wrappers)

def props_templates():
	global moneys_label, expense_label, cuts_label, warning_label, incomes_label, earnings_label, reports_label, paybacks_label
	moneys_label = QLabel('Total Moneys: ')
	expense_label = QLabel('Total Expense: ')
	cuts_label = QLabel('Total Cuts: ')
	warning_label = QLabel()
	warning_label.setStyleSheet('color:red')

	incomes_label = QLabel('Total Incomes: ')
	earnings_label = QLabel('Total Earnings: ')
	reports_label = QLabel('Total Reports: ')
	paybacks_label = QLabel()
	paybacks_label.setStyleSheet('color:red')

	props_layout1 = QVBoxLayout()
	props_layout1.addWidget(moneys_label)
	props_layout1.addWidget(expense_label)
	props_layout1.addWidget(reports_label)
	props_layout1.addWidget(warning_label)

	props_layout2 = QVBoxLayout()
	props_layout2.addWidget(incomes_label)
	props_layout2.addWidget(cuts_label)
	props_layout2.addWidget(earnings_label)
	props_layout2.addWidget(paybacks_label)

	props_wrapper = QHBoxLayout()
	props_label = QLabel('Properties')
	props_wrapper.addLayout(props_layout1)
	props_wrapper.addLayout(props_layout2)

	all_wrappers_layout.addLayout(props_wrapper)

def section_templates():
	expenses_layout = QHBoxLayout()
	expenses_label = QLabel('Expenses: ')
	expenses_edit = QLineEdit()
	expenses_edit.editingFinished.connect(expenses_submit)
	expenses_layout.addWidget(expenses_label)
	expenses_layout.addWidget(expenses_edit)

	customer_layout = QHBoxLayout()
	customer_label = QLabel('Customers: ')
	customer_edit = QLineEdit()
	customer_edit.editingFinished.connect(customer_submit)
	customer_layout.addWidget(customer_label)
	customer_layout.addWidget(customer_edit)

	section_wrappers = QVBoxLayout()
	section_label = QLabel('Section')
	section_wrappers.addLayout(expenses_layout)
	section_wrappers.addLayout(customer_layout)

	all_wrappers_layout.addLayout(section_wrappers)

def button_templates():
	def accept_submit():
		dates = str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
		jsonize = {}
		jsonize[dates] = {}
		if controllers['current_prices']:
			jsonize[dates]['profits'] = controllers['current_prices']
		if controllers['customer_moneys']:
			paybacks = controllers['customer_moneys'] - controllers['current_prices']
			if paybacks > 0:
				paybacks_label.setText(f'*Paybacks: {paybacks}')
				jsonize[dates]['paybacks'] = paybacks
			elif paybacks < 0:
				warning_label.setText(f'*Money: {paybacks}')
			jsonize[dates]['received'] = controllers['customer_moneys']
		if controllers['current_products']:
			jsonize[dates]['products'] = []
			for element in list(controllers['current_products']):
				with open('./bin/properties.json', 'r+') as file:
					json_content = json.load(file)
				for elem in list(json_content):
					for ele in json_content[elem]:
						if element == ele['products']:
							jsonize[dates]['products'].append(merge(ele, {'numbers': controllers['current_products'][element]}))
		if controllers['current_expenses']:
			jsonize[dates]['expenses'] = controllers['current_expenses']
			if controllers['current_reasons']:
				jsonize[dates]['reasons'] = controllers['current_reasons']
		with open(location, 'r+') as file:
			json_content = json.load(file)
			file.seek(0)
			file.write(json.dumps(merge(json_content, jsonize), sort_keys = True, indent = 4))
		current_button_submit()
		global_var()

	def reset_submit():
		moneys_label.setText('Total Moneys: ')
		expense_label.setText('Total Expenses: ')
		reports_label.setText('Total Reports: ')
		warning_label.setText('')

		incomes_label.setText('Total Incomes: ')
		earnings_label.setText('Total Earnings: ')
		cuts_label.setText('Total Cuts: ')
		paybacks_label.setText('')

		choco_lava_mochi_label.setText('') 
		strawberry_sakura_mochi_label.setText('')
		cookies_cream_mochi_label.setText('')
		vita_fruit_label.setText('')
		boba_milk_tea_label.setText('')
		strawberry_vanilla_label.setText('')
		tutti_frutti_label.setText('')
		chocolate_vanilla_label.setText('')
		cookies_cream_stick_label.setText('')
		choco_cashew_label.setText('')
		crunchy_double_choco_label.setText('')

		choco_vanilla_rainbow_label.setText('')
		black_pink_label.setText('')
		cookies_cream_cone_label.setText('')

		choco_pop_label.setText('')
		choco_loop_label.setText('')
		strawberry_loop_label.setText('')
		choco_berry_loop_label.setText('')
		mango_loop_label.setText('')
		cotton_candy_label.setText('')
		sweet_lychee_label.setText('')
		mixed_berry_label.setText('')
		choco_dino_label.setText('')

		vanilla_crispy_choco_monaka_label.setText('')
		strawberry_crispy_choco_monaka_label.setText('')
		double_crispy_choco_monaka_label.setText('')
		tokyo_cheese_delight_label.setText('')
		tiramisu_label.setText('')
		blueberry_cheesecake_label.setText('')
		matcha_monaka_label.setText('')
		vanilla_monaka_label.setText('')
		
		global_var()

	def current_button_submit():
		with open(location, 'r+') as file:
			json_content = json.load(file)
		total_money = 0
		total_products = 0
		total_expenses = 0
		for element in list(json_content):
			for elem in json_content[element].get('products', []):
				total_products += elem['numbers']
			total_money += json_content[element].get('profits', 0)
			total_expenses += json_content[element].get('expenses', 0)
		total_cuts = total_products * 1000
		total_incomes = total_money - total_cuts + total_expenses
		total_earnings = (total_incomes * 22.2222) / 100
		print(total_products)

		moneys_label.setText(f'Total Moneys: {total_money}')
		expense_label.setText(f'Total Expenses: {total_expenses}')
		reports_label.setText(f'Total Reports: {total_products}')
		warning_label.setText('')

		incomes_label.setText(f'Total Incomes: {total_incomes}')
		earnings_label.setText(f'Total Earnings: {total_earnings}')
		cuts_label.setText(f'Total Cuts: {total_cuts}')
		paybacks_label.setText('')

	def any_button_submit():
		total_money = 0
		total_products = 0
		total_expenses = 0
		for file in glob.glob('.json'):
			with open(file, 'r+') as file:
				json_content = json.load(file)
			for element in list(json_content):
				total_products += len(json_content[element].get('products', []))
				total_products += json_content[element].get('profits', 0)
				total_expenses += json_content[element].get('expenses', 0)
		total_cuts = total_products * 1000
		total_incomes = total_money - total_cuts + total_expenses
		total_earnings = (total_incomes * 25) / 100

		moneys_label.setText(f'Total Moneys: {total_money}')
		expense_label.setText(f'Total Expenses: {total_expenses}')
		reports_label.setText(f'Total Reports: {total_products}')
		warning_label.setText('')

		incomes_label.setText(f'Total Incomes: {total_incomes}')
		earnings_label.setText(f'Total Earnings: {total_earnings}')
		cuts_label.setText(f'Total Cuts: {total_cuts}')
		paybacks_label.setText('')

	accept_button = QPushButton('Accept')
	accept_button.clicked.connect(accept_submit)
	reset_button = QPushButton('Reset')
	reset_button.clicked.connect(reset_submit)

	current_button = QPushButton('Current')
	current_button.clicked.connect(current_button_submit)
	any_button = QPushButton('Any')
	any_button.clicked.connect(any_button_submit)

	button_layout1 = QHBoxLayout()
	button_layout1.addWidget(accept_button)
	button_layout1.addWidget(reset_button)

	button_layout2 = QHBoxLayout()
	button_layout2.addWidget(current_button)
	button_layout2.addWidget(any_button)

	button_wrappers = QVBoxLayout()
	button_wrappers.addLayout(button_layout1)
	button_wrappers.addLayout(button_layout2)

	all_wrappers_layout.addLayout(button_wrappers)

def global_var():
	global controllers
	controllers = {'current_products': {}, 'current_prices': 0, 'customer_moneys': 0, 'current_expenses': 0, 'current_reasons': ''}

if os.path.isfile(location) is False:
	with open(location, 'w') as f:
		f.write('{}')

os.chdir(os.path.dirname(sys.argv[0]))
global_var()

app = QApplication()
main_window = QMainWindow()
window = QWidget()
scrolls = QScrollArea()

main_window.setWindowTitle('Icelander v1.0')
main_window.setWindowIcon(QIcon('icelander.ico'))
all_wrappers_layout = QVBoxLayout()
frostbite_templates()
jcone_templates()
waku_templates()
haku_templates()
props_templates()
button_templates()

window.setLayout(all_wrappers_layout)
scrolls.setWidget(window)
main_window.setCentralWidget(scrolls)

main_window.show()
app.exec()