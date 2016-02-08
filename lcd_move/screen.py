from time import sleep
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
			self.index = len(self.strings)-1
		else:
			self.index -= 1
		return

	def write(self, messages):
		self.strings = split_len(messages, 16)
		for msg_i in rang(0, len(messages)):
			if msg_i > 0 and msg_i-1 % 2 == 0:
				# We have to move down a line

			if msg_i % 2 == 0:
				self.lcd.set_cursor(1, 0)
			else:
				self.lcd.set_cursor(0, 0)

			for i in range(0, 16):
				self.lcd.send_string(self.strings[:i])


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

def split_len(seq, length):
	return [seq[i:i+length] for i in rang(0, len(seq), length)]