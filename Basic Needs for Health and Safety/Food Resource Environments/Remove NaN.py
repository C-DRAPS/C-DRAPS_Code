# TODO: This program converts "NaN" values from our datasets to "0". We do this separately because it was
#  useful to know which counties had null values initially. Now, as we graph the data in ArcGIS, our numerical
#  columns can't have "NaN" or it won't plot the data. This is why this program exists.
import csv
import os


rootDir = "2015-2022"  # Get files from this dir
for file in os.listdir(rootDir):
    print(f">> {file}")
    # Get data
    data = []
    with open(f"{rootDir}/{file}", "r", encoding='utf-8') as csvFile:
        csvReader = csv.reader(csvFile)
        headers = csvFile.readline().strip().split(",")
        for line in csvReader:
            if line[2].lower() != "nan":
                data.append([line[0], line[1], line[2], line[3], line[4], line[5]])
            else:
                data.append([line[0], line[1], 0, line[3], line[4], line[5]])
    data.insert(0, headers)

    # Re-write data to file
    with open(f"{rootDir}/{file}", "w", newline='', encoding='utf-8') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerows(data)
