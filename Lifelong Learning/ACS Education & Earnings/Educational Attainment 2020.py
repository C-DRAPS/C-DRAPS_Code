# TODO: This program iterates through a "Lifelong Learning"
#  "Education & Earnings 20##.csv" file. Very large files, Excel can't open them.
#  Data Pulled (as whole numbers!):
#    1. Population 18 to 24 years
#    2. Less than high school grad (Population 18 to 24 years)
#    3. High school grad (Population 18 to 24 years)
#    4. Some college or associate's degree (Population 18 to 24 years)
#    5. Bachelor's degree or higher (Population 18 to 24 years)
#    6. Population 25 years and over
#    7. Less than 9th grade (Population 25 years and over)
#    8. 9th to 12th grade no diploma (Population 25 years and over)
#    9. High school grad (Population 25 years and over)
#    10. Some college no degree (Population 25 years and over)
#    11. Associate's degree (Population 25 years and over)
#    12. Bachelor's degree (Population 25 years and over)
#    13. Graduate or professional degree (Population 25 years and over)
#    14. Percent high school grad or higher (Population 25 years and over)
#    15. Percent bachelor's degree or higher (Population 25 years and over)
#    16. Population 25 to 34 years
#    17. High school grad or higher (Population 25 to 34 years)
#    18. Bachelor's degree or higher (Population 25 to 34 years)
#    19. Population 35 to 44 years
#    20. High school grad or higher (Population 35 to 44 years)
#    21. Bachelor's degree or higher (Population 35 to 44 years)
#    22. Population 45 to 64 years
#    23. High school grad or higher (Population 45 to 64 years)
#    24. Bachelor's degree of higher (Population 45 to 64 years)
#    25. Population 65 years and over
#    26. High school grad or higher (Population 65 years and over)
#    27. Bachelor's degree of higher (Population 65 years and over)
#    28. poverty status for less than high school grad
#    29. poverty status for high school grad
#    30. poverty status for some college or associate's
#    31. poverty status for bachelor's or higher
#    32. median earnings for Population 25 years and over with earnings
#    33. median earnings for Less than High School Grad
#    34. median earnings for High School Grad
#    35. median earnings for Some College or Associate's
#    36. median earnings for Bachelor's
#    37. median earnings for Graduate or Professional Degree

import csv
from tabulate import tabulate


# Returns Tuple "County,State"
def getCountyState(string):
    string = string.split("!!")[0]
    return string.split(", ")


# Given a column-header + row value -> Outputs respective value located in percentage-header
def getPercentage(columnHeader, rowNum):
    percentageCol = columnHeader.split("!!")[0] + "!!Percent!!Estimate"

    with open("Datasets/Lifelong Learning/Original/ACS S1501 EDUCATIONAL ATTAINMENT 2020.csv", "r") as csvFile:
        csvReader = csv.DictReader(csvFile)

        lineNum = 2
        for row in csvReader:
            if lineNum == rowNum:
                return row[percentageCol]
            lineNum += 1

    return "(X)"


