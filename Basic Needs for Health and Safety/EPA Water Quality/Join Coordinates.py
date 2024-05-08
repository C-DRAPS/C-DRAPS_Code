# TODO: This program joins our existing water facility violations datasets w/ their X-Y Coordinates
#  (coordinates located in SDWIS Facilities file). Writes 2 separate files: 
#     1. Water facilities w/ Coordinates.
#     2. Water facilities that have no coordinates (not found).
#  File pulled from: https://www.arcgis.com/home/item.html?id=bcd1f3810da64374b0ba3ad4c6089031&view=list&sortOrder=desc&sortField=defaultFSOrder#overview
import csv
import os


def getCoordinatesFile():
    waterFacilities = []
    with open("SDWIS stuff/SDWIS Facilities/Water_Facilities.csv", "r") as csvFile:
        csvReader = csv.reader(csvFile)
        for line in csvReader:
            waterFacilities.append(line)
        headers = waterFacilities.pop(0)
    return waterFacilities


def getWaterSystemSummaryDataset(filePath):
    dataset = []
    with open(filePath, "r") as csvFile:
        csvReader = csv.reader(csvFile)
        for line in csvReader:
            dataset.append(line)
        headers = dataset.pop(0)
    return dataset


# Gets file names listed in a directory
def folderFiles(folderPath):
    files = []
    for fileName in os.listdir(folderPath):
        files.append(fileName)
    return files


def mergedInfo(dataLine, waterFacilityLine):
    row = dataLine[0:2] + [waterFacilityLine[1], waterFacilityLine[3]] + [dataLine[3], dataLine[2]] + dataLine[4:] + waterFacilityLine[4:12]
    return row


def writeData(dataset, filePath):
    with open(filePath, "w", encoding='utf-8', newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        dataset.insert(0, ["PWSID", "PWS Name", "Approximate Address", "Postal", "Primacy Agency", "EPA Region",
                           "PWS Type", "Population Served Count", "Cities Served", "Counties Served", "# of Facilities",
                           "# of Violations", "# of Site Visits", "Longitude", "Latitude", "DisplayX", "DisplayY",
                           "Xmin", "Xmax", "Ymin", "Ymax"])
        csvWriter.writerows(dataset)


def writeData_NotFound(dataset, filePath):
    with open(filePath, "w", encoding='utf-8', newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        dataset.insert(0, ["PWSID", "Approximate Address"])
        csvWriter.writerows(dataset)


def displayNewFile(fileName):
    print()
    print(f"\t\t#############################################")
    print(f"\t\t{fileName}")
    print(f"\t\t#############################################")


# TODO: This is main.
year = "2010"  # Toggle
folder = f"SDWIS stuff/Original Datasets/{year} Modified Datasets"
waterFacilities = getCoordinatesFile()

for fileName in folderFiles(folderPath=folder):
    mergedData = []
    notFoundData = []
    displayNewFile(fileName)
    dataset = getWaterSystemSummaryDataset(filePath=folder + "/" + fileName)
    for item in dataset:
        pwsid = item[0]
        found = False
        print(f"pwsid {pwsid}")

        for waterFacility in waterFacilities:
            if pwsid == waterFacility[12]:
                data = mergedInfo(item, waterFacility)
                mergedData.append(data)
                print(f"    => {str(data)}")
                found = True
                break

        if not found:
            notFoundData.append([pwsid, "Not Found"])
            print(f"    =>  <NOT FOUND>")

    writeData(mergedData, filePath=f"SDWIS stuff/Coordinates/{year}/" + fileName)
    writeData_NotFound(notFoundData, filePath=f"SDWIS stuff/Coordinates/{year}/" + fileName.replace(".csv", " Not Found.csv"))
