import pickle
import json

def save_bin(dictionary, filename):    
   with open(filename, 'wb') as file:
       pickle.dump(dictionary, file)

def read_bin(filename):
    dict_data = {}
    with open(filename, 'rb') as file:
       dict_data = pickle.load(file)
    return dict_data    

def save_json(dictionary, filename):
    with open(filename, 'w') as file:
        json.dump(dictionary, file)

def read_json(filename):   
    dict_data = {}
    with open(filename, 'r') as file:
        dict_data = json.load(file)
    return dict_data

# Example usage:
print("Writing and reading bin file:")
test_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
save_bin(test_dict, 'data.bin')  
loaded_dict = read_bin('data.bin')
print(loaded_dict)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

print("\nWriting and reading json file:")
save_json(test_dict, 'data.json')  
loaded_dict = read_json('data.json')    
print(loaded_dict)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