def pullData(columnHeader):
    with open("Datasets/Lifelong Learning/Original/ACS S1501 EDUCATIONAL ATTAINMENT 2020.csv", "r") as csvFile:
        csvReader = csv.DictReader(csvFile)

        dataRetrieved = []

        lineNum = 2  # Pairs program w/ Excel line number
        for row in csvReader:
            if lineNum == 3:    # Gets 2nd Row (Population 18 to 24 years)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 4:  # (Less than high school grad (Population 18 to 24 years))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 5:  # (High school grad (Population 18 to 24 years))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 6:  # (Some college or associate's degree (Population 18 to 24 years))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 7:  # (Bachelor's degree or higher (Population 18 to 24 years))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 8:  # (Population 25 years and over)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 9:  # (Less than 9th grade (Population 25 years and over))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 10:  # (9th to 12th grade no diploma (Population 25 years and over))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 11:  # (High school grad (Population 25 years and over))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 12:  # (Some college no degree (Population 25 years and over))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 13:  # (Associate's degree (Population 25 years and over))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 14:  # (Bachelor's degree (Population 25 years and over))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 15:  # (Graduate or professional degree (Population 25 years and over))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 16:  # (high school grad or higher (Population 25 years and over))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 17:  # (bachelor's degree or higher (Population 25 years and over))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 18:  # (Population 25 to 34 years)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 19:  # (High school grad or higher (Population 25 to 34 years))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 20:  # (Bachelor's degree or higher (Population 25 to 34 years))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 21:  # (Population 35 to 44 years)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 22:  # (High school grad or higher (Population 35 to 44 years))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 23:  # (Bachelor's degree or higher (Population 35 to 44 years))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 24:  # (Population 45 to 64 years)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 25:  # (High school grad or higher (Population 45 to 64 years))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 26:  # (Bachelor's degree of higher (Population 45 to 64 years))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 27:  # (Population 65 years and over)
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 28:  # (High school grad or higher (Population 65 years and over))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 29:  # (Bachelor's degree of higher (Population 65 years and over))
                dataRetrieved.append(row[columnHeader])

            # Call "Percentage Column" (Whole Numbers not found in 2020 version, only percents.)
            elif lineNum == 59:  # (poverty status for less than high school grad (age 25+))
                dataRetrieved.append(getPercentage(columnHeader, 59))
            elif lineNum == 60:  # (poverty status for high school grad (age 25+))
                dataRetrieved.append(getPercentage(columnHeader, 60))
            elif lineNum == 61:  # (poverty status for some college or associate's (age 25+))
                dataRetrieved.append(getPercentage(columnHeader, 61))
            elif lineNum == 62:  # (poverty status for bachelor's or higher (age 25+))
                dataRetrieved.append(getPercentage(columnHeader, 62))

            elif lineNum == 64:  # (median earnings for Population 25 years and over with earnings (age 25+))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 65:  # (median earnings for Less than High School Grad (age 25+))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 66:  # (median earnings for High School Grad (age 25+))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 67:  # (median earnings for Some College or Associate's (age 25+))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 68:  # (median earnings for Bachelor's (age 25+))
                dataRetrieved.append(row[columnHeader])
            elif lineNum == 69:  # (median earnings for Graduate or Professional Degree (age 25+))
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
with open("Datasets/Lifelong Learning/Original/ACS S1501 EDUCATIONAL ATTAINMENT 2020.csv", "r") as csvFile:  # Gets all headers as a dictionary
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
with open("Datasets/Lifelong Learning/Modified/Education & Earnings 2020.csv", "w", newline='') as csvFile:
    csvWriter = csv.writer(csvFile)
    dataset.insert(0, ["County", "State",
                       "Population 18 to 24 years",
                       "Less than high school graduate (Population 18 to 24 years)",
                       "High school graduate (Population 18 to 24 years)",
                       "Some college or associate's degree (Population 18 to 24 years)",
                       "Bachelor's degree or higher (Population 18 to 24 years)",
                       "Population 25 years and over",
                       "Less than 9th grade (Population 25 years and over)",
                       "9th to 12th grade (Population 25 years and over)",
                       "High school graduate (Population 25 years and over)",
                       "Some college no degree (Population 25 years and over)",
                       "Associate's degree (Population 25 years and over)",
                       "Bachelor's degree (Population 25 years and over)",
                       "Graduate or professional degree (Population 25 years and over)",
                       "Percent high school graduate or higher (Population 25 years and over)",
                       "Percent bachelor's degree or higher (Population 25 years and over)",
                       "Population 25 to 34 years",
                       "High school graduate or higher (Population 25 to 34 years)",
                       "Bachelor's degree or higher (Population 25 to 34 years)",
                       "Population 35 to 44 years",
                       "High school graduate or higher (Population 35 to 44 years)",
                       "Bachelor's degree or higher (Population 35 to 44 years)",
                       "Population 45 to 64 years",
                       "High school graduate or higher (Population 45 to 64 years)",
                       "Bachelor's degree or higher (Population 45 to 64 years)",
                       "Population 65 and over",
                       "High school graduate or higher (Population 65 and over)",
                       "Bachelor's degree or higher (Population 65 and over)",
                       "Less than high school grad poverty rate (age 25+)", "High school grad poverty rate (age 25+)",
                       "Some college or associate's degree poverty rate (age 25+)",
                       "Bachelor's degree or higher poverty rate (age 25+)",
                       "Population 25 years and over with earnings median earnings",
                       "Less than high school grad median earnings", "High school grad median earnings",
                       "Some college or associate's degree median earnings", "Bachelor's degree median earnings",
                       "Graduate or professional degree median earnings"])
    csvWriter.writerows(dataset)
