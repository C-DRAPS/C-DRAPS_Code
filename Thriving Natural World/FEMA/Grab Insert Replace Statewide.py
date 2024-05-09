# TODO: This program fixes the issue w/ "statewide". When we originally made our Freq counter, it only +1 when
#  a county was affected OR it read "statewide". However, when it reads "statewide", it never inserted prev.
#  *non-affected* counties. This program fixes that issue by reading in all
#  counties (from Biological Disasters County Data (freq) 2015_2022), figuring out what counties are already
#  counted (target file), and creating a new CSV file w/ original data + new unaccounted counties +1 freq.
#  ...
#  We use "Biological Disasters County Data (freq) 2015_2022" bc names are already standardized to output a
#  new ready-to-map file.
#  ...
#  This program does NOT check if "statewide" is mentioned! Once YOU figure it out, Enter the state + target
#  file -> and it'll see if all counties were listed in the target file!

import csv
from tabulate import tabulate


# Gets ALL counties within a state. Isolate = True, when you just want the county name. Else returns entire line.
def getAllCounties_InState(stateAbbr, isolate):
    allCounties = []
    with open("Biological Disasters County Data (freq) 2015_2022.csv", "r") as csvFile:
        csvReader = csv.reader(csvFile)
        for line in csvReader:
            state = line[1]
            if state == stateAbbr:
                if isolate:
                    allCounties.append(line[3])  # Append county name
                else:
                    allCounties.append(line)  # Append entire line
    return allCounties


# This is our "statewide" file that requires appending counties
def getTargetedFile(fileName):
    dataset = []
    with open("Target Files/" + fileName, "r") as csvFile:
        csvReader = csv.reader(csvFile)
        for line in csvReader:
            dataset.append(line)
    return dataset


# Writes data to an output file
def writeDataset(originalFile, missingData):
    originalDataset = getTargetedFile(fileName=originalFile)

    updatedDataset = originalDataset + missingData

    with open("statewide_output.csv", "w", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerows(updatedDataset)


# Gets FID of a location
def getFID(state, missingCounty):
    for location in getAllCounties_InState(stateAbbr=state, isolate=False):
        if location[3] == missingCounty:
            return location[5]  # Return FID


# Abstracts our functions to get YEAR and INCIDENT_TYPE
def getDefaultData(fileName, dataIndex):
    with open("Target Files/" + fileName, "r") as csvFile:
        csvReader = csv.reader(csvFile)
        csvFile.readline()  # Pops header
        for line in csvReader:
            return line[dataIndex]  # Returns our singular piece of data


# Finds all missing counties within a state
def replaceMissingStatewide(fileName, statewide):
    missingCounties = getAllCounties_InState(statewide, isolate=True)  # Start w/ ALL counties, remove as we find them.

    for disaster in getTargetedFile(fileName=fileName):
        state = disaster[1]
        county = disaster[3]

        if state == statewide:
            missingCounties.remove(county)  # Remove since appeared in dataset = already counted

    # All missing counties found. Time to format missing data into existing data
    missingData = []
    year = getDefaultData(fileName, dataIndex=0)
    incidentType = getDefaultData(fileName, dataIndex=2)
    for county in missingCounties:
        missingData.append([year, statewide, incidentType, county, "1", getFID(state=statewide, missingCounty=county)])

    # Write missing data to original dataset
    print("~ MISSING DATA ~")
    if len(missingData) == 0:
        print("\t<NO MISSING DATA>")
    else:
        print(tabulate(missingData))
        writeDataset(originalFile=fileName, missingData=missingData)  # TODO: Write.
        print("\n[X] Finished: Compiling original + missing data to new file")

    return None


# This function increases freq counters for a specific statewide state. Used for the specific
#  case that we DID +1 statewide disaster prev. BUT there are multiple statewide declarations
#  within a small-time period (original program did not check if multiple statewides could
#  be declared for the same disaster, same time period, and same state...whoops!)
def increaseStatewideFreq(targetFile, statewide):
    print("[X] Wrote to new file, Freq +1 to Existing Statewide ~ " + statewide)
    updatedDataset = []
    for location in getTargetedFile(fileName=targetFile):
        if location[1] == statewide:
            line = location.copy()
            line[4] = str(int(line[4]) + 1)
            updatedDataset.append(line)
        else:
            updatedDataset.append(location)

    with open("statewide_output.csv", "w", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerows(updatedDataset)
    return None


# TODO: This is main.
targetFile = "Fire Disasters County Data (freq) 2015_2022.csv"
statewide_area = "WA"

replaceMissingStatewide(fileName=targetFile, statewide=statewide_area)

# increaseStatewideFreq(targetFile=targetFile, statewide=statewide_area)  # This is for very specific cases
