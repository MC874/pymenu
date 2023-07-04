
import os
import sys
import glob
import time
import json
import datetime
from jsonmerge import merge, Merger
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit, QVBoxLayout, QMainWindow, QScrollArea
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, QTimer, QCoreApplication
from PySide6.QtCore import Qt

location = f"./{str(datetime.datetime.now().strftime('%Y%m%d'))}.json"

class MainWindow(QWidget): 
	def __init__(self):
		super().__init__()
		self.wrappers = QVBoxLayout()

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
				product_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
				for _ in range(4):
					texti = json_content[element][products_num]
					timers = QTimer()
					btn_layout = QVBoxLayout()
					btn_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
					btn_label = QLabel()
					timers.timeout.connect(lambda: self.updaters(texti))
					timers.start(100)
					btn = QPushButton()
					btn.setIcon(QIcon(json_content[element][products_num]['icons']))
					btn.setFixedSize(100, 100)
					btn.setIconSize(QSize(110, 110))
					btn.clicked.connect(lambda *args, texti=texti, btn_label=btn_label: self.templates(texti, btn_label))
					btn_layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)
					btn_layout.addWidget(btn_label, alignment=Qt.AlignmentFlag.AlignCenter)
					product_layout.addLayout(btn_layout)
					if not (products_num == products_total):
						products_num += 1
					else:
						break
				section_layout.addLayout(product_layout)
				layout_num += 1
			self.wrappers.addLayout(section_layout)
		
		self.props_templates()
		self.section_templates()
		self.button_templates()
		self.setLayout(self.wrappers)

	def templates(self, texti, label):
		controllers['lists'].append(label)
		if controllers['current_products'].get(texti['products']) is not None:
			controllers['current_products'][texti['products']] += 1
		else:
			controllers['current_products'][texti['products']] = 1
		label.setText(f"{controllers['current_products'][texti['products']]}")
		controllers['current_prices'] += texti['prices']
		label.setText(str(controllers['current_products'][texti['products']]))
		self.moneys_label.setText(f"Total Moneys: {controllers['current_prices']}")

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
		expenses_layout = QHBoxLayout()
		expenses_label = QLabel('Expenses: ')
		self.expenses_edit = QLineEdit()
		self.expenses_edit.editingFinished.connect(self.expenses_submit)
		expenses_layout.addWidget(expenses_label)
		expenses_layout.addWidget(self.expenses_edit)

		reasons_layout = QHBoxLayout()
		reasons_label = QLabel('Reasons: ')
		self.reasons_edit = QLineEdit()
		self.reasons_edit.editingFinished.connect(self.reasons_submit)
		reasons_layout.addWidget(reasons_label)
		reasons_layout.addWidget(self.reasons_edit)

		customer_layout = QHBoxLayout()
		customer_label = QLabel('Customers: ')
		self.customer_edit = QLineEdit()
		self.customer_edit.editingFinished.connect(self.customer_submit)
		customer_layout.addWidget(customer_label)
		customer_layout.addWidget(self.customer_edit)

		section_wrappers = QVBoxLayout()
		section_label = QLabel('Section')
		section_wrappers.addLayout(expenses_layout)
		section_wrappers.addLayout(reasons_layout)
		section_wrappers.addLayout(customer_layout)

		self.wrappers.addLayout(section_wrappers)

	def button_templates(self):
		accept_button = QPushButton('Accept')
		accept_button.clicked.connect(self.accept_submit)
		reset_button = QPushButton('Reset')
		reset_button.clicked.connect(self.reset_submit)

		current_button = QPushButton('Current')
		current_button.clicked.connect(self.current_button_submit)
		any_button = QPushButton('Any')
		any_button.clicked.connect(self.any_button_submit)

		button_layout1 = QHBoxLayout()
		button_layout1.addWidget(accept_button)
		button_layout1.addWidget(reset_button)

		button_layout2 = QHBoxLayout()
		button_layout2.addWidget(current_button)
		button_layout2.addWidget(any_button)

		button_wrappers = QVBoxLayout()
		button_wrappers.addLayout(button_layout1)
		button_wrappers.addLayout(button_layout2)

		self.wrappers.addLayout(button_wrappers)

	def expenses_submit(self):
		if int(self.expenses_edit.text()) < 999:
			controllers['current_expenses'] += -int(self.expenses_edit.text()) * 1000
		else:
			controllers['current_expenses'] +=  -int(self.expenses_edit.text())

	def customer_submit(self):
		if int(self.customer_edit.text()) < 999:
			controllers['customer_moneys'] += int(self.customer_edit.text()) * 1000
		else:
			controllers['customer_moneys'] += int(self.customer_edit.text())
	
	def reasons_submit(self):
		controllers['current_reasons'] += self.reasons_edit.text()

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

	def reset_submit(self):
		for i in controllers['lists']:
			i.setText('')

		self.moneys_label.setText('Total Moneys: ')
		self.expense_label.setText('Total Expenses: ')
		self.reports_label.setText('Total Reports: ')

		self.incomes_label.setText('Total Incomes: ')
		self.earnings_label.setText('Total Earnings: ')
		self.cuts_label.setText('Total Cuts: ')	

		self.expenses_edit.clear()
		self.reasons_edit.clear()
		self.customer_edit.clear()

		global_var()

	def accept_submit(self):
		self.warning_label.setText('')
		self.paybacks_label.setText('')
		dates = str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
		jsonize = {}
		jsonize[dates] = {}
		if controllers['current_prices']:
			jsonize[dates]['profits'] = controllers['current_prices']
		if controllers['customer_moneys']:
			paybacks = controllers['customer_moneys'] - controllers['current_prices']
			if paybacks > 0:
				self.paybacks_label.setText(f'*Paybacks: {paybacks}')
				jsonize[dates]['paybacks'] = paybacks
			elif paybacks < 0:
				self.warning_label.setText(f'*Money: {paybacks}')
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
		self.reset_submit()
		global_var()

def global_var():
	global controllers
	controllers = {'current_products': {}, 'current_prices': 0, 'customer_moneys': 0, 'current_expenses': 0, 'current_reasons': '', 'symbols': '', 'lists': []}

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
	scrolls.setWidget(mainWin)
	main_window.setCentralWidget(scrolls)
	main_window.setWindowTitle('Icelander v1.2')
	main_window.setWindowIcon(QIcon('icelander.ico'))
	main_window.show()
	app.exec()