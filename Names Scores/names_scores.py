# opens the file to be read
with open('names.txt', 'r') as namesFile:
    # reads first line of the file
    allNames = namesFile.readline()

    # splits line by specific character and adds to a list
    namesList = allNames.split(',')

# removes unwanted characters and adds to new clean names list
cleanNames = []
for roughName in namesList:
    cleanName = roughName.strip('"')
    cleanNames.append(cleanName)

# sorts clean names alphabetically
cleanNames.sort()
    
nameScore = 0
position = 1

# iterates through all clean names in cleanNames list
for name in cleanNames:
    # iterates through each character of the current name to add values
    # values are multiplied by their position in the list starting at 1
    # position increments +1 after each name score is calculated
    for letter in name:
        if letter == 'A':
            nameScore += 1 * position
        elif letter == 'B':
            nameScore += 2 * position
        elif letter == 'C':
            nameScore += 3 * position
        elif letter == 'D':
            nameScore += 4 * position
        elif letter == 'E':
            nameScore += 5 * position
        elif letter == 'F':
            nameScore += 6 * position
        elif letter == 'G':
            nameScore += 7 * position
        elif letter == 'H':
            nameScore += 8 * position
        elif letter == 'I':
            nameScore += 9 * position
        elif letter == 'J':
            nameScore += 10 * position
        elif letter == 'K':
            nameScore += 11 * position
        elif letter == 'L':
            nameScore += 12 * position
        elif letter == 'M':
            nameScore += 13 * position
        elif letter == 'N':
            nameScore += 14 * position
        elif letter == 'O':
            nameScore += 15 * position
        elif letter == 'P':
            nameScore += 16 * position
        elif letter == 'Q':
            nameScore += 17 * position
        elif letter == 'R':
            nameScore += 18 * position
        elif letter == 'S':
            nameScore += 19 * position
        elif letter == 'T':
            nameScore += 20 * position
        elif letter == 'U':
            nameScore += 21 * position
        elif letter == 'V':
            nameScore += 22 * position
        elif letter == 'W':
            nameScore += 23 * position
        elif letter == 'X':
            nameScore += 24 * position
        elif letter == 'Y':
            nameScore += 25 * position
        elif letter == 'Z':
            nameScore += 26 * position
        else:
            print("there's a problem")
    position += 1

print(nameScore)