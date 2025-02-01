# Open the file in write mode ('w')
file = open('sample.txt', 'w')

# Write some content to the file
file.write('Hello, this is a sample text! how are you brother')

# Close the file to save changes
file.close()

##ANOTHER WAY 

with open('file.txt', 'w') as file:
    file.write('Hello, this is a sample text!how are you brother')

'''Reading the entire File'''
with open ("sample.txt",'r') as file:
    content =file.read()
    print(content)

##csv file can be read line by line

with open('sample.txt','r') as file:
    for line in file:
        print(line.strip())

import csv

# Define the data you want to write
data = [
    ['Name', 'Age', 'Country','address'],  # Header row
    ['John', 28, 'USA',7-9,12],
    ['Alice', 30, 'UK'],
    ['Bob', 25, 'Canada']
]

# Open the file in write mode ('w') and create the CSV file
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the rows to the CSV file
    writer.writerows(data)

print("CSV file 'output.csv' created successfully!")
with open('output.csv','r') as file:
    for line in file:
        print(line.strip())