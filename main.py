import argparse

from utility.utility import GenericUtility

def get_arguments():
	parser = argparse.ArgumentParser()
	
	parser.add_argument("-i", "--input", type=GenericUtility.file_exists, required=True)
	parser.add_argument("-o", "--output", type=GenericUtility.file_not_exists, required=True)
			
	return parser.parse_args()

def main():
	try:
		args = get_arguments()
		print("Hello world!")
	except Exception as e: 
		print (e.strerror)		
	
# Run the main method if ran from the command line
if __name__ == "__main__":
	main()