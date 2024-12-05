#TASK 1

#Reading the data
data = [line.strip() for line in open("1_data.txt", 'r').readlines()]

#Initializing the result
result_1 = 0

#Iterating through the lines of the data
for line in data:
    numeric_chars = [char for char in line if char.isnumeric()] #Extracting the numeric characters
    if numeric_chars:
        first = numeric_chars[0] #First numeric character
        last = numeric_chars[-1] #Last numeric character
        result_1 += int(first + last)

print(f"Result 1 = {result_1}")

#TASK 2

#Initializing the second result
result_2 = 0

#Dictionary to replace alphabetical numbers with their numeric counterparts with padded first and last letters for overlap protection
numbers = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

#Initializing the new data
data_2 = []

#Iterating through every line of the new data
for i, line in enumerate(data):
    new_line = line
    for key in numbers: #For every number in the dictionary
        if key in new_line: #If a match is found
            new_line = new_line.replace(key, numbers[key]) #Replace the match with the padded digit as
    data_2.append(new_line)

#Iterating through the lines of the new data
for line in data_2:
    numeric_chars = [char for char in line if char.isnumeric()] #Extracting the numeric characters
    if numeric_chars:
        first = numeric_chars[0] #First numeric character
        last = numeric_chars[-1] #Last numeric character
        result_2 += int(first + last)

print(f"Result 2 = {result_2}")