# TODO: This program searches through any file and gives you the raw line. That's it. VERY useful when 
#  manually debugging & conducting data validation.
import csv
import storage
from tabulate import tabulate

# 1. Figure out which file you want to get
metaData = storage.getPath_FEMA_22Years()  # Gets file location from storage.py
filename = metaData[0]
baseYearIndex = metaData[1]
countyIndex = metaData[2]
stateIndex = metaData[3]
disasterTypeIndex = metaData[4]


# 2. Read file
dataset = []
with open(filename, "r") as csvFile:
    csvReader = csv.reader(csvFile)
    for line in csvReader:
        dataset.append(line)
    dataset.pop(0)  # Pop headers


# 3. Figure out criteria
prefCounty = "Allegany"  # use ".find()" since may not be standardized
prefState = "NY"  # Abbr.
prefDisaster = "Other"

stateToggle = True  # Use this for reservations....True = Want Specific-State

# 3a. Search file, based on criteria (only run one of these at a time)
lineNum = 1  # TODO: State Toggle
for line in dataset:
    if not stateToggle:
        if (line[countyIndex].find(prefCounty) != -1) and prefDisaster == line[disasterTypeIndex]:
            print(str(lineNum) + ". " + str(line))
    else:
        if (line[countyIndex].find(prefCounty) != -1) and prefDisaster == line[disasterTypeIndex] and prefState == line[stateIndex]:
            print(str(lineNum) + ". " + str(line))
    lineNum += 1


# 3a. Search file, based on criteria (only run one of these at a time)
# lineNum = 1  # TODO: State-Isolated, use for small-area disasters
# for line in dataset:
#     if prefDisaster == line[disasterTypeIndex] and prefState == line[stateIndex]:
#         print(str(lineNum) + ". " + str(line))
#     lineNum += 1


# 3a. Search file, based on criteria (only run one of these at a time)
# lineNum = 1  # TODO: State-Specific, same as #1
# for line in dataset:
#     if (line[countyIndex].find(prefCounty) != -1) and prefDisaster == line[disasterTypeIndex] and prefState == line[stateIndex]:
#         print(str(lineNum) + ". " + str(line))
#     lineNum += 1
