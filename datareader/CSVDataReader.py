from datareader.AbstractDataReader import AbstractDataReader
import csv

class CSVDataReader(AbstractDataReader):
	def __init__(self, source):
		self.reader = csv.reader(open(source))
	
	def read(self):
		data = []
		for row in self.reader:
			if len(row) != 9:
				raise "Row {x + 1} in CSV {source} is not length 9 - aborted!"
			data.append(row)
		
		if len(data) != 9:
			raise "Column count in CSV {source} is not length 9 - aborted!"
			
		return data