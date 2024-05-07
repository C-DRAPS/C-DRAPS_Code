# TODO: This creates 2000s Census Database. Algorithm:
#  1. Call API to get needed data
#  2. Sort json data into previously gathered data (ID = County & State)
#  3. Repeat
#  ~
#  The program keeps ALL header items, that way we can see what data
#   was/wasn't pulled. Values themselves are formatted to fit our Census Database

import districtToCounty
import requests
from tabulate import tabulate
import csv


def printDatabase(database):
    print("\n~ DATABASE ~")
    for item in database:
        print(item)


# Cleans line to remove stateNum & countyNum (the last two items)
def cleanRequest(r, cutoff):
    row = []
    for item in r:
        row.append(item[0:len(item)-cutoff])
    return row


# Adds columns together to get 1 final column.
#  (Ex, age under 6 = under1yrs + 1yrs + 2yrs + 3yrs...)
def sumData(r):
    headers = r.pop(0)  # Pop Headers

    dataset = []
    for county in r:
        row = []
        row.append(county[0])
        values = list(map(int, county[1:]))  # Converts ["1","2"] -> [1,2]
        row.append(str(sum(values)))  # Sums [1,2] -> 3 -> "3"
        dataset.append(row)

    dataset.insert(0, headers)
    return dataset


# Inserts new data into our database
def joinData(database, newData):
    modifiedDatabase = []
    for county in database:
        location = county[0]

        for item in newData:
            if item[0] == location:
                modifiedDatabase.append(county + item[1:])  # Append existing + new
    return modifiedDatabase


# Merges datasets w/ Diff. Names & Same Table (congressional districts)
def mergeCongressionalDistricts(dataset, r):
    # Add everything in r -> dataset
    headers = r.pop(0)
    if dataset != []:
        dataset.pop(0)

    for item in r:
        city = item[0].split(", ")[0]
        city = city.replace(" (part)", "")
        state = item[0].split(", ")[2]
        dataset.append([city + ", " + state, item[1]])

    # Check if duplicates
    merged = []
    for item in dataset:
        exists = False
        for loc in merged:
            if item[0] == loc[0]:
                loc[1] = int(loc[1]) + int(item[1])
                exists = True
                break

        if not exists:
            merged.append(item)

    merged.insert(0, headers)
    return merged



API_Key = "YOUR_API_KEY_HERE"

database = []


# Get Males & Females
variables = "P012002,P012026"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
database = cleanRequest(r, 2)  # Initialize Database
print("[X] Males & Females")



# Get Age Under 6 yrs
variables = "PCT012003,PCT012004,PCT012005,PCT012006,PCT012007,PCT012008," + "PCT012107,PCT012108,PCT012109,PCT012110,PCT012111,PCT012112"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
age = cleanRequest(r, 2)
database = joinData(database, sumData(age))
print("[X] Age Under 6 yrs")



# Get Age 6-18 yrs -> Male + Female -> Combine
variables = "PCT012009,PCT012010,PCT012011,PCT012012,PCT012013," \
            "PCT012014,PCT012015,PCT012016,PCT012017,PCT012018," \
            "PCT012019,PCT012020,PCT012021"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
maleTotals = cleanRequest(r, 2)

variables = "PCT012113,PCT012114,PCT012115,PCT012116,PCT012117," \
            "PCT012118,PCT012119,PCT012120,PCT012121,PCT012122," \
            "PCT012123,PCT012124,PCT012125"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
femaleTotals = cleanRequest(r, 2)
age = joinData(maleTotals, femaleTotals)  # Combine males & females
database = joinData(database, sumData(age))  # Insert to database
print(tabulate(database))
breakpoint()
print("[X] Age 6-18 yrs")



# Get Age 19-25 yrs -> Male + Female -> Combine
variables = "PCT012022,PCT012023,PCT012024,PCT012025,PCT012026," \
            "PCT012027,PCT012028"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
maleTotals = cleanRequest(r, 2)

variables = "PCT012126,PCT012127,PCT012128,PCT012129,PCT012130," \
            "PCT012131,PCT012132"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
