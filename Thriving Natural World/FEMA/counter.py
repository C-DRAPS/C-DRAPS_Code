# TODO: This program counts the frequency of a location (State, County). It only works on 1 file per run.
#  You can make this program iterative to multiple files by calling this file from another python program and
#  applying it an array of folders/files.

import csv


def setFilePath(path, sy, ey):
    global filePath
    global filePath_New
    global startYear  # Used to check if any locations were affected "Statewide"
    global endYear
    filePath = path  # Set original

    path = path.removesuffix(".csv")
    path = path + " (freq).csv"
    filePath_New = path  # Set new

    startYear = sy
    endYear = ey


def readDataset():
    dataset = []

    with open(filePath, "r") as csvFile:
        csvReader = csv.reader(csvFile)
        for line in csvReader:
            dataset.append(line)
    dataset.pop(0)  # Pop headers

    return dataset


def writeDatabase(data):
    with open(filePath_New, "w", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(["BaseYear", "state", "incidentType", "designatedArea", "Freq", "FID"])
        csvWriter.writerows(data)


# This is where we check if a file has been affected by a disaster statewide. Adds +1 to all locations
#  if state, disasterType, & year match (includes reservations)
def coverStatewide(dataset):
    statewideAreas = [["ND", "2000", "Severe Storm(s)"], ["AZ", "2000", "Severe Storm(s)"],
                      ["IN", "2002", "Severe Storm(s)"], ["PA", "2003", "Severe Storm(s)"],
                      ["OR", "2001", "Fire"], ["CO", "2002", "Fire"], ["NM", "2003", "Fire"],
                      ["TX", "2009", "Fire"], ["OK", "2009", "Fire"], ["TX", "2009", "Fire"],
                      ["OK", "2012", "Fire"], ["NY", "2003", "Other"], ["WI", "2005", "Hurricane"],
                      ["TX", "2005", "Hurricane"], ["MO", "2007", "Severe Ice Storm"],
                      ["PA", "2012", "Hurricane"], ["LA", "2020", "Biological"],
                      ["RI", "2011", "Hurricane"], ["CO", "2016", "Fire"], ["WA", "2021", "Fire"]]

    modifiedDataset = []

    for location in dataset:  # Go through each location in dataset
        state = location[1]
        incidentType = location[2]

        matched = False
        for area in statewideAreas:  # +1 if area is statewide
            if state == area[0] and incidentType == area[2] and startYear <= int(area[1]) <= endYear:
                modifiedDataset.append([startYear, state, incidentType, location[3], str(int(location[4])+1), location[5]])
                print("   --> Statewide Found! " + str([startYear, state, incidentType, location[3], str(int(location[4])+1), location[5]]))
                matched = True

        if not matched:  # regular append if not statewide
            modifiedDataset.append(location)

    return modifiedDataset


# TODO: This is main.
#  Every function in this program gets initialized from here.
def findFreq(filepath, start, end):
    setFilePath(filepath, start, end)
    database = readDataset()
    copyDatabase = readDataset()

    dataset = []
    unique = []
    for line in database:
        line.pop(1)  # Pop "declaration date" identifier

        print("   " + str(line))
        if line not in unique:  # Top iterator: Only checks if item has already been accounted for.
            unique.append(line)  # makes it non-unique now...

            state = line[0]
            incidentType = line[1]
            county = line[2]
            FID = line[3]

            count = 0
            for row in copyDatabase:  # Inside iterator: checks freq
                if state == row[0] and county == row[3]:  # note - this still contains col "declaration date"
                    count += 1
                    print("       +1 <--" + str(row))

            dataset.append([str(start), state, incidentType, county, count, FID])  # Freq has been made, add to dataset

    dataset = coverStatewide(dataset)  # Check if any state in our dataset is statewide before writing to file
    writeDatabase(dataset)
