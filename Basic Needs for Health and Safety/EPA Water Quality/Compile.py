# TODO: This program should be run after Join Coordinates.py, it compiles all individual state-level datasets (w/ coordinates)
#  into a singular 2020 Water Facilities CSV File to plot into ArcGIS
import csv
import os
from tabulate import tabulate


def getDatasets(folderPath):
    filePaths = []
    for fileName in os.listdir(folderPath):
        if fileName.find(".csv") != -1 and fileName.find("Not Found") == -1:  # Remove folders and 'not found' datasets from list
            filePaths.append(folderPath + "/" + fileName)
    return filePaths


def getData(file):
    data = []
    with open(file, "r") as csvFile:
        csvReader = csv.reader(csvFile)
        for line in csvReader:
            data.append(line)
    data.pop(0)  # Remove Headers
    return data


def writeData(dataset, outputPath):
    with open(outputPath, "w", encoding='utf-8', newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        dataset.insert(0, ["PWSID", "PWS Name", "Approximate Address", "Postal", "Primacy Agency", "EPA Region",
                           "PWS Type", "Population Served Count", "Cities Served", "Counties Served", "# of Facilities",
                           "# of Violations", "# of Site Visits", "Longitude", "Latitude", "DisplayX", "DisplayY",
                           "Xmin", "Xmax", "Ymin", "Ymax"])
        csvWriter.writerows(dataset)


# TODO: This is main.
year = "2020"
path = f"SDWIS stuff/Coordinates/{year}"
compiledDataset = []
for filePath in getDatasets(folderPath=path):
    compiledDataset += getData(file=filePath)

writeData(compiledDataset, f"SDWIS stuff/{year} Water Facilities Coordinates/Water Facility Violations {year}.csv")