femaleTotals = cleanRequest(r, 2)
age = joinData(maleTotals, femaleTotals)  # Combine males & females
database = joinData(database, sumData(age))  # Insert to database
print("[X] Age 19-25 yrs")



# Get Age 26-34 yrs -> Male + Female -> Combine
variables = "PCT012029,PCT012030,PCT012031,PCT012032,PCT012033," \
            "PCT012034,PCT012035,PCT012036,PCT012037"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
maleTotals = cleanRequest(r, 2)

variables = "PCT012133,PCT012134,PCT012135,PCT012136,PCT012137," \
            "PCT012138,PCT012139,PCT012140,PCT012141"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
femaleTotals = cleanRequest(r, 2)
age = joinData(maleTotals, femaleTotals)  # Combine males & females
database = joinData(database, sumData(age))  # Insert to database
print("[X] Age 26-34 yrs")



# Get Age 35-44 yrs -> Male + Female -> Combine
variables = "PCT012038,PCT012039,PCT012040,PCT012041,PCT012042," \
            "PCT012043,PCT012044,PCT012045,PCT012046,PCT012047"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
maleTotals = cleanRequest(r, 2)

variables = "PCT012142,PCT012143,PCT012144,PCT012145,PCT012146," \
            "PCT012147,PCT012148,PCT012149,PCT012150,PCT012151"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
femaleTotals = cleanRequest(r, 2)
age = joinData(maleTotals, femaleTotals)  # Combine males & females
database = joinData(database, sumData(age))  # Insert to database
print("[X] Age 35-44 yrs")



# Get Age 45-54 yrs -> Male + Female -> Combine
variables = "PCT012048,PCT012049,PCT012050,PCT012051,PCT012052," \
            "PCT012053,PCT012054,PCT012055,PCT012056,PCT012057"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
maleTotals = cleanRequest(r, 2)

variables = "PCT012152,PCT012153,PCT012154,PCT012155,PCT012156," \
            "PCT012157,PCT012158,PCT012159,PCT012160,PCT012161"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
femaleTotals = cleanRequest(r, 2)
age = joinData(maleTotals, femaleTotals)  # Combine males & females
database = joinData(database, sumData(age))  # Insert to database
print("[X] Age 45-55 yrs")



# Get Age 55-64 yrs -> Male + Female -> Combine
variables = "PCT012058,PCT012059,PCT012060,PCT012061,PCT012062," \
            "PCT012063,PCT012064,PCT012065,PCT012066,PCT012067"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
maleTotals = cleanRequest(r, 2)

variables = "PCT012162,PCT012163,PCT012164,PCT012165,PCT012166," \
            "PCT012167,PCT012168,PCT012169,PCT012170,PCT012171"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
femaleTotals = cleanRequest(r, 2)
age = joinData(maleTotals, femaleTotals)  # Combine males & females
database = joinData(database, sumData(age))  # Insert to database
print("[X] Age 55-64 yrs")



# Get Age 65-74 yrs -> Male + Female -> Combine
variables = "PCT012068,PCT012069,PCT012070,PCT012071,PCT012072," \
            "PCT012073,PCT012074,PCT012075,PCT012076,PCT012077"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
maleTotals = cleanRequest(r, 2)

variables = "PCT012172,PCT012173,PCT012174,PCT012175,PCT012176," \
            "PCT012177,PCT012178,PCT012179,PCT012180,PCT012181"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
femaleTotals = cleanRequest(r, 2)

age = joinData(maleTotals, femaleTotals)  # Combine males & females
database = joinData(database, sumData(age))  # Insert to database
print("[X] Age 65-74 yrs")



# Get Age 75+ yrs -> Male + Female -> Combine
variables = "PCT012078,PCT012079,PCT012080,PCT012081,PCT012082," \
            "PCT012083,PCT012084,PCT012085,PCT012086,PCT012087," \
            "PCT012088,PCT012089,PCT012090,PCT012091,PCT012092"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
maleTotals_pt1 = cleanRequest(r, 2)
variables = "PCT012093,PCT012094,PCT012095,PCT012096,PCT012097," \
            "PCT012098,PCT012099,PCT012100,PCT012101,PCT012102," \
            "PCT012103,PCT012104,PCT012105"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
