
import os
import sys
import glob
import time
import json
import datetime
import operator
from jsonmerge import merge, Merger
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit, QVBoxLayout, QMainWindow, QScrollArea, QSizePolicy, QComboBox, QListView, QCompleter
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QSize, QTimer, QCoreApplication
from PySide6.QtCore import Qt

location = f"./{str(datetime.datetime.now().strftime('%Y%m%d'))}.json"

class MainWindow(QWidget): 
	def __init__(self):
		super().__init__()
		self.wrappers = QVBoxLayout()
		self.scrolls = QScrollArea()
		self.scrolls.setWidgetResizable(True)
		self.scrolls_layout = QVBoxLayout()
		self.scroll_widget = QWidget()

		self.search_templates()
		self.generate_templates()
		self.scroll_widget.setLayout(self.scrolls_layout)
		self.scrolls.setWidget(self.scroll_widget)
		self.wrappers.addWidget(self.scrolls)
		self.props_templates()
		self.section_templates()
		self.button_templates()

		self.setLayout(self.wrappers)

	def search_templates(self):
		search_layout = QVBoxLayout()
		self.comboBox = QComboBox()
		self.comboBox.setView(QListView())
		self.comboBox.setStyleSheet("QListView::item {height:30px;}")
		with open('./bin/properties.json') as file:
			json_content = json.load(file)
		for element in list(json_content):
			for elem in json_content[element]:
				self.comboBox.addItem(QIcon(elem['icons']), elem['products'])
		self.comboBox.setFont(QFont("Times", 10))
		self.comboBox.setIconSize(QSize(50, 50))
		self.comboBox.setEditable(True)
		self.comboBox.setInsertPolicy(QComboBox.NoInsert)
		self.comboBox.completer().setCompletionMode(QCompleter.PopupCompletion)
		self.comboBox.completer().setFilterMode(Qt.MatchFlag.MatchContains)
		search_layout.addWidget(self.comboBox)

		button_layout = QVBoxLayout()
		add_button = QPushButton('Add')
		add_button.clicked.connect(lambda *args, texti=self.comboBox.currentText(): self.add_submit(texti, None))
		button_layout.addWidget(add_button)
		remove_button = QPushButton('Remove')
		remove_button.clicked.connect(lambda *args, texti=self.comboBox.currentText(): self.remove_submit(texti, None))
		button_layout.addWidget(remove_button)

		search_wrappers = QHBoxLayout()
		search_wrappers.addLayout(search_layout)
		search_wrappers.addLayout(button_layout)
		self.scrolls_layout.addLayout(search_wrappers)

	def generate_templates(self):
		with open('./bin/properties.json') as file:
			json_content = json.load(file)

		for element in list(json_content):
			section_layout = QVBoxLayout()
			section_label = QLabel(element)
			section_layout.addWidget(section_label)
			layout_num = 0
			products_num = 0
			products_total = len(json_content[element]) - 1
			while not products_num == products_total:
				product_layout = QHBoxLayout()
				for _ in range(4):
					btn_layout = QVBoxLayout()
					btn_label = QLabel()
					btn = QPushButton()
					btn.setMinimumSize(QSize(100, 100))
					btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
					btn.setIcon(QIcon(json_content[element][products_num]['icons']))
					btn.setIconSize(QSize(110, 110))
					texti = json_content[element][products_num]['products']
					btn.clicked.connect(lambda *args, texti=texti, btn_label=btn_label: self.templates(texti, btn_label))
					btn_layout.addWidget(btn)
					btn_layout.addWidget(btn_label)
					product_layout.addLayout(btn_layout)
					if not (products_num == products_total):
						products_num += 1
					else:
						break
				section_layout.addLayout(product_layout)
				layout_num += 1
			self.scrolls_layout.addLayout(section_layout)

	def props_templates(self):
		self.moneys_label = QLabel('Total Moneys: ')
		self.expense_label = QLabel('Total Expenses: ')
		self.cuts_label = QLabel('Total Cuts: ')
		self.warning_label = QLabel()
		self.warning_label.setStyleSheet('color:red')

		self.incomes_label = QLabel('Total Incomes: ')
		self.earnings_label = QLabel('Total Earnings: ')
		self.reports_label = QLabel('Total Reports: ')
		self.paybacks_label = QLabel()
		self.paybacks_label.setStyleSheet('color:red')

		props_layout1 = QVBoxLayout()
		props_layout1.addWidget(self.moneys_label)
		props_layout1.addWidget(self.expense_label)
		props_layout1.addWidget(self.reports_label)
		props_layout1.addWidget(self.warning_label)

		props_layout2 = QVBoxLayout()
		props_layout2.addWidget(self.incomes_label)
		props_layout2.addWidget(self.cuts_label)
		props_layout2.addWidget(self.earnings_label)
		props_layout2.addWidget(self.paybacks_label)

		props_wrapper = QHBoxLayout()
		props_label = QLabel('Properties')
		props_wrapper.addLayout(props_layout1)
		props_wrapper.addLayout(props_layout2)

		self.wrappers.addLayout(props_wrapper)
	
	def section_templates(self):
		customer_layout = QVBoxLayout()
		labels_layout = QHBoxLayout()
		self.switchers_label = QLabel('Switchers: ')
		self.customer_label = QLabel('Customers: ')
		self.customer_edit = QLineEdit()
		self.customer_edit.setPlaceholderText('Customers')
		self.customer_edit.editingFinished.connect(self.customer_submit)
		labels_layout.addWidget(self.switchers_label)
		labels_layout.addWidget(self.customer_label)
		customer_layout.addLayout(labels_layout)
		customer_layout.addWidget(self.customer_edit)

		self.wrappers.addLayout(customer_layout)

	def button_templates(self):
		accept_button = QPushButton('Accept')
		accept_button.clicked.connect(self.accept_submit)
		reset_button = QPushButton('Reset')
		reset_button.clicked.connect(self.reset_submit)

		current_button = QPushButton('Current')
		current_button.clicked.connect(self.current_button_submit)
		any_button = QPushButton('Any')
		any_button.clicked.connect(self.any_button_submit)

		expenses_button = QPushButton('Expenses')
		expenses_button.clicked.connect(self.expenses_submit)
		stats_button = QPushButton('Statistics')
		stats_button.clicked.connect(self.stats_submit)

		switchers_button = QPushButton('Switcher')
		switchers_button.clicked.connect(self.switchers)

		button_layout1 = QHBoxLayout()
		button_layout1.addWidget(accept_button)
		button_layout1.addWidget(reset_button)

		button_layout2 = QHBoxLayout()
		button_layout2.addWidget(current_button)
		button_layout2.addWidget(any_button)

		button_layout3 = QHBoxLayout()
		button_layout3.addWidget(expenses_button)
		button_layout3.addWidget(stats_button)

		button_wrappers = QVBoxLayout()
		button_wrappers.addLayout(button_layout1)
		button_wrappers.addLayout(button_layout2)
		button_wrappers.addLayout(button_layout3)
		button_wrappers.addWidget(switchers_button)

		self.wrappers.addLayout(button_wrappers)

	def customer_submit(self):
		if int(self.customer_edit.text()) < 999:
			stores['customers'] += int(self.customer_edit.text()) * 1000
		else:
			stores['customers'] += int(self.customer_edit.text())
		self.customer_label.setText(f"Customers: {stores['customers']}")

	def templates(self, texti, label):
		controllers['labels'].append(label)
		if stores['products'].get(texti['products']) is not None:
			stores['products'][texti['products']] += 1
		else:
			stores['products'][texti['products']] = 1
		label.setText(f"{stores['products'][texti['products']]}")
		stores['prices'] += texti['prices']
		label.setText(str(stores['products'][texti['products']]))
		self.moneys_label.setText(f"Total Moneys: {stores['prices']}")

	def any_button_submit(self):
		total_money = 0
		total_products = 0
		total_expenses = 0
		for file in glob.glob('./*.json'):
			with open(file, 'r+') as file:
				json_content = json.load(file)
			for element in list(json_content):
				for elem in json_content[element].get('products', []):
					total_products += elem['numbers']
				total_money += json_content[element].get('profits', 0)
				total_expenses += json_content[element].get('expenses', 0)
		total_cuts = total_products * 1000
		total_incomes = total_money - total_cuts + total_expenses
		total_earnings = (total_incomes * 22.2222) / 100

		self.moneys_label.setText(f'Total Moneys: {total_money}')
		self.expense_label.setText(f'Total Expenses: {total_expenses}')
		self.reports_label.setText(f'Total Reports: {total_products}')
		self.warning_label.setText('')

		self.incomes_label.setText(f'Total Incomes: {total_incomes}')
		self.earnings_label.setText(f'Total Earnings: {total_earnings}')
		self.cuts_label.setText(f'Total Cuts: {total_cuts}')
		self.paybacks_label.setText('')

	def current_button_submit(self):
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
		total_incomes = total_money - total_cuts
		total_earnings = ((total_incomes * 22.2222) / 100) + total_expenses

		self.moneys_label.setText(f'Total Moneys: {total_money}')
		self.expense_label.setText(f'Total Expenses: {total_expenses}')
		self.reports_label.setText(f'Total Reports: {total_products}')
		self.warning_label.setText('')

		self.incomes_label.setText(f'Total Incomes: {total_incomes}')
		self.earnings_label.setText(f'Total Earnings: {total_earnings}')
		self.cuts_label.setText(f'Total Cuts: {total_cuts}')
		self.paybacks_label.setText('')

	def switchers(self):
		if controllers['operators'] == '+':
			controllers['operators'] = '-'
		else:
			controllers['operators'] = '+'
		self.switchers_label.setText(f"Switchers: {controllers['operators']}")

	def templates(self, labels, reff):
		controllers['labels'].append(reff)
		if controllers['operators'] == '+':
			self.add_submit(labels, reff)
		else:
			self.remove_submit(labels, reff)

	def expenses_submit(self):
		global mainWin
		mainWin = ExpenseWindow()
		scrolls = QScrollArea()
		scrolls.setWidget(mainWin)
		scrolls.setWidgetResizable(True)
		main_window.setCentralWidget(scrolls)
		main_window.resize(450, 600)
		main_window.show()

	def stats_submit(self):
		global mainWin
		mainWin = StatsWindow()
		main_window.setCentralWidget(mainWin)
		main_window.resize(450, 600)
		main_window.show()

	def add_submit(self, labels, reff):
		with open('./bin/properties.json', 'r+') as file:
			json_content = json.load(file)
		for element in list(json_content):
			for elem in json_content[element]:
				if elem['products'] == labels:
					if stores['products'].get(labels) is not None:
						stores['products'][labels] += 1
					else:
						stores['products'][labels] = 1
					stores['prices'] += elem['prices']
		self.moneys_label.setText(f"Total Moneys: {stores['prices']}")
		if reff is not None:
			reff.setText(str(stores['products'][labels]))

	def remove_submit(self, labels, reff):
		with open('./bin/properties.json', 'r+') as file:
			json_content = json.load(file)
		for element in list(json_content):
			for elem in json_content[element]:
				if elem['products'] == labels:
					if stores['products'].get(labels) is not None:
						stores['products'][labels] -= 1
					else:
						stores['products'][labels] = 0
					stores['prices'] -= elem['prices']
		self.moneys_label.setText(f"Total Moneys: {stores['prices']}")
		if reff is not None:
			reff.setText(str(stores['products'][labels]))

	def reset_submit(self):
		for i in controllers['labels']:
			i.setText('')

		self.moneys_label.setText('Total Moneys: ')
		self.expense_label.setText('Total Expenses: ')
		self.reports_label.setText('Total Reports: ')

		self.incomes_label.setText('Total Incomes: ')
		self.earnings_label.setText('Total Earnings: ')
		self.cuts_label.setText('Total Cuts: ')	

		self.customer_edit.clear()
		global_var()

	def accept_submit(self):
		self.warning_label.setText('')
		self.paybacks_label.setText('')
		self.customer_label.setText('')
		saves()
		if stores['paybacks'] > 0:
			self.paybacks_label.setText(f"*Paybacks: {stores['paybacks']}")
		elif stores['paybacks'] < 0:
			self.warning_label.setText(f"*Money: {stores['paybacks']}")
		self.reset_submit()
		global_var()

class ExpenseWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.expense_wrappers = QVBoxLayout()
		self.scrolls = QScrollArea()
		self.scrolls.setWidgetResizable(True)
		self.scrolls_layout = QVBoxLayout()
		self.scroll_widget = QWidget()

		self.search_templates()
		self.generate_templates()
		self.scroll_widget.setLayout(self.scrolls_layout)
		self.scrolls.setWidget(self.scroll_widget)
		self.expense_wrappers.addWidget(self.scrolls)
		self.section_templates()
		self.props_templates()
		self.setLayout(self.expense_wrappers)

	def section_templates(self):
		edit_layout = QVBoxLayout()
		self.reason_edit = QLineEdit()
		self.reason_edit.setPlaceholderText('Reasons')
		self.reason_edit.editingFinished.connect(self.reason_submit)
		self.expense_edit = QLineEdit()
		self.expense_edit.setPlaceholderText('Expenses')
		self.expense_edit.editingFinished.connect(self.expense_submit)
		switchers_button = QPushButton('Switchers')
		switchers_button.clicked.connect(self.switchers)
		edit_layout.addWidget(self.reason_edit)
		edit_layout.addWidget(self.expense_edit)
		edit_layout.addWidget(switchers_button)

		section_layout = QHBoxLayout()
		self.expenses_label = QLabel('Expenses: ')
		self.reasons_label = QLabel('Reasons: ')
		self.switchers_label = QLabel('Switchers: ')
		section_layout.addWidget(self.expenses_label)
		section_layout.addWidget(self.reasons_label)
		section_layout.addWidget(self.switchers_label)

		section_wrappers = QVBoxLayout()
		section_wrappers.addLayout(section_layout)
		section_wrappers.addLayout(edit_layout)

		self.expense_wrappers.addLayout(section_wrappers)

	def props_templates(self):
		accept_button = QPushButton('Accept')
		accept_button.clicked.connect(self.accept_submit)
		reset_button = QPushButton('Reset')
		reset_button.clicked.connect(self.reset_submit)

		menus_button = QPushButton('Menus')
		menus_button.clicked.connect(self.menu_submit)
		stats_button = QPushButton('Statistics')
		stats_button.clicked.connect(self.stats_submit)

		button_layout1 = QHBoxLayout()
		button_layout1.addWidget(accept_button)
		button_layout1.addWidget(reset_button)

		button_layout2 = QHBoxLayout()
		button_layout2.addWidget(menus_button)
		button_layout2.addWidget(stats_button)

		button_wrappers = QVBoxLayout()
		button_wrappers.addLayout(button_layout1)
		button_wrappers.addLayout(button_layout2)

		self.expense_wrappers.addLayout(button_wrappers)

	def search_templates(self):
		search_layout = QVBoxLayout()
		self.comboBox = QComboBox()
		self.comboBox.setView(QListView())
		self.comboBox.setStyleSheet("QListView::item {height:30px;}")
		with open('./bin/properties.json') as file:
			json_content = json.load(file)
		for element in list(json_content):
			for elem in json_content[element]:
				self.comboBox.addItem(QIcon(elem['icons']), elem['products'])
		self.comboBox.setFont(QFont("Times", 10))
		self.comboBox.setIconSize(QSize(50, 50))
		self.comboBox.setEditable(True)
		self.comboBox.setInsertPolicy(QComboBox.NoInsert)
		self.comboBox.completer().setCompletionMode(QCompleter.PopupCompletion)
		self.comboBox.completer().setFilterMode(Qt.MatchFlag.MatchContains)
		search_layout.addWidget(self.comboBox)

		button_layout = QVBoxLayout()
		add_button = QPushButton('Add')
		add_button.clicked.connect(lambda *args, texti=self.comboBox.currentText(): self.add_submit(texti, None))
		button_layout.addWidget(add_button)
		remove_button = QPushButton('Remove')
		remove_button.clicked.connect(lambda *args, texti=self.comboBox.currentText(): self.remove_submit(texti, None))
		button_layout.addWidget(remove_button)

		search_wrappers = QHBoxLayout()
		search_wrappers.addLayout(search_layout)
		search_wrappers.addLayout(button_layout)
		self.scrolls_layout.addLayout(search_wrappers)

	def generate_templates(self):
		with open('./bin/properties.json') as file:
			json_content = json.load(file)

		for element in list(json_content):
			section_layout = QVBoxLayout()
			section_label = QLabel(element)
			section_layout.addWidget(section_label)
			layout_num = 0
			products_num = 0
			products_total = len(json_content[element]) - 1
			while not products_num == products_total:
				product_layout = QHBoxLayout()
				for _ in range(4):
					btn_layout = QVBoxLayout()
					btn_label = QLabel()
					btn = QPushButton()
					btn.setMinimumSize(QSize(100, 100))
					btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
					btn.setIcon(QIcon(json_content[element][products_num]['icons']))
					btn.setIconSize(QSize(110, 110))
					texti = json_content[element][products_num]['products']
					btn.clicked.connect(lambda *args, texti=texti, btn_label=btn_label: self.templates(texti, btn_label))
					btn_layout.addWidget(btn)
					btn_layout.addWidget(btn_label)
					product_layout.addLayout(btn_layout)
					if not (products_num == products_total):
						products_num += 1
					else:
						break
				section_layout.addLayout(product_layout)
				layout_num += 1
			self.scrolls_layout.addLayout(section_layout)

	def expense_submit(self):
		if int(self.expense_edit.text()) < 999:
			outers['expenses'] += int(self.expense_edit.text()) * 1000
		else:
			outers['expenses'] += int(self.expense_edit.text()) * 1000
	
	def reason_submit(self):
		outers['reasons'] += self.reason_edit.text()
		self.reasons_label.setText(f"Reasons: {outers['reasons']}")

	def switchers(self):
		if controllers['operators'] == '+':
			controllers['operators'] = '-'
		else:
			controllers['operators'] = '+'
		self.switchers_label.setText(f"Switchers: {controllers['operators']}")

	def templates(self, labels, reff):
		controllers['labels'].append(reff)
		if controllers['operators'] == '+':
			self.add_submit(labels, reff)
		else:
			self.remove_submit(labels, reff)

	def add_submit(self, labels, reff):
		with open('./bin/properties.json', 'r+') as file:
			json_content = json.load(file)
		for element in list(json_content):
			for elem in json_content[element]:
				if elem['products'] == labels:
					if outers['outers'].get(labels) is not None:
						outers['outers'][labels] -= 1
					else:
						outers['outers'][labels] = -1
					outers['expenses'] -= elem['prices']
		self.expenses_label.setText(f"Expenses: {outers['expenses']}")
		if reff is not None:
			reff.setText(str(outers['outers'][labels]))
		print(controllers)
		print(outers)

	def remove_submit(self, labels, reff):
		with open('./bin/properties.json', 'r+') as file:
			json_content = json.load(file)
		for element in list(json_content):
			for elem in json_content[element]:
				if elem['products'] == labels:
					if outers['outers'].get(labels) is not None:
						outers['outers'][labels] += 1
					else:
						outers['outers'][labels] = 0
					outers['expenses'] += elem['prices']
		self.expenses_label.setText(f"Expenses: {outers['expenses']}")
		if reff is not None:
			reff.setText(str(outers['outers'][labels]))

	def reset_submit(self):
		for i in controllers['labels']:
			i.setText('')

		self.expenses_label.setText('Expenses: ')
		self.reasons_label.setText('Reasons: ')

		self.expense_edit.clear()
		self.reason_edit.clear()

		global_var()

	def accept_submit(self):
		saves()
		self.reset_submit()
		global_var()

	def stats_submit(self):
		global mainWin
		mainWin = StatsWindow()
		main_window.setCentralWidget(mainWin)
		main_window.resize(450, 600)
		main_window.show()

	def menu_submit(self):
		global mainWin
		mainWin = MainWindow()
		scrolls = QScrollArea()
		scrolls.setWidget(mainWin)
		scrolls.setWidgetResizable(True)
		main_window.setCentralWidget(scrolls)
		main_window.resize(450, 600)
		main_window.show()

class StatsWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.stats_wrapper = QVBoxLayout()
		self.labels_templates()
		self.buttons_templates()
		self.setLayout(self.stats_wrapper)

	def buttons_templates(self):
		menus_button = QPushButton('Menus')
		menus_button.clicked.connect(self.menus_submit)
		expenses_button = QPushButton('Expenses')
		expenses_button.clicked.connect(self.expenses_submit)

		button_layout = QHBoxLayout()
		button_layout.addWidget(menus_button)
		button_layout.addWidget(expenses_button)

		current_button = QPushButton('Current')
		current_button.clicked.connect(self.current_button_submit)
		any_button = QPushButton('Any')
		any_button.clicked.connect(self.any_button_submit)

		button_layout2 = QHBoxLayout()
		button_layout2.addWidget(current_button)
		button_layout2.addWidget(any_button)

		self.stats_wrapper.addLayout(button_layout)
		self.stats_wrapper.addLayout(button_layout2)

	def labels_templates(self):
		layout1 = QVBoxLayout()
		layout1.setAlignment(Qt.AlignmentFlag.AlignLeft)
		self.moneys = QLabel('Moneys: ')
		layout1.addWidget(self.moneys)
		self.products = QLabel('Products: ')
		layout1.addWidget(self.products)
		self.expenses = QLabel('Expenses: ')
		layout1.addWidget(self.expenses)
		self.cuts = QLabel('Cuts: ')
		layout1.addWidget(self.cuts)

		layout2 = QVBoxLayout()
		layout2.setAlignment(Qt.AlignmentFlag.AlignLeft)
		self.bases = QLabel('Bases: ')
		layout2.addWidget(self.bases)
		self.originals = QLabel('Original: ')
		layout2.addWidget(self.originals)
		self.profits = QLabel('Profits: ')
		layout2.addWidget(self.profits)
		self.cleans = QLabel('Cleans: ')
		layout2.addWidget(self.cleans)

		layout_wrappers = QHBoxLayout()
		layout_wrappers.addLayout(layout1)
		layout_wrappers.addLayout(layout2)

		self.stats_wrapper.addLayout(layout_wrappers)
		self.current_button_submit()

	def any_button_submit(self):
		moneys = 0
		products = 0
		expenses = 0
		cuts = 0
		bases = 0
		originals = 0
		profits = 0
		for file in glob.glob('./*.json'):
			with open(file, 'r+') as file:
				json_content = json.load(file)
			for element in list(json_content):
				for elem in json_content[element].get('products', []):
					products += elem.get('numbers', 0)
					cuts += elem.get('cuts', 0)
					bases += elem.get('bases', 0)
					moneys += elem.get('prices', 0)
					originals += elem.get('original', 0)
					profits += elem.get('profits', 0)
				expenses += json_content[element].get('expenses', 0)
		cleans = profits + expenses

		self.moneys.setText(f'Moneys: {moneys}')
		self.products.setText(f'Products: {products}')
		self.expenses.setText(f'Expenses: {expenses}')
		self.cuts.setText(f'Cuts: {cuts}')

		self.bases.setText(f'Bases: {bases}')
		self.originals.setText(f'Originals: {originals}')
		self.profits.setText(f'Profits: {profits}')
		self.cleans.setText(f'Cleans: {cleans}')

	def current_button_submit(self):
		with open(location, 'r+') as file:
			json_content = json.load(file)
		moneys = 0
		products = 0
		expenses = 0
		cuts = 0
		bases = 0
		originals = 0
		profits = 0
		for element in list(json_content):
			for elem in json_content[element].get('products', []):
				products += elem.get('numbers', 0)
				cuts += elem.get('cuts', 0)
				bases += elem.get('bases', 0)
				moneys += elem.get('prices', 0)
				originals += elem.get('original', 0)
				profits += elem.get('profits', 0)
			expenses += json_content[element].get('expenses', 0)
		cleans = profits + expenses

		self.moneys.setText(f'Moneys: {moneys}')
		self.products.setText(f'Products: {products}')
		self.expenses.setText(f'Expenses: {expenses}')
		self.cuts.setText(f'Cuts: {cuts}')

		self.bases.setText(f'Bases: {bases}')
		self.originals.setText(f'Originals: {originals}')
		self.profits.setText(f'Profits: {profits}')
		self.cleans.setText(f'Cleans: {cleans}')

	def menus_submit(self):
		global mainWin
		mainWin = MainWindow()
		scrolls = QScrollArea()
		scrolls.setWidget(mainWin)
		scrolls.setWidgetResizable(True)
		main_window.setCentralWidget(scrolls)
		main_window.resize(450, 600)
		main_window.show()

	def expenses_submit(self):
		global mainWin, scrolls
		mainWin = ExpenseWindow()
		scrolls = QScrollArea()
		scrolls.setWidget(mainWin)
		scrolls.setWidgetResizable(True)
		main_window.setCentralWidget(scrolls)
		main_window.resize(450, 600)
		main_window.show()

