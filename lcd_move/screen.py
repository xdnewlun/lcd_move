class Screen:
	strings = []
	index = 0
	clear_space = "                "

	def __init__(self, strings, lcd):
		self.strings = strings
		self.lcd = lcd

	def moveDown(self):
		if(self.index+1 >= len(self.strings)):
			self.index = 0
		else:
			self.index+=1
		return

	def moveUp(self):
		if self.index-1 < 0:
			print('looped back')
			self.index = len(self.strings)
		else:
			print('went down')
			self.index -= 1
		print(self.index)
		return

	def removeString(self, index):
		del self.strings[index]
		return

	def insertString(self, index, string):
		self.strings.insert([index, string])
		return

	def addString(self, string):
		self.strings.append(string);
		return

	def clear(self):
		self.lcd.set_cursor(0,0)
		self.lcd.send_string(self.clear_space)
		self.lcd.set_cursor(1,0)
		self.lcd.send_string(self.clear_space)

	def display(self):
		self.clear()
		self.lcd.set_cursor(0,0)
		self.lcd.send_string(self.strings[self.index])
		self.lcd.set_cursor(1,0)
		
		second = self.index+1
		if(second >= len(self.strings)):
			second = 0

		self.lcd.send_string(self.strings[second])
		return