maleTotals_pt2 = cleanRequest(r, 2)
maleTotals = joinData(maleTotals_pt1,maleTotals_pt2)

variables = "PCT012182,PCT012183,PCT012184,PCT012185,PCT012186," \
            "PCT012187,PCT012188,PCT012189,PCT012190,PCT012191," \
            "PCT012192,PCT012193,PCT012194,PCT012195,PCT012196"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
femaleTotals_pt1 = cleanRequest(r, 2)
variables = "PCT012197,PCT012198,PCT012199,PCT012200,PCT012201," \
            "PCT012202,PCT012203,PCT012204,PCT012205,PCT012206," \
            "PCT012207,PCT012208,PCT012209"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
femaleTotals_pt2 = cleanRequest(r, 2)
femaleTotals = joinData(femaleTotals_pt1, femaleTotals_pt2)

age = joinData(maleTotals, femaleTotals)  # Combine males & females
database = joinData(database, sumData(age))  # Insert to database
print("[X] Age 75+ yrs")



# White Alone
variables = "P003003"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
race = cleanRequest(r, 2)
database = joinData(database, race)

# Black Alone
variables = "P003004"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
race = cleanRequest(r, 2)
database = joinData(database, race)

# Native American Alone
variables = "P003005"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
race = cleanRequest(r, 2)
database = joinData(database, race)

# Asian Alone
variables = "P003006"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
race = cleanRequest(r, 2)
database = joinData(database, race)


# Hawaiian Alone
variables = "P003007"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
race = cleanRequest(r, 2)
database = joinData(database, race)

# Other Race Alone
variables = "P003008"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
race = cleanRequest(r, 2)
database = joinData(database, race)

# Two or More Races Alone
variables = "P003009"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
race = cleanRequest(r, 2)
database = joinData(database, race)

# Hispanic Alone
variables = "P004002"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
race = cleanRequest(r, 2)
database = joinData(database, race)

# White (Not Hispanic) Alone
variables = "P008003"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
race = cleanRequest(r, 2)
database = joinData(database, race)


#
# API Call Change
#


# Households
print("[ ] Households")
variables = "P055001"
districts = districtToCounty.getCongressionalDistricts()
print(districts)
income = []
for stateNum in districts:
    for district in districts.get(stateNum):
        r = requests.get("https://api.census.gov/data/2000/dec/cd110s?get=NAME," + variables + "&for=county%20(or%20part):*&in=state:" + stateNum + "%20congressional%20district:" + district + "&key=" + API_Key).json()
        r = cleanRequest(r, 3)
        income = mergeCongressionalDistricts(income, r)
        # print(tabulate(households))
    print("   [X] " + variables + " -> stateNum " + stateNum + " | districts " + str(districts.get(stateNum)))
database = joinData(database, income)


# Income: Under $25,000
print("[ ] Under $25,000")
variables = "P052002,P052003,P052004,P052005"
districts = districtToCounty.getCongressionalDistricts()
print(districts)
income = []
for stateNum in districts:
    for district in districts.get(stateNum):
        r = requests.get("https://api.census.gov/data/2000/dec/cd110s?get=NAME," + variables + "&for=county%20(or%20part):*&in=state:" + stateNum + "%20congressional%20district:" + district + "&key=" + API_Key).json()
        r = cleanRequest(r, 3)
        income = mergeCongressionalDistricts(income, sumData(r))
        # print(tabulate(households))
    print("   [X] " + variables + " -> stateNum " + stateNum + " | districts " + str(districts.get(stateNum)))
database = joinData(database, income)


# Income: $25,000 - $49,999
print("[ ] $25,000 - $49,999")
variables = "P052006,P052007,P052008,P052009,P052010"
districts = districtToCounty.getCongressionalDistricts()
print(districts)
income = []
for stateNum in districts:
    for district in districts.get(stateNum):
        r = requests.get("https://api.census.gov/data/2000/dec/cd110s?get=NAME," + variables + "&for=county%20(or%20part):*&in=state:" + stateNum + "%20congressional%20district:" + district + "&key=" + API_Key).json()
        r = cleanRequest(r, 3)
        income = mergeCongressionalDistricts(income, sumData(r))
        # print(tabulate(households))
    print("   [X] " + variables + " -> stateNum " + stateNum + " | districts " + str(districts.get(stateNum)))
