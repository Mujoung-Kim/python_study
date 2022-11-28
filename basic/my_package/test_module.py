def hello_world():
	print('hello_world')

def greeting(name):
	print(f'welcome to {name}.')

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f'name: {self.name}, age: {self.age}'