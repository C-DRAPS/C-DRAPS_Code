# TODO: This file pulls Congressional District data from Census -> Stores it as a Dictionary
import csv
import requests
from tabulate import tabulate


# Grabs every Congressional District from each state (key=stateNum, val=CongressionalDistrict)
def getCongressionalDistricts():
    districts = {}
    # Assigning
    with open("congressionalDistricts.txt", "r") as textFile:
        for line in textFile:
            stateNum = line.split(",")[3].replace('"', '')
            cdNum = line.split(",")[4].replace('"', '').replace(']', '')

            districts.setdefault(stateNum, [])
            districts[stateNum].append(cdNum)

    # Print
    # print("\nState -> Congressional District Assigned")
    # for key in districts.keys():
    #     print(key + " --> ", end='')
    #     print(districts.get(key))
    # print()
    return districts
