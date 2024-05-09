# TODO: Reads a RAW FEMA dataset -> Assigns to FEMA disaster (in "County Data.csv" file).
#  program does NOT assign IDs or standardize names. Still utilizes raw county names.
#  This program works independent of what names are inside of our FEMA Datasets.

import csv
import os
from tabulate import tabulate


# Get all folder names in the "2000_2005 FEMA Disasters" Folder
def getFolderNames(clean):
    folders = os.listdir("DRASTIC File Structure Copycat/2000_2009 FEMA Disasters")

    if clean:
        newFolders = []
        # Strip ' Disasters' keyword from names
        for folder in folders:
            newFolders.append(folder.removesuffix(" Disasters"))
    else:
        newFolders = folders

    return newFolders


# Given an array [[all bio incidents], [all chem incidents], [etc.]] for a given yearSet -> Assign
# sub array data to "County Data.csv" file. IncidentType & Folders are 100% aligned.
def sortToFolder(yearType, dataset):
    basePath = "DRASTIC File Structure Copycat/"
    match yearType:
        case 1:
            basePath += "2000_2009 FEMA Disasters/"
        case 2:
            basePath += "2010_2019 FEMA Disasters/"
        case 3:
            basePath += "2020+ FEMA Disasters/"

    i = 0  # Helps pull specific index from dataset
    for folderName in getFolderNames(clean=False):
        path = basePath + folderName + "/County Data.csv"  # TODO: ~

        print("Writing to File Struct - " + path)
        with open(path, "w", newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            csvWriter.writerow(["state", "declarationDate", "incidentType", "designatedArea", "FID"])
            csvWriter.writerows(dataset[i])
        i += 1  # Gets next dataset (bio, chem, etc.)


# Gets a dataset, given the base year.
def getFEMA_Dataset(year):
    dataset = []
    header = []

    match year:
        case 2000:
            with open("C:\\Users\\ferramos\\Desktop\\FEMA Rebuild\\FEMA Datasets\\FEMA Disasters - 2000_2009 (Counties).csv", "r") as csvFile:  # TODO: ~
                csvReader = csv.reader(csvFile)
                for line in csvReader:
                    dataset.append(line)
            # header = dataset.pop(0)
        case 2010:
            with open("C:\\Users\\ferramos\\Desktop\\FEMA Rebuild\\FEMA Datasets\\FEMA Disasters - 2010_2019 (Counties).csv", "r") as csvFile:  # TODO: ~
                csvReader = csv.reader(csvFile)
                for line in csvReader:
                    dataset.append(line)
            # header = dataset.pop(0)
        case 2020:
            with open("C:\\Users\\ferramos\\Desktop\\FEMA Rebuild\\FEMA Datasets\\FEMA Disasters - 2020_2022 (Counties).csv", "r") as csvFile:  # TODO: ~
                csvReader = csv.reader(csvFile)
                for line in csvReader:
                    dataset.append(line)
            # header = dataset.pop(0)
    return dataset


def pullDisasters(disaster, dataset):
    # print(">> " + disaster)
    disasterData = []

    for datapoint in dataset:
        incidentType = datapoint[2]
        if incidentType == disaster or (disaster.find("Levee") != -1 and incidentType == "Dam/Levee Break"):
            disasterData.append(datapoint)
            # print(datapoint)

    return disasterData


def writeDatabase(dataset):
    print(tabulate(dataset))


datasets = [getFEMA_Dataset(2000), getFEMA_Dataset(2010), getFEMA_Dataset(2020)]
# Iterates 3 yearSets
yearType = 1
for yearSet in datasets:
    fullData = []  # Holds compilation of biological, chemical, hurricane, etc. for 1 entire yearSet

    # 1 YearSet = 19 FEMA disaster arrays
    femaDisasters = getFolderNames(clean=True)
    for disaster in femaDisasters:
        data = pullDisasters(disaster, yearSet)
        fullData.append(data)

    # Write to file struct
    print("- - - - - -")
    sortToFolder(yearType, fullData)
    print("- - - - - -")

    yearType += 1
