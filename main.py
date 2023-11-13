import sys

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QPushButton, QWidget

from ui.base_qt_ui.ui_graph import Ui_Graph

row_base = 6
col_base = 200
pixel_size = 5


class System(QWidget):
	def __init__(self, color, parent=None):
		super(System, self).__init__(parent)
		self.color = color
		self.buttons = []
		self.end = 0
		self.level = 0
		self.dicct = {}
		self.time = 20
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(10)
		font.setBold(True)
		pushButton_reset = QPushButton('Reset', self)
		pushButton_reset.setFont(font)
		pushButton_reset.setGeometry(1010, 0, 50, 30)
		pushButton_reset.clicked.connect(self.buttons_reset)
		self.form_button()

	def form_button(self):
		for row in range(row_base):
			for col in range(col_base):
				button = QPushButton(f"", self)
				button.setGeometry(pixel_size * col, pixel_size * row, pixel_size, pixel_size)
				button.setObjectName(f'button{str(col + col_base * row).zfill(4)}')
				button.setStyleSheet(f"background-color: white")
				button.clicked.connect(self.change_button_color)
				self.buttons.append(button)
		pass

	def change_color(self):
		self.setStyleSheet(f"background-color: {self.color.name()};")

	def change_button_color(self):
		button = app.focusWidget()
		if button.palette().button().color().name() != '#ffffff':
			button.setStyleSheet(f"background-color: {self.color.name()};")
		else:
			button.setStyleSheet("background-color: white")
		self.draw_hor_line(button.objectName())

	def draw_hor_line(self, name: str):
		number = int(name[-4:])
		col = number % col_base
		row = number // col_base
		if self.end < col:
			for i in range(self.end, col + 1):
				if row < 3:
					row = 0
					self.buttons[i].setStyleSheet(f"background-color: {self.color}")
				else:
					row = 5
					self.buttons[i + (row_base - 1) * col_base].setStyleSheet(f"background-color: {self.color}")
			if self.level != row and self.end != 0:
				for j in range(row_base):
					self.buttons[j * col_base + self.end].setStyleSheet(f"background-color: {self.color}")
			self.end = col
			self.level = row

	def buttons_reset(self):
		self.get_data()
		for i in range(col_base * row_base):
			self.buttons[i].setStyleSheet(f"background-color: white")
		self.end = 0
		self.level = 0

	def get_data(self):
		for row in range(0, row_base, 5):
			for col in range(col_base):
				if self.buttons[col + row * col_base].palette().button().color().name() != '#ffffff':
					if col in self.dicct:
						self.dicct[col] += ((row // 5) ^ 1) + 1
					else:
						self.dicct[col] = (row // 5) ^ 1
		return self.convert_dict_to_str()

	def convert_dict_to_str(self):
		str = ''
		for key in range(len(self.dicct)):
			if self.dicct[key] == 2:
				if self.dicct[key - 1] == 0:
					str += f'0:{(key + 1) * self.time}µs; '
				elif self.dicct[key - 1] == 1:
					str += f'1:{(key + 1) * self.time}µs; '
		if len(self.dicct) != 0 and self.dicct[len(self.dicct) - 1] == 0:
			str += f'0:{len(self.dicct) * self.time}µs; '
		elif len(self.dicct) != 0 and self.dicct[len(self.dicct) - 1] == 1:
			str += f'1:{len(self.dicct) * self.time}µs; '

		self.dicct.clear()
		return str[:-2]

	def set_time_step(self, value):
		self.time = value



class Graph(QtWidgets.QMainWindow):

	def __init__(self):
		super().__init__()
		self.ui = Ui_Graph()
		self.ui.setupUi(self)
		self.end = 0
		self.level = 0
		self.str = ''
		self.sys_array1 = []
		self.sys_array2 = []
		self.count_axle = 0
		self.count_sys1 = 0
		self.count_sys2 = 0
		self.system1 = System('red')
		self.system1.setParent(self)
		self.system2 = System('blue')
		self.system2.setParent(self)
		self.ui.button_trans.clicked.connect(self.buttons_trans)
		self.ui.button_reset_count.clicked.connect(self.button_reset_count)

	def resizeEvent(self, event) -> None:
		super().resizeEvent(event)
		self.system1.setGeometry(60, 40, 1060, 30)
		self.system2.setGeometry(60, 85, 1060, 30)

	def buttons_trans(self):
		self.system1.set_time_step(int(self.ui.spinBox.text()))
		self.system2.set_time_step(int(self.ui.spinBox.text()))
		str1 = self.system1.get_data()
		str2 = self.system2.get_data()
		self.str = f"SYS1({str1}); SYS2({str2})"
		if self.str != "SYS1(); SYS2()":
			self.ui.textEdit.setText(self.str)
		else:
			self.ui.textEdit.setText('')
		self.form_mass_data(self.sys_array1, str1)
		self.form_mass_data(self.sys_array2, str2)
		self.find_axle(self.sys_array1, self.sys_array2, len(self.sys_array1))
		self.sys_array1.clear()
		self.sys_array2.clear()

	def button_reset_count(self):
		self.count_axle = 0
		self.count_sys1 = 0
		self.count_sys2 = 0
		self.ui.lineEdit_2.setText(str(self.count_axle))
		self.ui.lineEdit_3.setText(str(self.count_sys1))
		self.ui.lineEdit_4.setText(str(self.count_sys2))

	def form_mass_data(self, sys_array, str):
		last = 0
		str = str.replace('u', 'µ').replace(' ', '').replace(';', '')
		count_ex = str.count('µs')
		for _ in range(count_ex):
			sys_value = int(str[str.find(':') - 1])
			sys_count = int(str[str.find(':') + 1:str.find('µs')])
			for __ in range(last//20, sys_count//20):
				sys_array.append(sys_value)
			str = str[str.find('µs')+2:]
			last = sys_count
		pass

	def find_axle(self, mass1, mass2, size: int):
		count_type1_p = 0
		count_type2_p = 0
		count_type3_p = 0
		count_type1_m = 0
		count_type2_m = 0
		count_type3_m = 0
		length_single = 50
		length_both = 10
		length_alone = 10

		for i in range(size):
			if mass1[i] == 0 and mass2[i] == 1 and (count_type1_m + count_type2_m) < length_single:
				count_type1_m = 0
				count_type2_m = 0
				count_type3_m = 0
				count_type1_p += 1
			elif mass1[i] == 1 and mass2[i] == 0 and (count_type1_p + count_type2_p) < length_single:
				count_type1_p = 0
				count_type2_p = 0
				count_type3_p = 0
				count_type1_m += 1
			elif mass1[i] == 0 and mass2[i] == 0 and count_type1_p >= length_alone and count_type3_p == 0:
				count_type1_m = 0
				count_type2_m = 0
				count_type3_m = 0
				count_type2_p += 1
			elif mass1[i] == 0 and mass2[i] == 0 and count_type1_m >= length_alone and count_type3_m == 0:
				count_type1_p = 0
				count_type2_p = 0
				count_type3_p = 0
				count_type2_m += 1
			elif mass1[i] == 1 and mass2[i] == 0 and count_type2_p >= length_both and (count_type1_p + count_type2_p) >= length_single:
				count_type1_m = 0
				count_type2_m = 0
				count_type3_m = 0
				count_type3_p += 1
				if (count_type2_p + count_type3_p) >= length_single:
					self.count_axle += 1
					count_type1_p = 0
					count_type2_p = 0
					count_type3_p = 0
			elif mass1[i] == 0 and mass2[i] == 1 and count_type2_m >= length_both and (count_type1_m + count_type2_m) >= length_single:
				count_type1_p = 0
				count_type2_p = 0
				count_type3_p = 0
				count_type3_m += 1
				if (count_type2_m + count_type3_m) >= length_single:
					self.count_axle -= 1
					count_type1_m = 0
					count_type2_m = 0
					count_type3_m = 0
			else:
				count_type1_p = 0
				count_type2_p = 0
				count_type3_p = 0
				count_type1_m = 0
				count_type2_m = 0
				count_type3_m = 0
		self.ui.lineEdit_2.setText(str(self.count_axle))
		pass


# 0:1000us1:2500us0:4000us

# SYS1(0:1000us;  1:2500us;  0:4000us);SYS2(0:1300us;   1:2800us;  0:4000us)
# SYS1(0:d1000us; 1:d1500us; 0:d1500us);SYS2(0:d1300us; 1:d1500us; 0:d1200us)


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	graph = Graph()
	graph.show()
	sys.exit(app.exec())