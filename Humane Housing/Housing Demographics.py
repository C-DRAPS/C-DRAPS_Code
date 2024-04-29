# TODO: This program iterates through a "Housing Demographics"
#  "Housing 20##.csv" file. Very large files, Excel can't open them.
#  Data Pulled (as percentages!):
#    1.Households with one or more people under 18 years
#    2.Households with one or more people 60 years and over
#    3. 1-unit structures
#    4. 2-unit structures
#    5. Mobile homes and all other types of units

import csv
from tabulate import tabulate


# Returns Tuple "County,State"
def getCountyState(string):
    string = string.split("!!")[0]
    return string.split(", ")


def pullData(columnHeader):
    with open(
            "Datasets/Housing Demographics/Original/ACS S1101 HOUSEHOLDS AND FAMILIES 2020.csv", "r") as csvFile:
        csvReader = csv.DictReader(csvFile)

        dataRetrieved = []

        lineNum = 2  # Pairs program w/ Excel line number
        for row in csvReader:
            if lineNum == 15:    # Gets 15th Row (Households with one or more people under 18 years)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 16:  # (Households with one or more people 60 years and over)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 20:  # (1-unit structures)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 21:  # (2-unit structures)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 22:  # (Mobile homes and all other types of units)
                dataRetrieved.append(row[columnHeader])
            lineNum += 1

        return dataRetrieved


# Returns any column that has "...!!Total!!Estimate" in name
def getEligibleColumns(headers):
    columns = []
    for column in headers:
        if column.find("!!Total!!Estimate") != -1:
            columns.append(column)
    return columns


# Written as two separate files bc of pointer issues when reading
headers = []
with open("Datasets/Housing Demographics/Original/ACS S1101 HOUSEHOLDS AND FAMILIES 2020.csv", "r") as csvFile:  # Gets all headers as a dictionary
    csvReader = csv.DictReader(csvFile)
    headers = list(csvReader.fieldnames)

dataset = []
for column in getEligibleColumns(headers):  # Gets Data for each header.
    row = []
    dataPIs = pullData(column)
    row = getCountyState(column) + dataPIs  # Creates array [County, State, %, %, %...]

    print(row)
    dataset.append(row)


# Writes to file
with open("Datasets/Housing Demographics/Modified/Household Demographics 2020.csv", "w", newline='') as csvFile:
    csvWriter = csv.writer(csvFile)
    dataset.insert(0, ["County", "State",
                       "Households with one or more people under 18 years",
                       "Households with one or more people 60 years and over",
                       "1-unit structures", "2-unit structures",
                       "Mobile homes and all other types of units"])
    csvWriter.writerows(dataset)
