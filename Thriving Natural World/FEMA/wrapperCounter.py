# TODO: This file serves as a "wrapper" that applies the counter.py program to each file in our
#  "DRASTIC File Structure Copycat"
import counter as counter
import os


# Get all filepaths from "DRASTIC File Structure Copycat" (don't care if structure is preserved)
def compileAllFiles():
    basePath = "C:\\Users\\ferramos\\Desktop\\FEMA Rebuild\\DRASTIC File Structure Copycat"

    files = []
    groupYearFolders = os.listdir(basePath)
    for folderYear in groupYearFolders:  # Enter Group Years
        for disasterFolder in os.listdir(basePath + "\\" + folderYear):  # Enter Disaster Types
            for file in os.listdir(basePath + "\\" + folderYear + "\\" + disasterFolder):  # Enter Individual File Names
                filePath = basePath + "\\" + folderYear + "\\" + disasterFolder + "\\" + file
                if filePath.find("(freq)") == -1:  # In case we already ran, ignore those files
                    files.append(filePath)  # Append the full individual file path

    for item in files:
        print(item)

    return files


for file in compileAllFiles():
    if file.find("2020+ FEMA Disasters") != -1:
        counter.findFreq(file, 2020, 2022)
    elif file.find("2010_2019 FEMA Disasters") != -1:
        counter.findFreq(file, 2010, 2019)
    else:
        counter.findFreq(file, 2000, 2009)
