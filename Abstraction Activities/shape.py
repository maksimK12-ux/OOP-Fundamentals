from abc import ABC, abstractmethod
 
class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass
	
class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
		
	def perimeter(self):
		return 2 * 3.14 * self.radius
	
	def area(self):
		return 3.14 * self.radius ** 2
	
	def volume(self):
		return 4/3 * 3.14 * self.radius ** 3 
	
class Rectangle(Shape):
	def __init__(self, width, height, length):
		self.width = width
		self.height = height
		self.length = length

	def perimeter(self):
			return 2 * (self.width + self.height)

	def area(self):
		return self.width * self.height

def volume(self):
	return self.width * self.height * self.length
	
class Volume(Shape):
	def __init__(self, volume):
		self.volume = volume