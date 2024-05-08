# TODO: This program reads our .xslx files (given a folder path) and outputs as .csv (so we can standardize)
import pandas
import os


# Gets a list of all .xlsx files in a folder (to convert to .csv)
def getFilePaths(path):
    files = []
    for fileName in os.listdir(path):
        if fileName != "Modified":  # Skips our folder from being added to list of .xlsx files
            files.append(path + "/" + fileName)
    return files


# Given a file, it:
#  1. Scrapes useful data (dataFrame obj.)
#  2. Converts dataFrame obj. -> CSV obj.
#  3. Writes CSV obj. to .csv File
def scrapeData(file):
    dataFrame = pandas.read_excel(file, sheet_name='REPORT', skiprows=4)
    path = generateNewPath(file)  # Generates a new path to write our scraped CSV data
    return dataFrame.to_csv(path, index=False)


# Given a string obj, writes it as a .csv file
def generateNewPath(path):
    # Generate a new file path
    newFilePath = path.split("/")
    newFilePath = "/".join(newFilePath[0:len(newFilePath)-1]) + "/Modified/" + newFilePath[len(newFilePath)-1]
    newFilePath = newFilePath.replace('.xlsx', '.csv')
    return newFilePath


# TODO: This is main.
for filePath in getFilePaths("SDWIS stuff/Original Datasets/2010"):
    scrapeData(filePath)
    print('Finished ' + '"' + filePath + '"')
