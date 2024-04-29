# TODO: This program iterates through a "Reliable Transportation"
#  "Transportation 20##.csv" file. Very large files, Excel can't open them.
#  Data Pulled (as percentages!):
#    1. "Use car/truck/van to go to work"
#    2. "Drove alone"
#    3. "Carpooled"
#    4. "Public Transportation"
#    5. "Walked"
#    6. "Bicycle"
#    7. "Taxicab/motorcycle/other means"
#    8. "Worked from home"
#    9. "Worked within county of residence"
#    10. "Worked outside county of residence"
#    11. "Travel time to work less than 10 minutes"
#    12. "Travel time to work 10 to 14 minutes"
#    13. "Travel time to work 15 to 19 minutes"
#    14. "Travel time to work 20 to 24 minutes"
#    15. "Travel time to work 25 to 29 minutes"
#    16. "Travel time to work 30 to 34 minutes"
#    17. "Travel time to work 35 to 44 minutes"
#    18. "Travel time to work 45 to 59 minutes"
#    19. "Travel time to work 60+ minutes"
#    20. "Mean travel time to work (minutes)"
#    21. "0 vehicles available"
#    22. "1 vehicles available"
#    23. "2 vehicles available"
#    24. "3+ vehicles available"

import csv
from tabulate import tabulate


# Returns Tuple "County,State"
def getCountyState(string):
    string = string.split("!!")[0]
    return string.split(", ")


def pullData(columnHeader):
    with open("Datasets/Reliable Transportation/Original/ACS S0801 COMMUTE 2010.csv", "r") as csvFile:
        csvReader = csv.DictReader(csvFile)

        dataRetrieved = []

        lineNum = 2  # Pairs program w/ Excel line number
        for row in csvReader:
            if lineNum == 4:    # Gets 4th Row (Use car/truck/van to go to work)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 5:  # (drove alone)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 6:  # (carpooled)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 11:  # (public transportation)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 12:  # (walked)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 13:  # (bicycle)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 14:  # (taxicab/motorcycle/other means)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 15:  # (worked from home)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 18:  # (worked within county of residence)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 19:  # (worked outside county of residence)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 42:  # (travel time to work less than 10 minutes)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 43:  # (travel time to work 10 to 14 minutes)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 44:  # (travel time to work 15 to 19 minutes)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 45:  # (travel time to work 20 to 24 minutes)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 46:  # (travel time to work 25 to 29 minutes)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 47:  # (travel time to work 30 to 34 minutes)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 48:  # (travel time to work 35 to 44 minutes)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 49:  # (travel time to work 45 to 59 minutes)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 50:  # (travel time to work 60+ minutes)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 51:  # (Mean travel time to work (minutes))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 54:  # (0 vehicles available)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 55:  # (1 vehicles available)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 56:  # (2 vehicles available)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 57:  # (3+ vehicles available)
                dataRetrieved.append(row[columnHeader])
            lineNum += 1

        return dataRetrieved


# Returns any column that has "...!!Total!!Estimate" in name
def getEligibleColumns(headers):
    columns = []
    for column in headers:
        if column.find("!!Total!!Estimate") != -1:  # Only gather the "total" values
            columns.append(column)
    return columns


# Written as two separate files bc of pointer issues when reading
headers = []
with open("Datasets/Reliable Transportation/Original/ACS S0801 COMMUTE 2010.csv", "r") as csvFile:  # Gets all headers
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
with open("Datasets/Reliable Transportation/Modified/Transportation 2010.csv.csv", "w", newline='') as csvFile:
    csvWriter = csv.writer(csvFile)
    dataset.insert(0, ["County", "State",
                       "Use car/truck/van to go to work", "Drove alone", "Carpooled", "Public Transportation",
                       "Walked", "Bicycle", "Taxicab/motorcycle/other means", "Worked from home",
                       "Worked within county of residence", "Worked outside county of residence",
                       "Travel time to work less than 10 minutes", "Travel time to work 10 to 14 minutes",
                       "Travel time to work 15 to 19 minutes", "Travel time to work 20 to 24 minutes",
                       "Travel time to work 25 to 29 minutes", "Travel time to work 30 to 34 minutes",
                       "Travel time to work 35 to 44 minutes", "Travel time to work 45 to 59 minutes",
                       "Travel time to work 60+ minutes", "Mean travel time to work (minutes)",
                       "0 vehicles available", "1 vehicles available", "2 vehicles available", "3+ vehicles available"])
    csvWriter.writerows(dataset)
