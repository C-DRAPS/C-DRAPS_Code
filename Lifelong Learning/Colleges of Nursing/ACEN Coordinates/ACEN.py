# TODO: This file opens a file, extracts useful information from dataset to form an "address". Passes
#  this info to "Coordinates_Module.py" to pull coordinates of a single location.
#  Modified to use Address first then if DNE use College Name + State.
import csv

import Coordinates_Module as Coordinates_Module
from tabulate import tabulate


def getDataset(path):
    dataset = []
    with open(path, "r", encoding='utf-8') as csvFile:
        csvReader = csv.reader(csvFile)
        for line in csvReader:
            dataset.append(line)
    headers = dataset.pop(0)  # Pop Headers
    return dataset


def formAddress(line):
    address = line[1]
    return address


# Our Coordinate_Module may return -1,-1 if Address not found -> this checks that our lat/long is actually valid.
def validCoordinates(lat, long):
    if lat != -1 and long != -1:
        return True
    return False


def writeDataset(data, path):
    with open(path, "w", encoding='utf-8', newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerows(data)


# TODO: This is main.
if __name__ == '__main__':
    path = "Colleges of Nursing/"  # Path to our dataset
    inputFile = "ACEN Colleges of Nursing.csv"
    outputFile = "ACEN Colleges of Nursing_Coordinates_v2.csv"

    updatedDataset = []
    for line in getDataset(path=path+inputFile):
        address = formAddress(line)
        lat, long = Coordinates_Module.getCoordinates(address)  # Module Prints its status + handles timeout errors

        if validCoordinates(lat, long):
            updatedDataset.append(line + [lat, long])   # Add coord if address Exists
        else:
            print("** Invalid Address  ->  Using School Name **", end='')
            # Get coordinates based on school name if address DNE
            lat, long = Coordinates_Module.getCoordinates(line[0] + ", " + line[3])
            if validCoordinates(lat, long):
                updatedDataset.append(line + [lat, long])
            else:
                print("**** Invalid Address || Invalid School Name ****")
                updatedDataset.append(line + ["-1", "-1"])  # Add "fluff" if address DNE

    print(tabulate(updatedDataset))
    writeDataset(data=updatedDataset, path=path+outputFile)
