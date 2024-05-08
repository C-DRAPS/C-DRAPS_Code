# TODO: A lot of our raw water quality files have generic & meaningless names. This program renames files
#  to have meaningful names.
#  New names consists of:
#   1. State origin
#   2. Quarter (1,2,3,4,FULL)
#   3. Year pulled from

import csv
import os


# Gets a list of all .xlsx files in a folder (to convert to .csv)
def getFilePaths(path):
    files = []
    for fileName in os.listdir(path):
        if fileName != "2010 Modified Datasets":
            files.append(path + "/" + fileName)
    return files


def rename(filePath, basePath, quarter, year):
    # Load existing data
    dataset = []
    with open(filePath, "r") as csvFile:
        csvReader = csv.reader(csvFile)
        for line in csvReader:
            dataset.append(line)

    # Get state
    state = dataset[1][3]

    # Create new file w/ new name
    with open(basePath + "/" + year + " Modified Datasets/" + state.capitalize() + " Q" + quarter + " WATER SYSTEM SUMMARY " + year + ".csv", "w", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerows(dataset)


# TODO: This is main.
BASE_PATH = "SDWIS stuff/Original Datasets/2020/Modified"  # Toggles
QUARTER = "1"                             # Toggles
YEAR = "2010"                             # Toggles

for filePath in getFilePaths(BASE_PATH):
    rename(filePath, BASE_PATH, QUARTER, YEAR)
    print('Finished ' + '"' + filePath + '"')
