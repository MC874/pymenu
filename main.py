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

class interface(QWidget):
    def __init__(self):
        super().__init__()
        wrappers = QVBoxLayout()

        with open('./bin/properties.json', 'r+') as file:
            json_content = json.load(file)
        for section in list(json_content):
            self.products_num = 0
            self.layout_num = 0
            while not self.products_num == len(json_content[section]):
                exec(f'{section}_layout{self.layout_num} = QHBoxLayout()')
                exec(f'{section}_layout{self.layout_num}.setAlignment(Qt.AlignmentFlag.AlignLeft)')
                for _ in range(4):
                    names = json_content[section][self.products_num - 1]['products']
                    pseudo = json_content[section][self.products_num - 1]['products'].replace(' ', '_').lower()
                    def __templates__(texti):
                        if controllers['current_products'].get(texti) is not None:
                            controllers['current_products'][texti] += 1
                        else:
                            controllers['current_products'][texti] = 1
                        print(controllers)
                        exec(f'{pseudo}_label.setText("{controllers["current_products"][names]}")')
                    locals()[f'{pseudo}_submit'] = __templates__
                    exec(f'{pseudo}_layout = QVBoxLayout()')
                    exec(f'{pseudo}_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)')
                    exec(f'{pseudo}_button = QPushButton()')
                    exec(f'globals()["{pseudo}_label"] = QLabel()')
                    exec(f'{pseudo}_button.setFixedSize(100, 100)')
                    exec(f'{pseudo}_button.setIcon(QIcon("{json_content[section][self.products_num - 1]["icons"]}"))')
                    exec(f'{pseudo}_button.setIconSize(QSize(110, 110))')
                    exec(f'{pseudo}_button.clicked.connect({pseudo}_submit)')
                    exec(f'{pseudo}_layout.addWidget({pseudo}_button, alignment=Qt.AlignmentFlag.AlignCenter)')
                    exec(f'{pseudo}_layout.addWidget({pseudo}_label, alignment=Qt.AlignmentFlag.AlignCenter)')
                    exec(f'{section}_layout{self.layout_num}.addLayout({pseudo}_layout)')
                    if not self.products_num == len(json_content[section]):
                        self.products_num += 1
                exec(f'wrappers.addLayout({section}_layout{self.layout_num})')
                self.layout_num += 1
        self.setLayout(wrappers)

def global_var():
    global controllers
    controllers = {'current_products': {}, 'current_prices': 0, 'customer_moneys': 0, 'current_expenses': 0, 'current_reasons': ''}

if os.path.isfile(location) is False:
    with open(location, 'w') as f:
        f.write('{}')
os.chdir(os.path.dirname(sys.argv[0]))
global_var()

app = QApplication()
window = interface()
window.show()
app.exec()