database = joinData(database, income)


# Income: $50,000 - $74,999
print("[ ] $50,000 - $74,999")
variables = "P052011,P052012"
districts = districtToCounty.getCongressionalDistricts()
print(districts)
income = []
for stateNum in districts:
    for district in districts.get(stateNum):
        r = requests.get("https://api.census.gov/data/2000/dec/cd110s?get=NAME," + variables + "&for=county%20(or%20part):*&in=state:" + stateNum + "%20congressional%20district:" + district + "&key=" + API_Key).json()
        r = cleanRequest(r, 3)
        income = mergeCongressionalDistricts(income, sumData(r))
        # print(tabulate(households))
    print("   [X] " + variables + " -> stateNum " + stateNum + " | districts " + str(districts.get(stateNum)))
database = joinData(database, income)


# Income: $75,000 - $99,999
print("[ ] $75,000 - $99,999")
variables = "P052013"
districts = districtToCounty.getCongressionalDistricts()
print(districts)
income = []
for stateNum in districts:
    for district in districts.get(stateNum):
        r = requests.get("https://api.census.gov/data/2000/dec/cd110s?get=NAME," + variables + "&for=county%20(or%20part):*&in=state:" + stateNum + "%20congressional%20district:" + district + "&key=" + API_Key).json()
        r = cleanRequest(r, 3)
        income = mergeCongressionalDistricts(income, r)
        # print(tabulate(households))
    print("   [X] " + variables + " -> stateNum " + stateNum + " | districts " + str(districts.get(stateNum)))
database = joinData(database, income)


# Income: Over $100,000
print("[ ] Over $100,000")
variables = "P052014,P052015,P052016,P052017"
districts = districtToCounty.getCongressionalDistricts()
print(districts)
income = []
for stateNum in districts:
    for district in districts.get(stateNum):
        r = requests.get("https://api.census.gov/data/2000/dec/cd110s?get=NAME," + variables + "&for=county%20(or%20part):*&in=state:" + stateNum + "%20congressional%20district:" + district + "&key=" + API_Key).json()
        r = cleanRequest(r, 3)
        income = mergeCongressionalDistricts(income, sumData(r))
        # print(tabulate(households))
    print("   [X] " + variables + " -> stateNum " + stateNum + " | districts " + str(districts.get(stateNum)))
database = joinData(database, income)


#
# API Call Change (back to original)
#


# Use Employment Figures from original .csv File / "Pop 16 & Over"
#  Algorithm: (Males + Females) - childPop + Get age "16-18yrs" -> Population 16 & Over. Used to calculate 
#  percentages for some figures in a research article.
variables = "PCT012019,PCT012020,PCT012021," + "PCT012123,PCT012124,PCT012125"
r = requests.get("https://api.census.gov/data/2000/dec/sf1?get=NAME," + variables + "&for=county:*&in=state:*&key=" + API_Key).json()
age = cleanRequest(r, 2)
database = joinData(database, sumData(age))
print("[X] Population 16-18")

printDatabase(database)


# Write new data
with open("/Databases/Updated/2000s/2000s Census Database (Updated Labels).csv", "w", newline='') as csvFile:
    csvWriter = csv.writer(csvFile)
    database.insert(0, ["Location", "Males", "Females",
                        "Under 6 years", "6 to 18 years", "19 to 25 years", "26 to 34 years", "35 to 44 years",
                        "45 to 54 years", "55 to 64 years", "65 to 74 years", "75 years and above",
                        "White alone", "Black or African American alone", "American Indian and Alaska Native alone",
                        "Asian alone", "Native Hawaiian and other Pacific Islander alone", "Some other race alone",
                        "Two or more races", "Hispanic or Latino (of any race)", "White alone (not hispanic or Latino)",
                        "Households", "Under $25K", "$25K to $49K", "$50K to $74K", "$75K to $99K", "$100K and over",
                        "Population 16 to 18"])
    csvWriter.writerows(database)
