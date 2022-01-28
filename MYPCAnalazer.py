class PC:
	name = 'My PC'
	processor = 'Intel Core'
	
	@staticmethod
	def start():
		print('PC is starting..')
		
	@staticmethod
	def restart(self):
		print('PC is restarting')
		
	def details(self):
		print('My PC name is:', self.name)
		print('It has',self.processor,'processor.')
