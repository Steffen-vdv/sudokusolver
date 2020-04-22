import argparse

from utility.GenericUtility import GenericUtility
from datareader.DataReaderFactory import DataReaderFactory

def get_arguments():
	parser = argparse.ArgumentParser()
	
	parser.add_argument("-i", "--input", type=GenericUtility.file_exists, required=True)
			
	return parser.parse_args()

def main():
	try:
		args = get_arguments()
		inputSource = args.input
		
		dataReaderFactory = DataReaderFactory()
		dataReader = dataReaderFactory.create(inputSource)
		sudokuBoard = dataReader.read()			
	except Exception as e: 
		print (e.strerror)		
	
# Run the main method if ran from the command line
if __name__ == "__main__":
	main()