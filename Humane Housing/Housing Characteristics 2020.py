# TODO: This program iterates through a "Housing Characteristics"
#  "Housing Chars 20##.csv" file. Very large files, Excel can't open them.
#  Data Pulled:
#    1. Year Built: 2014+
#    2. Year Built: 2010 to 2013
#    3. Year Built: 2000 to 2009
#    4. Year Built: 1980 to 1999
#    5. Year Built: 1960 to 1979
#    6. Year Built: 1940 to 1959
#    7. Year Built: 1939 or earlier
#    8. Vehicles Available: 0
#    9. Vehicles Available: 1
#    10. Vehicles Available: 2
#    11. Vehicles Available: 3+


import csv
from tabulate import tabulate


originalFilePath = "Housing Characteristics/Original/ACS S2504 Physical Housing 2020.csv"
newFilePath = "Housing Characteristics/Modified/Household Characteristics 2020.csv"


# Returns Tuple "County,State"
def getCountyState(string):
    string = string.split("!!")[0]
    return string.split(", ")


def pullData(columnHeader):
    with open(originalFilePath, "r") as csvFile:
        csvReader = csv.DictReader(csvFile)

        dataRetrieved = []

        lineNum = 2  # Pairs program w/ Excel line number
        for row in csvReader:
            if lineNum == 12:    # Gets 12th Row (Year Structure Built: 2014+)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 13:  # (Year Structure Built: 2010 to 2013)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 14:  # (Year Structure Built: 2000 to 2009)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 15:  # (Year Structure Built: 1980 to 1999)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 16:  # (Year Structure Built: 1960 to 1979)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 17:  # (Year Structure Built: 1940 to 1959)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 18:  # (Year Structure Built: 1939 or earlier)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 34:  # (Vehicles Available 0)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 35:  # (Vehicles Available 1)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 36:  # (Vehicles Available 2)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 37:  # (Vehicles Available 3+)
                dataRetrieved.append(row[columnHeader])
            lineNum += 1

        return dataRetrieved


# Returns any column that has "...!!Total!!Estimate" in name
def getEligibleColumns(headers):
    columns = []
    for column in headers:
        if column.find("!!Occupied housing units!!Estimate") != -1:
            columns.append(column)
    return columns


# Written as two separate files bc of pointer issues when reading
headers = []
with open(originalFilePath, "r") as csvFile:  # Gets all headers as a dictionary
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
with open(newFilePath, "w", newline='') as csvFile:
    csvWriter = csv.writer(csvFile)
    dataset.insert(0, ["County", "State",
                       "Year Structure Built: 2014+",
                       "Year Structure Built: 2010 to 2013",
                       "Year Structure Built: 2000 to 2009",
                       "Year Structure Built: 1980 to 1999",
                       "Year Structure Built: 1960 to 1979",
                       "Year Structure Built: 1940 to 1959",
                       "Year Structure Built: 1939 or earlier",
                       "0 Vehicles Available", "1 Vehicles Available",
                       "2 Vehicles Available", "3+ Vehicles Available"])  # TODO: Fill in rest of headers

    csvWriter.writerows(dataset)
