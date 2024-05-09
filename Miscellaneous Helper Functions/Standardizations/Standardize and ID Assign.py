# TODO: This program creates a .csv file w/ Translated Locations (State,OldName,NewName,FID) + Outputs any locations
#  that it could not identify to the console + Standardizes all counties in a file. ALL files go through this 
#  program before being mapped in ArcGIS (except for x,y coordinate data).
import csv
from tabulate import tabulate
import Translator as translator
import os
import FIPS_Translator as fipsTranslator


# Reads FEMA -22years dataset
def readDataset():
    dataset = []

    with open(inputFilePath, "r", encoding='utf-8') as csvFile:
        csvReader = csv.reader(csvFile)
        for line in csvReader:
            dataset.append(line)
    headers = dataset.pop(0)

    return dataset


# Gets headers of original dataset
def getOriginalHeaders():
    with open(inputFilePath, "r") as csvFile:
        csvReader = csv.reader(csvFile)
        for line in csvReader:
            return line


# Reads ArcGIS "US Counties" Shapefile Table
shpfilesDataset = []  # Global to avoid re-reading dataset on every iteration.
def readArcGIS_USCounties():
    if len(shpfilesDataset) == 0:  # Dump data if empty, before returning dataset
        headers = []
        with open("Basemaps/USA_Counties.csv", "r", encoding='utf-8') as csvFile:
            csvReader = csv.reader(csvFile)
            for line in csvReader:
                shpfilesDataset.append(line)
        headers = shpfilesDataset.pop(0)

    return shpfilesDataset


# Reads ArcGIS "Native Lands" Shapefile Table
nativeLandsDatabase = []  # Global to avoid re-reading dataset on every iteration.
def readArcGIS_NativeLands():
    if len(nativeLandsDatabase) == 0:  # Dump data if empty, before returning dataset
        headers = []
        with open("Basemaps/Native Lands.csv", "r") as csvFile:
            csvReader = csv.reader(csvFile)
            for line in csvReader:
                nativeLandsDatabase.append(line)
        headers = nativeLandsDatabase.pop(0)

    return nativeLandsDatabase


# Converts FEMA state abbr. to real name. Includes territories.
def convertStateAbbr(abbr):
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming',
        'PR': 'Puerto Rico',
        'VI': 'Virgin Islands',
        'AS': 'American Samoa',
        'MP': 'Northern Mariana Islands',
        'GU': 'Guam',
        'FM': 'Federated States of Micronesia'
    }

    return states.get(abbr, "-1")


# Cleans the county string pulled from our FEMA database
def cleanCountyName(location):
    location = location.lower().capitalize()

    location = location.removesuffix(" County")
    location = location.removesuffix(" Parish")
    location = location.removesuffix(" City and Borough")
    location = location.removesuffix(" Borough")
    location = location.removesuffix(" Census Area")
    location = location.removesuffix(" Municipio")
    location = location.removesuffix(" Municipality")

    location = location.removesuffix(" county")
    location = location.removesuffix(" parish")
    location = location.removesuffix(" city and borough")
    location = location.removesuffix(" borough")
    location = location.removesuffix(" census area")
    location = location.removesuffix(" municipio")
    location = location.removesuffix(" municipality")

    return location


def cleanReservationName(location):
    location = location.removesuffix(" Colony (Reservation)")
    location = location.removesuffix(" Indian Reservation")
    location = location.removesuffix(" Community (Indian Reservation)")
    location = location.removesuffix(" Pueblo (Indian Reservation)")
    return location


def hasMatch_USCounties(state, county):
    for row in readArcGIS_USCounties():  # Read in .shp file stuff
        countyArcGIS = row[1]
        stateArcGIS = row[2]

        if state == stateArcGIS and county == countyArcGIS:
            return True
    return False


def hasMatch_NativeLands(state, county):
    for row in readArcGIS_NativeLands():  # Read in .shp file stuff
        countyArcGIS = row[11]
        stateArcGIS = convertStateAbbr(row[13])  # NM -> New Mexico

        if state == stateArcGIS and county == countyArcGIS:
            return True
    return False


def getFID_USCounties(state, county):
    for row in readArcGIS_USCounties():  # Read in .shp file stuff
        countyArcGIS = row[1]
        stateArcGIS = row[2]

        if state == stateArcGIS and county == countyArcGIS:
            return row[0]  # Returns ID


