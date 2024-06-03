import json
import argparse

parser = argparse.ArgumentParser(description="This is for taking user input")
parser.add_argument('--json_file', type=str, help='this will take json file as an input')
parser.add_argument('--key', type=str, help='this will key of the json file')
parser.add_argument('--value', type=str, help='this is the search value')


# Load the JSON data from a file
def load_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError as e:
    	print("Error: The directory '{filename}' was not found. Details: {e}")
    except Exception as e:
        print("An unexpected error occurred: {e}")

# Function to search for a specific key-value pair in the JSON data
def search_json(data, search_key, search_value):
    results = []
    
    def search(item):
        if isinstance(item, dict):
            for key, value in item.items():
                if key == search_key and value == search_value:
                    results.append(item)
                if isinstance(value, (dict, list)):
                    search(value)
        elif isinstance(item, list):
            for element in item:
                search(element)
    
    search(data)
    return results

# Example usage
arge = parser.parse_args()
filename = arge.json_file
data = load_json(filename)
search_key = arge.key
search_value = arge.value
results = search_json(data, search_key, search_value)

print(f"Search results for {search_key} = {search_value}:")
for result in results:
    print(result)