def global_var():
	global controllers, stores, outers
	stores = {'products': {}, 'prices': 0, 'customers': 0, 'paybacks': 0}
	outers = {'outers': {}, 'expenses': 0, 'reasons': ''}
	controllers = {'labels': [], 'operators': '+'}

def saves():
	dates = str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
	jsonize = {}
	jsonize[dates] = {}
	if stores['prices']:
		jsonize[dates]['profits'] = stores['prices']
	if stores['customers']:
		paybacks = stores['customers'] - stores['prices']
		stores['paybacks'] += paybacks
		if paybacks > 0:
			jsonize[dates]['paybacks'] = paybacks
		elif paybacks < 0:
			jsonize[dates]['paybacks'] = paybacks
		jsonize[dates]['received'] = stores['customers']
	if stores['products']:
		jsonize[dates]['products'] = []
		for element in list(stores['products']):
			if stores['products'][element] > 0:
				with open('./bin/properties.json', 'r+') as file:
					json_content = json.load(file)
				for elem in list(json_content):
					for ele in json_content[elem]:
						if element == ele['products']:
							jsonize[dates]['products'].append(merge(ele, {'numbers': stores['products'][element]}))
	if outers['outers']:
		jsonize[dates]['outers'] = []
		for element in list(outers['outers']):
			with open('./bin/properties.json', 'r+') as file:
				json_content = json.load(file)
			for elem in list(json_content):
				for ele in json_content[elem]:
					if element == ele['products']:
						jsonize[dates]['outers'].append(merge(ele, {'numbers': outers['outers'][element]}))
	if outers['expenses']:
		jsonize[dates]['expenses'] = outers['expenses']
		if outers['reasons']:
			jsonize[dates]['reasons'] = outers['reasons']
	with open(location, 'r+') as file:
		json_content = json.load(file)
		file.seek(0)
		file.write(json.dumps(merge(json_content, jsonize), sort_keys = True, indent = 4))

if __name__ == "__main__":
	if os.path.isfile(location) is False:
		with open(location, 'w') as f:
			f.write('{}')
	os.chdir(os.path.dirname(sys.argv[0]))
	global_var()

	app = QApplication(sys.argv)
	main_window = QMainWindow()
	mainWin = MainWindow()
	scrolls = QScrollArea()
	scrolls.setWidgetResizable(True)
	scrolls.setWidget(mainWin)
	main_window.setCentralWidget(scrolls)
	main_window.setWindowTitle('Icelander v1.6')
	main_window.setWindowIcon(QIcon('icelander.ico'))
	main_window.resize(450, 600)
	main_window.show()
	app.exec()