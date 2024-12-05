import re

#TASK 1

#Reading the data line by line
data = [line for line in open("2_data.txt", 'r').readlines()]

#Dictionary for the color limits
limits = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}

#Initializing the final result
result_1 = 0

#Creating list of lists for the games (each game list now has the draws as separate strings)
for i, game in enumerate(data):
    data[i] = re.sub(r"^Game \d+: ", "", game).strip().split("; ")

#Iterating through the data
for i, game in enumerate(data): #For every game
    increment = True #Initial flag for increment set to True
    for draw in game: #For every draw
        for colour, limit in limits.items(): #For every colour in the limits dictionary
            if colour in draw: #If the current colour is in the draw
                match = re.search(r"(\d+)\s+" + re.escape(colour), draw) #Creating a variable for the regex match for the number+colour pair
                count = int(match.group(1)) #Extracting the number from the match (the first capturing group of the regex)
                if count > limit: #If the count is higher than the limit
                    increment = False #Set the flag False
    if increment:
        result_1 += (i + 1) #Incrementing the result if the flag allows it
                
print(f"Result 1 = {result_1}")

#TASK 2

#Initializing the second result
result_2 = 0

#Iterating through the data (each game)
for i, game in enumerate(data):
    #Initializing the max numbers dictionary as 0 for each colour
    max_numbers = {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    }
    for draw in game: #For each draw
        for colour, number in max_numbers.items(): #For each item in the max numbers dictionary
            if colour in draw: #If the colour is in the draw
                match = re.search(r"(\d+)\s+" + re.escape(colour), draw) #Creating a variable for the regex match for the number+colour pair
                count = int(match.group(1)) #Extracting the number from the match (the first capturing group of the regex)
                if count > max_numbers[colour]: #If the count is higher than the current count in the max numbers dictionary
                    max_numbers[colour] = count #Update the count with the higher one
    power = 1 #Initializin the power as 1
    for colour, number in max_numbers.items(): #Getting the product of the max number counts
        power *= number 
    result_2 += power

print(f"Result 2 = {result_2}")