def getFID_NativeLands(state, reservation):
    for row in readArcGIS_NativeLands():  # Read in .shp file stuff
        reservationArcGIS = row[11]
        stateArcGIS = convertStateAbbr(row[13])

        if state == stateArcGIS and reservation == reservationArcGIS:
            return row[0]  # Returns ID


# Prints to Console locations that did have a match, but don't have an FID.
def printIgnoredLocations(ignoredLocations):
    # print("~ LOCATIONS IGNORED ~")
    # for item in ignoredLocations:
    #     print("<IGNORED> " + item)
    return None


# Prints to Console locations that did not match. Locations are unique.
def printMissingLocations(missingLocations):
    # print("\n~ LOCATIONS MISSING ~")
    # for item in missingLocations:
    #     print("<MISSING> " + item)
    return None


# Writes to TranslatedLocations.csv file in format "State,OldName,NewName,FID". For our bookkeeping.
# This function not really used too often...
def writeBookKeepingDoc():
    data = []

    for line in readDataset():
        # state = convertStateAbbr(line[stateIndex])  # NM -> New Mexico
        state = line[stateIndex].strip()
        county = cleanCountyName(line[countyIndex].strip())  # Removes the "fluff"

        if hasMatch_USCounties(state, county):
            data.append([state, county, county, getFID_USCounties(state, county)])
        else:
            state, countyTranslated = translator.Translate(state + "," + county).split(",")
            data.append([state, countyTranslated, county, getFID_USCounties(state, countyTranslated)])

    with open(outputBookKeepingPath, "w", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(["State", "Old_County_Name", "New_County_Name", "FID"])
        csvWriter.writerows(data)


# THIS is our function that standardizes counties in a file :)
def standardizeDoc(isCounty, convertMyState, joinPoint):
    print("   >> Standardizing")
    data = []

    if isCounty:  # County Logic
        for line in readDataset():
            state = convertStateAbbr(line[stateIndex].strip()) if convertMyState else line[stateIndex].strip()  # NM -> New Mexico
            county = cleanCountyName(line[countyIndex].strip())  # Removes the "fluff"

            if hasMatch_USCounties(state, county):
                data.append([state, county] + line[joinPoint:] + [getFID_USCounties(state, county)])
            else:
                try:
                    state, countyTranslated = translator.Translate(state + "," + county).split(",")
                    data.append([state, countyTranslated] + line[joinPoint:] + [getFID_USCounties(state, countyTranslated)])
                except ValueError:
                    print("  >> Skipping: " + state + ", " + county)
    else:  # Reservation Logic
        for line in readDataset():
            state = convertStateAbbr(line[stateIndex]) if convertMyState else line[stateIndex]  # NM -> New Mexico
            reservation = cleanReservationName(line[countyIndex].strip())  # Removes the "fluff"

            if hasMatch_NativeLands(state, reservation):
                data.append([state, "NOT SPECIFIED", reservation] + line[joinPoint:] + [getFID_NativeLands(state, reservation)])
            else:
                try:
                    state, resTranslated = translator.Translate(state + "," + reservation).split(",")
                    data.append([state, "NOT SPECIFIED", resTranslated] + line[joinPoint:] + [getFID_NativeLands(state, resTranslated)])
                except ValueError:
                    print("  >> Skipping: " + state + ", " + reservation)

    data.insert(0, getOriginalHeaders() + ["FID"])
    # print(tabulate(data))

    with open(outputFilePath, "w", encoding='utf-8', newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerows(data)


# Standardizes counties in a file, using FIPS. Used only for special occasions.
def standardizeDoc_FIPS(convertMyState, joinPoint, fipsIndex):
    print("   >> Standardizing")
    data = []

    for line in readDataset():
        state = convertStateAbbr(line[stateIndex].strip()) if convertMyState else line[stateIndex].strip()  # NM -> New Mexico
        fipsCode = str(line[fipsIndex]).replace(".0", "")
        while len(fipsCode) < 5:
            fipsCode = "0" + fipsCode
        county = fipsTranslator.translate(fipsCode)
        county = cleanCountyName(county)  # Translates FIPS -> County -> Cleaned name

        if hasMatch_USCounties(state, county):
            data.append([state, county] + line[joinPoint:] + [getFID_USCounties(state, county)])
        else:
            try:
                state, countyTranslated = translator.Translate(state + "," + county).split(",")
                data.append([state, countyTranslated] + line[joinPoint:] + [getFID_USCounties(state, countyTranslated)])

            except ValueError:
                print("     >> Skipping: " + state + ", " + county + ", FIPS-" + fipsCode)
    data.insert(0, getOriginalHeaders() + ["FID"])
    # print(tabulate(data))

    with open(outputFilePath, "w", encoding='utf-8', newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerows(data)

    return None


# Just iterates through dataset & highlights differences. Run this before standardizing.
def highlightDiff(isCounty, convertMyState):
    for line in readDataset():
        if isCounty:  # Opposite of isCounty is a reservation...
            # state = convertStateAbbr(line[stateIndex])  # NM -> New Mexico
            state = convertStateAbbr(line[stateIndex].strip()) if convertMyState else line[stateIndex]  # NM -> New Mexico
            county = cleanCountyName(line[countyIndex].strip())  # Removes the "fluff"
            # reservation = cleanReservationName(county)  # Removes the "fluff" (if not a county, but is a reservation)

            if not hasMatch_USCounties(state, county) and translator.Translate(state + "," + county) == "N/A":
                print("    <NO MATCH> " + state + ", " + county + " -->  " + translator.Translate(state + "," + county))

        else:
            # state = convertStateAbbr(line[stateIndex])  # NM -> New Mexico
            state = convertStateAbbr(line[stateIndex]) if convertMyState else line[stateIndex]  # NM -> New Mexico
            reservation = cleanReservationName(line[countyIndex].strip())  # Removes the "fluff" (if not a county, but is a reservation)

            if not hasMatch_NativeLands(state, reservation) and translator.Translate(state + "," + reservation) == "N/A":
                print("    <NO MATCH> " + state + ", " + reservation + " -->  " + translator.Translate(state + "," + reservation))


# Creates dictionary items for our Translator.py. Useful when needing to update Translator.py. Use after
#  running highlightDiff().
def createTranslatorItems(isCounty, convertMyState):
    for line in readDataset():
        if isCounty:
            # state = convertStateAbbr(line[1])  # NM -> New Mexico
            state = line[stateIndex].strip()
            county = cleanCountyName(line[countyIndex].strip())  # Removes the "fluff"
            # reservation = cleanReservationName(county)  # Removes the "fluff" (if not a county, but is a reservation)

            if not hasMatch_USCounties(state, county) and translator.Translate(state + "," + county) == "N/A":
                print('        "' + state + ',' + county + '": ' + '"",')  # just remove last "," when copy/pasting :)

        else:
            # state = convertStateAbbr(line[1])  # NM -> New Mexico
            state = convertStateAbbr(line[stateIndex]) if convertMyState else line[stateIndex]  # NM -> New Mexico
            reservation = cleanReservationName(line[countyIndex].strip())  # Removes the "fluff" (if not a county, but is a reservation)

            if not hasMatch_NativeLands(state, reservation) and translator.Translate(state + "," + reservation) == "N/A":
                print('        "' + state + ',' + reservation + '": ' + '"",')  # just remove last "," when copy/pasting :)


# TODO: This is main.
stateIndex = 0   # Advanced Settings: location of "state" in input .csv file
countyIndex = 1  # Advanced Settings: location of "county" in input .csv file
isCounty = True
convertMyState = True  # NM -> New Mexico
inputFilePath = "Input/Files/Adult diabetes rate 2008.csv"
outputFilePath = "Output/Files/Adult diabetes rate 2008.csv"
outputBookKeepingPath = "Output/TranslatedLocations.csv"

# This is for single files
# highlightDiff(isCounty=isCounty, convertMyState=convertMyState)
# createTranslatorItems()
# writeBookKeepingDoc()
# standardizeDoc(isCounty=isCounty, convertMyState=convertMyState, joinPoint=2)
# standardizeDoc_FIPS(convertMyState=convertMyState, joinPoint=2, fipsIndex=4)
# printIgnoredLocations(ignoredLocations)
# printMissingLocations(missingLocations)

# This is for multiple files
for file in os.listdir("Input/Files"):
    inputFilePath = "Input/Files/" + file
    outputFilePath = "Output/Files/" + file
    print(f"[X] {file}")

    # highlightDiff(isCounty=isCounty, convertMyState=convertMyState)
    # createTranslatorItems(isCounty=isCounty, convertMyState=convertMyState)
    # standardizeDoc(isCounty=isCounty, convertMyState=convertMyState, joinPoint=2)
    standardizeDoc_FIPS(convertMyState=convertMyState, joinPoint=2, fipsIndex=4)
