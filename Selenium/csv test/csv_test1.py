import csv

# CSV file path
csv_file_path = 'C:/files/data.csv'

# Sample data
data = [
    {'name': 'Alice', 'location': 'New York', 'link': 'http://example.com/alice'},
    {'name': 'Bob', 'location': 'Los Angeles', 'link': 'http://example.com/bob'},
    {'name': 'Charlie', 'location': 'Chicago', 'link': 'http://example.com/charlie'},   
    {'name': 'curlie', 'location': 'Chicago', 'link': 'cu'},
    {'name': 'Charlie', 'location': 'Chicago', 'link': 'http://example.com/cha'}
]

# Read existing data from the file
existing_data = [] # cria lista em branco
with open(csv_file_path, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        existing_data.append(row) # add na lista o que já existe no csv 

# Identify the last populated line
last_populated_line = len(existing_data) # pega a qtde linhas populadas na lista existentes

# Append new data to the file starting from the next line after the last populated line
with open(csv_file_path, 'a', newline='') as csvfile:
    fieldnames = ['name', 'location', 'link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write new data only for lines that aren't populated
    for i, row in enumerate(data):
        if i >= last_populated_line:
            writer.writerow(row)
