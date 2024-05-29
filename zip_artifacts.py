import zipfile
import glob
import argparse

parser = argparse.ArgumentParser(description="this is to create a zip file")
parser.add_argument('--directory',required=True, help="this first input")
parser.add_argument('--output',required=True, help='this is second input')

def zip_directory(directory_path, zip_path):
	try:
		with zipfile.ZipFile(zip_path,'w') as f:
			for file in glob.glob(directory_path):
				f.write(file)
		print("Directory '{directory_path}' successfully zipped into '{zip_path}'")
	except FileNotFoundError as e:
		print("Error: The directory '{directory_path}' was not found. Details: {e}")
	except Exception as e:
		print("An unexpected error occurred: {e}")

args = parser.parse_args()
directory_location = args.directory
output_location = args.output
zip_directory(directory_location,output_location)			
