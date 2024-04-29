# TODO: This program iterates through a "Meaningful Work & Wealth"
#  "Industry 20##.csv" file. Very large files, Excel can't open them.
#  Data Pulled (as whole numbers!):
#    1. Population for whom poverty status is determined
#    2. Poverty status for Under 18 years old
#    3. Poverty status for Under 18-64 years old
#    4. Poverty status for Under 60+ years old (2020 only)
#    5. Poverty status for Under 65+ years old
#    6. poverty levels, white alone
#    7. poverty levels, black alone
#    8. poverty levels, indian alone
#    9. poverty levels, asian alone
#    10. poverty levels, hawaiian alone
#    11. poverty levels, other race alone
#    12. poverty levels, two or more races
#    13. poverty levels, hispanic or latino
#    14. poverty levels, white alone (not hispanic or latino)
#    15. Poverty levels, less than high school grad
#    16. Poverty levels, high school grad
#    17. Poverty levels, some college/associates
#    18. Poverty levels, bachelors or higher
#    19. in poverty, employed
#    20. in poverty, unemployed
#    21. income below 50% poverty level
#    22. income below 125% poverty level
#    23. income below 150% poverty level
#    24. income below 200% poverty level
#    25. income below 300% poverty level (2020 only)
#    26. income below 400% poverty level (2020 only)
#    27. income below 500% poverty level (2020 only)

import csv
from tabulate import tabulate


# Returns Tuple "County,State"
def getCountyState(string):
    string = string.split("!!")[0]
    return string.split(", ")


def pullData(columnHeader):
    with open("Datasets/Meaningful Work & Wealth/Original/ACS S1701 POVERTY STATUS 2012.csv", "r") as csvFile:
        csvReader = csv.DictReader(csvFile)

        dataRetrieved = []

        lineNum = 2  # Pairs program w/ Excel line number
        for row in csvReader:
            if lineNum == 2:    # Gets 2nd Row (Population for whom poverty status is determined)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 4:  # (poverty status for Under 18 years old)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 6:  # (poverty status for Under 18-64 years old)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 7:  # (poverty status for Under 65+ years old)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 13:  # (poverty levels, white alone)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 14:  # (poverty levels, black alone)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 15:  # (poverty levels, indian alone)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 16:  # (poverty levels, asian alone)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 17:  # (poverty levels, hawaiian alone)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 18:  # (poverty levels, other race alone)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 19:  # (poverty levels, two or more races)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 20:  # (poverty levels, hispanic or latino)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 21:  # (poverty levels, white alone (not hispanic or latino))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 24:  # (poverty levels, less than high school grad)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 25:  # (poverty levels, high school grad)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 26:  # (poverty levels, some college/associates)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 27:  # (poverty levels, bachelors or higher)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 30:  # (in poverty, employed)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 33:  # (in poverty, unemployed)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 42:  # (income below 50% poverty level)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 43:  # (income below 125% poverty level)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 44:  # (income below 150% poverty level)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 45:  # (income below 185% poverty level)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 46:  # (income below 200% poverty level)
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
with open("Datasets/Meaningful Work & Wealth/Original/ACS S1701 POVERTY STATUS 2012.csv", "r") as csvFile:  # Gets all headers as a dictionary
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
with open("Datasets/Meaningful Work & Wealth/Modified/Poverty Levels 2012.csv", "w", newline='') as csvFile:
    csvWriter = csv.writer(csvFile)
    dataset.insert(0, ["County", "State",
                       "Population for whom poverty status is determined",
                       "Under 18 years (in poverty)", "18 to 64 years (in poverty)",
                       "65 years and over (in poverty)",
                       "White alone (in poverty)", "Black or African American alone (in poverty)",
                       "American Indian and Alaska Native alone (in poverty)", "Asian alone (in poverty)",
                       "Native Hawaiian and Other Pacific Islander alone (in poverty)",
                       "Some other race alone (in poverty)", "Two or more races (in poverty)",
                       "Hispanic or Latino origin (in poverty)", "White alone (not Hispanic or Latino) (in poverty)",
                       "Less than high school graduate (in poverty)", "High school graduate (in poverty)",
                       "Some college or Associate's degree (in poverty)", "Bachelor's degree or higher (in poverty)",
                       "Employed (in poverty)", "Unemployed (in poverty)",
                       "Income below 50% poverty level", "Income below 125% poverty level",
                       "Income below 150% poverty level", "Income below 185% poverty level",
                       "Income below 200% poverty level"])
    csvWriter.writerows(dataset)
