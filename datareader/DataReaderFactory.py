from datareader.CSVDataReader import CSVDataReader

class DataReaderFactory:
	def create(self, sourceName):
		if sourceName.endswith(".csv"):
			return CSVDataReader(sourceName)