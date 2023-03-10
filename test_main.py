import pytest
import main
import os
import csv

# Creating lists to store the length of the lists
accessories = []
clothing = []
household_cleaners = []

# Opens up accessories.csv for reading
with open("./fixtures/accessories.csv", "r") as temp:
        reader = csv.reader(temp)
        accessories = list(reader)[1:]

# Opens up clothing.csv for reading
with open("./fixtures/clothing.csv", "r") as temp:
        reader = csv.reader(temp)
        clothing = list(reader)[1:]

# Opens up household_cleaners.csv for reading
with open("./fixtures/household_cleaners.csv", "r") as temp:
        reader = csv.reader(temp)
        household_cleaners = list(reader)[1:]

# Function to compare if the output CSV matches up with the input CSVs
def rowLookup(filename, row):

    # Opens up the input file
    with open(filename, "r") as temp:

        reader = csv.reader(temp)
        fileContents = list(reader)[1:]
        # Checking to see if the rows are matching between the
        # input CSV and output CSV
        if row in fileContents:
            return True

    return False

# PyTest for accessories.csv and clothing.csv
def test_accessories_clothing():

    # Runs the command to generate the output1.csv
    os.system("python main.py ./fixtures/accessories.csv ./fixtures/clothing.csv > ./output/output1.csv")
    
    file = "./output/output1.csv"

    outputFile = []

    # Opens up the output1.csv
    with open(file, "r") as tempFile:

        reader = csv.reader(tempFile)
        outputFile = list(reader)[1:]

    clothingCount = 0
    accessoriesCount = 0

    # Iterates through both accessories.csv and clothing.csv
    # And checks to see if the filename that was added to
    # the output1.csv matches with the correct row
    # Also creates a counter
    for row in outputFile:
        if row[2] == "accessories.csv":
            if rowLookup("./fixtures/accessories.csv", row[:-1]) == True:
                accessoriesCount = accessoriesCount + 1

        elif row[2] == "clothing.csv":
            if rowLookup("./fixtures/clothing.csv", row[:-1]) == True:
                clothingCount = clothingCount + 1
            
    # Checking to see if the length is adding up properly
    assert clothingCount == len(clothing)
    assert accessoriesCount == len(accessories)
        
# PyTest for accessories.csv and household_cleaners.csv
def test_accessories_household_cleaners():

    os.system("python main.py ./fixtures/accessories.csv ./fixtures/household_cleaners.csv > ./output/output2.csv")
    
    file = "./output/output2.csv"

    outputFile = []

    with open(file, "r") as tempFile:

        reader = csv.reader(tempFile)
        outputFile = list(reader)[1:]

    accessoriesCount = 0
    householdCleanersCount = 0

    for row in outputFile:
        if row[2] == "accessories.csv":
            if rowLookup("./fixtures/accessories.csv", row[:-1]) == True:
                accessoriesCount = accessoriesCount + 1

        elif row[2] == "household_cleaners.csv":
            if rowLookup("./fixtures/household_cleaners.csv", row[:-1]) == True:
                householdCleanersCount = householdCleanersCount + 1
            
    assert householdCleanersCount == len(household_cleaners)
    assert accessoriesCount == len(accessories)
        
# PyTest for clothing.csv and household_cleaners.csv
def test_clothing_household_cleaners():

    os.system("python main.py ./fixtures/clothing.csv ./fixtures/household_cleaners.csv > ./output/output3.csv")
    
    file = "./output/output3.csv"

    outputFile = []

    with open(file, "r") as tempFile:

        reader = csv.reader(tempFile)
        outputFile = list(reader)[1:]

    clothingCount = 0
    householdCleanersCount = 0

    for row in outputFile:
        if row[2] == "clothing.csv":
            if rowLookup("./fixtures/clothing.csv", row[:-1]) == True:
                clothingCount = clothingCount + 1

        elif row[2] == "household_cleaners.csv":
            if rowLookup("./fixtures/household_cleaners.csv", row[:-1]) == True:
                householdCleanersCount = householdCleanersCount + 1
            
    assert clothingCount == len(clothing)
    assert householdCleanersCount == len(household_cleaners)
        
# PyTest for accessories.csv, clothing.csv, and household_cleaners.csv
def test_accessories_clothing_household_cleaners():

    os.system("python main.py ./fixtures/accessories.csv ./fixtures/clothing.csv ./fixtures/household_cleaners.csv > ./output/output4.csv")
    
    file = "./output/output4.csv"

    outputFile = []

    with open(file, "r") as tempFile:

        reader = csv.reader(tempFile)
        outputFile = list(reader)[1:]

    accessoriesCount = 0
    clothingCount = 0
    householdCleanersCount = 0

    for row in outputFile:
        if row[2] == "accessories.csv":
            if rowLookup("./fixtures/accessories.csv", row[:-1]) == True:
                accessoriesCount = accessoriesCount + 1

        elif row[2] == "clothing.csv":
            if rowLookup("./fixtures/clothing.csv", row[:-1]) == True:
                clothingCount = clothingCount + 1
        
        elif row[2] == "household_cleaners.csv":
            if rowLookup("./fixtures/household_cleaners.csv", row[:-1]) == True:
                householdCleanersCount = householdCleanersCount + 1
            
    assert clothingCount == len(clothing)
    assert accessoriesCount == len(accessories)
    assert householdCleanersCount == len(household_cleaners)