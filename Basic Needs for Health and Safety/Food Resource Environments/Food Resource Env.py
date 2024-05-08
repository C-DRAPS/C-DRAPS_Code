# TODO: This program pulls specific variables from our Food Environment Atlas.xlsx file (raw). Program does not
#  standardize names.
import csv
import pandas


def getDataFrame(sheetName):
    if sheetName == "PRICES_TAXES":
        sheetName = "TAXES"  # Original authors forgot to change this var :)

    df = pandas.read_excel('RAW Datasets/FoodEnvironmentAtlas.xls', sheet_name=sheetName)
    return df


# Gets the following var attributes:
#    1. Category Code - The Excel page our data is located in
#    2. Variable Name - Ex, "Population, low access to store, 2010"
#    3. Variable Code - The header where our data is located in
#    4. Units         - Units used for our data (percentage, whole numbers)
def getVariablesList(df):
    variables = []

    i = 0
    while i < len(df['Variable Name']):
        sheetName = df.at[i, 'Category Code']
        variableName = df.at[i, 'Variable Name']
        code = df.at[i, 'Variable Code']
        units = df.at[i, 'Units']

        variables.append([variableName, sheetName, code, units])
        i += 1

    return variables


# Remove chars that are unnecessary or mess up our file paths when writing to datasets
def cleanVarName(var):
    var = var.replace(',', '')
    var = var.replace('/', ' per ')
    var = var.replace('*', '')
    return var


def generateDataset(df, varName, code, units):
    if code == "PCH_LACCESS_CHILD_10_15":
        code = "LACCESS_CHILD_10_15"  # Original authors forgot to change this var :)

    data = [["State", "County", f"{varName} ({code})", "Units", "FIPS"]]
    try:
        i = 0
        while i < len(df[code]):
            data.append([df.at[i, 'State'], df.at[i, 'County'], df.at[i, code], units, df.at[i, 'FIPS']])
            i += 1
    except KeyError:
        print(f"\n-- UNABLE TO PROCESS DATASET {code}\n")
    return data


if __name__ == "__main__":
    df = getDataFrame(sheetName=' Variable List')
    # headers = df.iloc[0]

    variables = getVariablesList(df)

    for variable in variables:
        variableName = cleanVarName(variable[0])
        sheet = variable[1]
        code = variable[2]
        units = variable[3]

        df = getDataFrame(sheetName=sheet)
        dataset = generateDataset(df, variableName, code, units)

        for item in dataset:
            print(item)
        breakpoint()

        with open(f"Generated Datasets/{variableName}.csv", "w", newline='', encoding='utf-8') as csvFile:
            csvWriter = csv.writer(csvFile)
            csvWriter.writerows(dataset)
            print(f"Generated Dataset: {variableName}.csv")
