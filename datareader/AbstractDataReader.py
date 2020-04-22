from abc import ABC, abstractmethod

class AbstractDataReader(ABC):
	@abstractmethod
	def __init__(self, source):
		pass

	@abstractmethod
	def read(self):
		pass