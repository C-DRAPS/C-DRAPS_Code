# TODO: This gets CENSUS demographics in 2010, using API Calls
# Ex: https://api.census.gov/data/2010/dec/sf1/examples.html
# Var: https://api.census.gov/data/2010/dec/sf1/variables.html
# Title: Decennial SF1
# Found from: https://api.census.gov/data.html

import requests
from tabulate import tabulate
import csv
from Location import Location  # Contains our County Location Objs (in a separate file)


# Compiles data we collected & Writes to our .txt database
def writeToDatabase(countiesList):
    with open("C:\\Users\\ferramos\\Desktop\\Census_API_Calls\\Databases\\2010 Census\\2010 Census Database.csv", "w", newline='') as csvfile:
        database = csv.writer(csvfile)

        # Write Custom Headers
        headers = ["State", "County", "Males", "Females", "Under 6 years", "6 to 18 years", "19 to 25 years",
                   "26 to 34 years", "35 to 44 years", "45 to 54 years", "55 to 64 years", "65 to 74 years",
                   "75 years and above", "White alone", "Black or African American alone",
                   "American Indian and Alaska Native alone", "Asian alone",
                   "Native Hawaiian and other Pacific Islander alone", "Some other race alone", "Two or more races",
                   "Hispanic or Latino (of any race)", "White alone (not hispanic or Latino)", "Under $25,000",
                   "$25,000 to $49,999", "$50,000 to $74,999", "$75,000 to $99,999", "$100,000 and over", "Employed",
                   "Unemployed", "Not in labor force"]
        database.writerow(headers)

        # Write Data from each County Location
        for county in countiesList:
            rowData = []
            rowData.append(county.getState())
            rowData.append(county.getCounty())
            rowData.append(county.getTotalMales())
            rowData.append(county.getTotalFemales())
            rowData.append(county.getAgeUnder6yrs())
            rowData.append(county.getAge6to18yrs())
            rowData.append(county.getAge19to25yrs())
            rowData.append(county.getAge26to34yrs())
            rowData.append(county.getAge35to44yrs())
            rowData.append(county.getAge45to54yrs())
            rowData.append(county.getAge55to64yrs())
            rowData.append(county.getAge65to74yrs())
            rowData.append(county.getAgeAbove75yrs())
            rowData.append(county.getWhiteAlone())
            rowData.append(county.getBlackAlone())
            rowData.append(county.getIndianAlone())
            rowData.append(county.getAsianAlone())
            rowData.append(county.getHawaiianAlone())
            rowData.append(county.getOtherRaceAlone())
            rowData.append(county.getTwoOrMoreRaces())
            rowData.append(county.getHispanicOrLatino())
            rowData.append(county.getWhiteAlone_NotHisp())

            rowData.append(county.getIncomeUnder25K())
            rowData.append(county.getIncome25Kto49K())
            rowData.append(county.getIncome50Kto74K())
            rowData.append(county.getIncome75Kto99K())
            rowData.append(county.getIncome100KOver())
            rowData.append(county.getEmployed())
            rowData.append(county.getUnemployed())
            rowData.append(county.getNotinLaborForce())

            database.writerow(rowData)  # Write to our .csv database
    csvfile.close()


# Prints organized JSON Request
def printRequest(countiesList):
    rowData = []
    for county in countiesList:
        # 2D Array, add this data to 1 line array
        countyData = []
        countyData.append(county.getState())
        countyData.append(county.getCounty())
        countyData.append(county.getTotalMales())
        countyData.append(county.getTotalFemales())
        countyData.append(county.getWhiteAlone())
        countyData.append(county.getBlackAlone())
        countyData.append(county.getIndianAlone())
        countyData.append(county.getAsianAlone())
        countyData.append(county.getHawaiianAlone())
        countyData.append(county.getOtherRaceAlone())
        countyData.append(county.getTwoOrMoreRaces())
        countyData.append(county.getHispanicOrLatino())
        countyData.append(county.getWhiteAlone_NotHisp())

        # 2D Array, add this array to rowData to be formatted by tabulate
        rowData.append(countyData)

    # Print results
    print("\n")  # Formatting
    headers = ["State", "County", "Males", "Females", "White alone", "Black or African American alone",
                "American Indian and Alaska Native alone", "Asian alone",
                "Native Hawaiian and other Pacific Islander alone", "Some other race alone", "Two or more races",
                "Hispanic or Latino (of any race)", "White alone (not hispanic or Latino)"]
    print(tabulate(rowData, headers=headers))


# Creates an array where our variable tables will live (male, female, race).
#  We coded it like this so that we (humans) can see what code each variable is assigned to.
def compile_SF_Tables():
    variables = []

    malesTable = "PCT012002"
    femalesTable = "PCT012106"
    whiteAlone = "P003002"
    blackAlone = "P003003"
    indianAlone = "P003004"
    asianAlone = "P003005"
    hawaiianAlone = "P003006"
    otherRaceAlone = "P003007"
    twoOrMoreRaces = "P003008"
    hispanic = "P009002"
    whiteNotHispanic = "P005003"

    ages = "SEE SF README TABLE!"  # 2000's age groups split by males/female
    ageUnder1yr_male = "PCT012003"
    age1yrs_male = "PCT012004"
    age2yrs_male = "PCT012005"
    age3yrs_male = "PCT012006"
    age4yrs_male = "PCT012007"
    age5yrs_male = "PCT012008"
    age6yrs_male = "PCT012009"
    age7yrs_male = "PCT012010"
    age8yrs_male = "PCT012011"
    age9yrs_male = "PCT012012"
    age10yrs_male = "PCT012013"
    age11yrs_male = "PCT012014"
    age12yrs_male = "PCT012015"
    age13yrs_male = "PCT012016"
    age14yrs_male = "PCT012017"
    age15yrs_male = "PCT012018"
    age16yrs_male = "PCT012019"
    age17yrs_male = "PCT012020"
    age18yrs_male = "PCT012021"
    age19yrs_male = "PCT012022"
    age20yrs_male = "PCT012023"
    age21yrs_male = "PCT012024"
    age22yrs_male = "PCT012025"
    age23yrs_male = "PCT012026"
    age24yrs_male = "PCT012027"
    age25yrs_male = "PCT012028"
    age26yrs_male = "PCT012029"
    age27yrs_male = "PCT012030"
    age28yrs_male = "PCT012031"
    age29yrs_male = "PCT012032"
    age30yrs_male = "PCT012033"
    age31yrs_male = "PCT012034"
    age32yrs_male = "PCT012035"
    age33yrs_male = "PCT012036"
    age34yrs_male = "PCT012037"
    age35yrs_male = "PCT012038"
    age36yrs_male = "PCT012039"
    age37yrs_male = "PCT012040"
    age38yrs_male = "PCT012041"
    age39yrs_male = "PCT012042"
    age40yrs_male = "PCT012043"
    age41yrs_male = "PCT012044"
    age42yrs_male = "PCT012045"
    age43yrs_male = "PCT012046"
    age44yrs_male = "PCT012047"
    age45yrs_male = "PCT012048"
    age46yrs_male = "PCT012049"
    age47yrs_male = "PCT012050"
    age48yrs_male = "PCT012051"
    age49yrs_male = "PCT012052"
    age50yrs_male = "PCT012053"
    age51yrs_male = "PCT012054"
    age52yrs_male = "PCT012055"
    age53yrs_male = "PCT012056"
    age54yrs_male = "PCT012057"
    age55yrs_male = "PCT012058"
    age56yrs_male = "PCT012059"
    age57yrs_male = "PCT012060"
    age58yrs_male = "PCT012061"
    age59yrs_male = "PCT012062"
    age60yrs_male = "PCT012063"
    age61yrs_male = "PCT012064"
    age62yrs_male = "PCT012065"
    age63yrs_male = "PCT012066"
    age64yrs_male = "PCT012067"
    age65yrs_male = "PCT012068"
    age66yrs_male = "PCT012069"
    age67yrs_male = "PCT012070"
    age68yrs_male = "PCT012071"
    age69yrs_male = "PCT012072"
    age70yrs_male = "PCT012073"
    age71yrs_male = "PCT012074"
    age72yrs_male = "PCT012075"
    age73yrs_male = "PCT012076"
    age74yrs_male = "PCT012077"
    age75yrs_male = "PCT012078"
    age76yrs_male = "PCT012079"
    age77yrs_male = "PCT012080"
    age78yrs_male = "PCT012081"
    age79yrs_male = "PCT012082"
    age80yrs_male = "PCT012083"
    age81yrs_male = "PCT012084"
    age82yrs_male = "PCT012085"
    age83yrs_male = "PCT012086"
    age84yrs_male = "PCT012087"
    age85yrs_male = "PCT012088"
    age86yrs_male = "PCT012089"
    age87yrs_male = "PCT012090"
    age88yrs_male = "PCT012091"
    age89yrs_male = "PCT012092"
    age90yrs_male = "PCT012093"
    age91yrs_male = "PCT012094"
    age92yrs_male = "PCT012095"
    age93yrs_male = "PCT012096"
    age94yrs_male = "PCT012097"
    age95yrs_male = "PCT012098"
    age96yrs_male = "PCT012099"
    age97yrs_male = "PCT012100"
    age98yrs_male = "PCT012101"
    age99yrs_male = "PCT012102"
    age100_104yrs_male = "PCT012103"
    age105_108yrs_male = "PCT012104"
    ageOver110yrs_male = "PCT012105"

    ageUnder1yr_female = "PCT012107"
    age1yrs_female = "PCT012108"
    age2yrs_female = "PCT012109"
    age3yrs_female = "PCT012110"
    age4yrs_female = "PCT012111"
    age5yrs_female = "PCT012112"
    age6yrs_female = "PCT012113"
    age7yrs_female = "PCT012114"
    age8yrs_female = "PCT012115"
    age9yrs_female = "PCT012116"
    age10yrs_female = "PCT012117"
    age11yrs_female = "PCT012118"
    age12yrs_female = "PCT012119"
    age13yrs_female = "PCT012120"
    age14yrs_female = "PCT012121"
    age15yrs_female = "PCT012122"
    age16yrs_female = "PCT012123"
    age17yrs_female = "PCT012124"
    age18yrs_female = "PCT012125"
    age19yrs_female = "PCT012126"
    age20yrs_female = "PCT012127"
    age21yrs_female = "PCT012128"
    age22yrs_female = "PCT012129"
    age23yrs_female = "PCT012130"
    age24yrs_female = "PCT012131"
    age25yrs_female = "PCT012132"
    age26yrs_female = "PCT012133"
    age27yrs_female = "PCT012134"
    age28yrs_female = "PCT012135"
    age29yrs_female = "PCT012136"
    age30yrs_female = "PCT012137"
    age31yrs_female = "PCT012138"
    age32yrs_female = "PCT012139"
    age33yrs_female = "PCT012140"
    age34yrs_female = "PCT012141"
    age35yrs_female = "PCT012142"
    age36yrs_female = "PCT012143"
    age37yrs_female = "PCT012144"
    age38yrs_female = "PCT012145"
    age39yrs_female = "PCT012146"
    age40yrs_female = "PCT012147"
    age41yrs_female = "PCT012148"
    age42yrs_female = "PCT012149"
    age43yrs_female = "PCT012150"
    age44yrs_female = "PCT012151"
    age45yrs_female = "PCT012152"
    age46yrs_female = "PCT012153"
    age47yrs_female = "PCT012154"
    age48yrs_female = "PCT012155"
    age49yrs_female = "PCT012156"
    age50yrs_female = "PCT012157"
    age51yrs_female = "PCT012158"
    age52yrs_female = "PCT012159"
    age53yrs_female = "PCT012160"
    age54yrs_female = "PCT012161"
    age55yrs_female = "PCT012162"
    age56yrs_female = "PCT012163"
    age57yrs_female = "PCT012164"
    age58yrs_female = "PCT012165"
    age59yrs_female = "PCT012166"
    age60yrs_female = "PCT012167"
    age61yrs_female = "PCT012168"
    age62yrs_female = "PCT012169"
    age63yrs_female = "PCT012170"
    age64yrs_female = "PCT012171"
    age65yrs_female = "PCT012172"
    age66yrs_female = "PCT012173"
    age67yrs_female = "PCT012174"
    age68yrs_female = "PCT012175"
    age69yrs_female = "PCT012176"
    age70yrs_female = "PCT012177"
    age71yrs_female = "PCT012178"
    age72yrs_female = "PCT012179"
    age73yrs_female = "PCT012180"
    age74yrs_female = "PCT012181"
    age75yrs_female = "PCT012182"
    age76yrs_female = "PCT012183"
    age77yrs_female = "PCT012184"
    age78yrs_female = "PCT012185"
    age79yrs_female = "PCT012186"
    age80yrs_female = "PCT012187"
    age81yrs_female = "PCT012188"
    age82yrs_female = "PCT012189"
    age83yrs_female = "PCT012190"
    age84yrs_female = "PCT012191"
    age85yrs_female = "PCT012192"
    age86yrs_female = "PCT012193"
    age87yrs_female = "PCT012194"
    age88yrs_female = "PCT012195"
    age89yrs_female = "PCT012196"
    age90yrs_female = "PCT012197"
    age91yrs_female = "PCT012198"
    age92yrs_female = "PCT012199"
    age93yrs_female = "PCT012200"
    age94yrs_female = "PCT012201"
    age95yrs_female = "PCT012202"
    age96yrs_female = "PCT012203"
    age97yrs_female = "PCT012204"
    age98yrs_female = "PCT012205"
    age99yrs_female = "PCT012206"
    age100_104yrs_female = "PCT012207"
    age105_108yrs_female = "PCT012208"
    ageOver110yrs_female = "PCT012209"

    variables.append(malesTable)
    variables.append(femalesTable)
    variables.append(whiteAlone)
    variables.append(blackAlone)
    variables.append(indianAlone)
    variables.append(asianAlone)
    variables.append(hawaiianAlone)
    variables.append(otherRaceAlone)
    variables.append(twoOrMoreRaces)
    variables.append(hispanic)
    variables.append(whiteNotHispanic)

    variables.append(ageUnder1yr_male)
    variables.append(age1yrs_male)
    variables.append(age2yrs_male)
    variables.append(age3yrs_male)
    variables.append(age4yrs_male)
    variables.append(age5yrs_male)
    variables.append(age6yrs_male)
    variables.append(age7yrs_male)
    variables.append(age8yrs_male)
    variables.append(age9yrs_male)
    variables.append(age10yrs_male)
    variables.append(age11yrs_male)
    variables.append(age12yrs_male)
    variables.append(age13yrs_male)
    variables.append(age14yrs_male)
    variables.append(age15yrs_male)
    variables.append(age16yrs_male)
    variables.append(age17yrs_male)
    variables.append(age18yrs_male)
    variables.append(age19yrs_male)
    variables.append(age20yrs_male)
    variables.append(age21yrs_male)
    variables.append(age22yrs_male)
    variables.append(age23yrs_male)
    variables.append(age24yrs_male)
    variables.append(age25yrs_male)
    variables.append(age26yrs_male)
    variables.append(age27yrs_male)
    variables.append(age28yrs_male)
    variables.append(age29yrs_male)
    variables.append(age30yrs_male)
    variables.append(age31yrs_male)
    variables.append(age32yrs_male)
    variables.append(age33yrs_male)
    variables.append(age34yrs_male)
    variables.append(age35yrs_male)
    variables.append(age36yrs_male)
    variables.append(age37yrs_male)
    variables.append(age38yrs_male)
    variables.append(age39yrs_male)
    variables.append(age40yrs_male)
    variables.append(age41yrs_male)
    variables.append(age42yrs_male)
    variables.append(age43yrs_male)
    variables.append(age44yrs_male)
    variables.append(age45yrs_male)
    variables.append(age46yrs_male)
    variables.append(age47yrs_male)
    variables.append(age48yrs_male)
    variables.append(age49yrs_male)
    variables.append(age50yrs_male)
    variables.append(age51yrs_male)
    variables.append(age52yrs_male)
    variables.append(age53yrs_male)
    variables.append(age54yrs_male)
    variables.append(age55yrs_male)
    variables.append(age56yrs_male)
    variables.append(age57yrs_male)
    variables.append(age58yrs_male)
    variables.append(age59yrs_male)
    variables.append(age60yrs_male)
    variables.append(age61yrs_male)
    variables.append(age62yrs_male)
    variables.append(age63yrs_male)
    variables.append(age64yrs_male)
    variables.append(age65yrs_male)
    variables.append(age66yrs_male)
    variables.append(age67yrs_male)
    variables.append(age68yrs_male)
    variables.append(age69yrs_male)
    variables.append(age70yrs_male)
    variables.append(age71yrs_male)
    variables.append(age72yrs_male)
    variables.append(age73yrs_male)
    variables.append(age74yrs_male)
    variables.append(age75yrs_male)
    variables.append(age76yrs_male)
    variables.append(age77yrs_male)
    variables.append(age78yrs_male)
    variables.append(age79yrs_male)
    variables.append(age80yrs_male)
    variables.append(age81yrs_male)
    variables.append(age82yrs_male)
    variables.append(age83yrs_male)
    variables.append(age84yrs_male)
    variables.append(age85yrs_male)
    variables.append(age86yrs_male)
    variables.append(age87yrs_male)
    variables.append(age88yrs_male)
    variables.append(age89yrs_male)
    variables.append(age90yrs_male)
    variables.append(age91yrs_male)
    variables.append(age92yrs_male)
    variables.append(age93yrs_male)
    variables.append(age94yrs_male)
    variables.append(age95yrs_male)
    variables.append(age96yrs_male)
    variables.append(age97yrs_male)
    variables.append(age98yrs_male)
    variables.append(age99yrs_male)
    variables.append(age100_104yrs_male)
    variables.append(age105_108yrs_male)
    variables.append(ageOver110yrs_male)

    variables.append(ageUnder1yr_female)
    variables.append(age1yrs_female)
    variables.append(age2yrs_female)
    variables.append(age3yrs_female)
    variables.append(age4yrs_female)
    variables.append(age5yrs_female)
    variables.append(age6yrs_female)
    variables.append(age7yrs_female)
    variables.append(age8yrs_female)
    variables.append(age9yrs_female)
    variables.append(age10yrs_female)
    variables.append(age11yrs_female)
    variables.append(age12yrs_female)
    variables.append(age13yrs_female)
    variables.append(age14yrs_female)
    variables.append(age15yrs_female)
    variables.append(age16yrs_female)
    variables.append(age17yrs_female)
    variables.append(age18yrs_female)
    variables.append(age19yrs_female)
    variables.append(age20yrs_female)
    variables.append(age21yrs_female)
    variables.append(age22yrs_female)
    variables.append(age23yrs_female)
    variables.append(age24yrs_female)
    variables.append(age25yrs_female)
    variables.append(age26yrs_female)
    variables.append(age27yrs_female)
    variables.append(age28yrs_female)
    variables.append(age29yrs_female)
    variables.append(age30yrs_female)
    variables.append(age31yrs_female)
    variables.append(age32yrs_female)
    variables.append(age33yrs_female)
    variables.append(age34yrs_female)
    variables.append(age35yrs_female)
    variables.append(age36yrs_female)
    variables.append(age37yrs_female)
    variables.append(age38yrs_female)
    variables.append(age39yrs_female)
    variables.append(age40yrs_female)
    variables.append(age41yrs_female)
    variables.append(age42yrs_female)
    variables.append(age43yrs_female)
    variables.append(age44yrs_female)
    variables.append(age45yrs_female)
    variables.append(age46yrs_female)
    variables.append(age47yrs_female)
    variables.append(age48yrs_female)
    variables.append(age49yrs_female)
    variables.append(age50yrs_female)
    variables.append(age51yrs_female)
    variables.append(age52yrs_female)
    variables.append(age53yrs_female)
    variables.append(age54yrs_female)
    variables.append(age55yrs_female)
    variables.append(age56yrs_female)
    variables.append(age57yrs_female)
    variables.append(age58yrs_female)
    variables.append(age59yrs_female)
    variables.append(age60yrs_female)
    variables.append(age61yrs_female)
    variables.append(age62yrs_female)
    variables.append(age63yrs_female)
    variables.append(age64yrs_female)
    variables.append(age65yrs_female)
    variables.append(age66yrs_female)
    variables.append(age67yrs_female)
    variables.append(age68yrs_female)
    variables.append(age69yrs_female)
    variables.append(age70yrs_female)
    variables.append(age71yrs_female)
    variables.append(age72yrs_female)
    variables.append(age73yrs_female)
    variables.append(age74yrs_female)
    variables.append(age75yrs_female)
    variables.append(age76yrs_female)
    variables.append(age77yrs_female)
    variables.append(age78yrs_female)
    variables.append(age79yrs_female)
    variables.append(age80yrs_female)
    variables.append(age81yrs_female)
    variables.append(age82yrs_female)
    variables.append(age83yrs_female)
    variables.append(age84yrs_female)
    variables.append(age85yrs_female)
    variables.append(age86yrs_female)
    variables.append(age87yrs_female)
    variables.append(age88yrs_female)
    variables.append(age89yrs_female)
    variables.append(age90yrs_female)
    variables.append(age91yrs_female)
    variables.append(age92yrs_female)
    variables.append(age93yrs_female)
    variables.append(age94yrs_female)
    variables.append(age95yrs_female)
    variables.append(age96yrs_female)
    variables.append(age97yrs_female)
    variables.append(age98yrs_female)
    variables.append(age99yrs_female)
    variables.append(age100_104yrs_female)
    variables.append(age105_108yrs_female)
    variables.append(ageOver110yrs_female)

    return variables


# Creates an array where our variable tables will live (male, female, race)
def compile_EmployIncome_Tables():
    variables = []
    employed = "C24010_001E"
    unemployed_16to19_Males = "B23001_008E"
    unemployed_20to21_Males = "B23001_015E"
    unemployed_22to24_Males = "B23001_022E"
    unemployed_25to29_Males = "B23001_029E"
    unemployed_30to34_Males = "B23001_036E"
    unemployed_35to44_Males = "B23001_043E"
    unemployed_45to54_Males = "B23001_050E"
    unemployed_55to59_Males = "B23001_057E"
    unemployed_60to61_Males = "B23001_064E"
    unemployed_62to64_Males = "B23001_071E"
    unemployed_65to69_Males = "B23001_076E"
    unemployed_70to74_Males = "B23001_081E"
    unemployed_75Over_Males = "B23001_086E"
    unemployed_16to19_Females = "B23001_094E"
    unemployed_20to21_Females = "B23001_101E"
    unemployed_22to24_Females = "B23001_108E"
    unemployed_25to29_Females = "B23001_115E"
    unemployed_30to34_Females = "B23001_122E"
    unemployed_35to44_Females = "B23001_129E"
    unemployed_45to54_Females = "B23001_136E"
    unemployed_55to59_Females = "B23001_143E"
    unemployed_60to61_Females = "B23001_150E"
    unemployed_62to64_Females = "B23001_157E"
    unemployed_65to69_Females = "B23001_162E"
    unemployed_70to74_Females = "B23001_167E"
    unemployed_75Over_Females = "B23001_172E"

    notInLaborForce_16to19_Males = "B23001_009E"
    notInLaborForce_20to21_Males = "B23001_016E"
    notInLaborForce_22to24_Males = "B23001_023E"
    notInLaborForce_25to29_Males = "B23001_030E"
    notInLaborForce_30to34_Males = "B23001_037E"
    notInLaborForce_35to44_Males = "B23001_044E"
    notInLaborForce_45to54_Males = "B23001_051E"
    notInLaborForce_55to59_Males = "B23001_058E"
    notInLaborForce_60to61_Males = "B23001_065E"
    notInLaborForce_62to64_Males = "B23001_072E"
    notInLaborForce_65to69_Males = "B23001_077E"
    notInLaborForce_70to74_Males = "B23001_082E"
    notInLaborForce_75Over_Males = "B23001_087E"
    notInLaborForce_16to19_Females = "B23001_095E"
    notInLaborForce_20to21_Females = "B23001_102E"
    notInLaborForce_22to24_Females = "B23001_109E"
    notInLaborForce_25to29_Females = "B23001_116E"
    notInLaborForce_30to34_Females = "B23001_123E"
    notInLaborForce_35to44_Females = "B23001_130E"
    notInLaborForce_45to54_Females = "B23001_137E"
    notInLaborForce_55to59_Females = "B23001_144E"
    notInLaborForce_60to61_Females = "B23001_151E"
    notInLaborForce_62to64_Females = "B23001_158E"
    notInLaborForce_65to69_Females = "B23001_163E"
    notInLaborForce_70to74_Females = "B23001_168E"
    notInLaborForce_75Over_Females = "B23001_173E"

    income_Less_than_10K = "B19001_002E"
    income_10Kto14K = "B19001_003E"
    income_15Kto19K = "B19001_004E"
    income_20Kto24K = "B19001_005E"
    income_25Kto29K = "B19001_006E"
    income_30Kto34K = "B19001_007E"
    income_35Kto39K = "B19001_008E"
    income_40Kto44K = "B19001_009E"
    income_45Kto49K = "B19001_010E"
    income_50Kto59K = "B19001_011E"
    income_60Kto74K = "B19001_012E"
    income_75Kto99K = "B19001_013E"
    income_100Kto124K = "B19001_014E"
    income_125Kto149K = "B19001_015E"
    income_150Kto199K = "B19001_016E"
    income_200KOver = "B19001_017E"

    variables.append(employed)
    variables.append(unemployed_16to19_Males)
    variables.append(unemployed_20to21_Males)
    variables.append(unemployed_22to24_Males)
    variables.append(unemployed_25to29_Males)
    variables.append(unemployed_30to34_Males)
    variables.append(unemployed_35to44_Males)
    variables.append(unemployed_45to54_Males)
    variables.append(unemployed_55to59_Males)
    variables.append(unemployed_60to61_Males)
    variables.append(unemployed_62to64_Males)
    variables.append(unemployed_65to69_Males)
    variables.append(unemployed_70to74_Males)
    variables.append(unemployed_75Over_Males)
    variables.append(unemployed_16to19_Females)
    variables.append(unemployed_20to21_Females)
    variables.append(unemployed_22to24_Females)
    variables.append(unemployed_25to29_Females)
    variables.append(unemployed_30to34_Females)
    variables.append(unemployed_35to44_Females)
    variables.append(unemployed_45to54_Females)
    variables.append(unemployed_55to59_Females)
    variables.append(unemployed_60to61_Females)
    variables.append(unemployed_62to64_Females)
    variables.append(unemployed_65to69_Females)
    variables.append(unemployed_70to74_Females)
    variables.append(unemployed_75Over_Females)
    variables.append(notInLaborForce_16to19_Males)
    variables.append(notInLaborForce_20to21_Males)
    variables.append(notInLaborForce_22to24_Males)
    variables.append(notInLaborForce_25to29_Males)
    variables.append(notInLaborForce_30to34_Males)
    variables.append(notInLaborForce_35to44_Males)
    variables.append(notInLaborForce_45to54_Males)
    variables.append(notInLaborForce_55to59_Males)
    variables.append(notInLaborForce_60to61_Males)
    variables.append(notInLaborForce_62to64_Males)
    variables.append(notInLaborForce_65to69_Males)
    variables.append(notInLaborForce_70to74_Males)
    variables.append(notInLaborForce_75Over_Males)
    variables.append(notInLaborForce_16to19_Females)
    variables.append(notInLaborForce_20to21_Females)
    variables.append(notInLaborForce_22to24_Females)
    variables.append(notInLaborForce_25to29_Females)
    variables.append(notInLaborForce_30to34_Females)
    variables.append(notInLaborForce_35to44_Females)
    variables.append(notInLaborForce_45to54_Females)
    variables.append(notInLaborForce_55to59_Females)
    variables.append(notInLaborForce_60to61_Females)
    variables.append(notInLaborForce_62to64_Females)
    variables.append(notInLaborForce_65to69_Females)
    variables.append(notInLaborForce_70to74_Females)
    variables.append(notInLaborForce_75Over_Females)
    variables.append(income_Less_than_10K)
    variables.append(income_10Kto14K)
    variables.append(income_15Kto19K)
    variables.append(income_20Kto24K)
    variables.append(income_25Kto29K)
    variables.append(income_30Kto34K)
    variables.append(income_35Kto39K)
    variables.append(income_40Kto44K)
    variables.append(income_45Kto49K)
    variables.append(income_50Kto59K)
    variables.append(income_60Kto74K)
    variables.append(income_75Kto99K)
    variables.append(income_100Kto124K)
    variables.append(income_125Kto149K)
    variables.append(income_150Kto199K)
    variables.append(income_200KOver)

    return variables


# Creates a list of all county objects, so we can insert data into them.
#  calls the base-model API to get all the counties.
def createCountyObjs():
    counties = []

    # Type this into google to see what we're pulling
    #  https://api.census.gov/data/2010/dec/sf1?get=NAME&for=county:*&key=643a663a4ca7ea22d3d4e69e2721a9ba250f96b7
    jsonPackage = requests.get(base_url + "?get=NAME&for=county:*&key=" + API_Key).json()
    jsonPackage.pop(0)
    for item in jsonPackage:
        censusName = item[0]
        counties.append(Location(censusName))

    return counties  # Return full list of county objects


# Building Request + Adding Data to County Objs
base_url = "http://api.census.gov/data/2010/dec/sf1"
API_Key = "YOUR_API_KEY_HERE"
countyObjs = createCountyObjs()
print("[x] County Location Objs...")
tables = compile_SF_Tables()
print("[x] Compiling Tables...")
print("[ ] Running Data Allocation...")
for table in tables:
    # Call 1 Table at a time
    var = "?get=NAME," + table + "&for=county:*"
    package = base_url + var + "&key=" + API_Key
    request = requests.get(package).json()

    # Add table data to each object
    tableName = request.pop(0)[1]  # Get what type of data we're dealing w/ (white alone, total males, etc.)
    for tableData in request:
        for county in countyObjs:
            location = tableData[0]

            # New table data location == created county obj location -> Add this new data to it
            if location == county.getCensusName():
                # print("  >> Match! " + location + " == " + county.getCensusName())
                # Add data to corresponding data type (Note: "MATCH" keyword for python version 10+)
                match tableName:
                    case "P003002":
                        county.setWhiteAlone(int(tableData[1]))
                    case "P003003":
                        county.setBlackAlone(int(tableData[1]))
                    case "P003004":
                        county.setIndianAlone(int(tableData[1]))
                    case "P003005":
                        county.setAsianAlone(int(tableData[1]))
                    case "P003006":
                        county.setHawaiianAlone(int(tableData[1]))
                    case "P003007":
                        county.setOtherRaceAlone(int(tableData[1]))
                    case "P003008":
                        county.setTwoOrMoreRaces(int(tableData[1]))
                    case "P009002":
                        county.setHispanicOrLatino(int(tableData[1]))
                    case "P005003":
                        county.setWhiteAlone_NotHisp(int(tableData[1]))
                    case "PCT012002":
                        county.setTotalMales(int(tableData[1]))
                    case "PCT012106":
                        county.setTotalFemales(int(tableData[1]))
                    case "PCT012003":
                        county.setAgeUnder1yrs_males(int(tableData[1]))
                    case "PCT012004":
                        county.setAge1yrs_males(int(tableData[1]))
                    case "PCT012005":
                        county.setAge2yrs_males(int(tableData[1]))
                    case "PCT012006":
                        county.setAge3yrs_males(int(tableData[1]))
                    case "PCT012007":
                        county.setAge4yrs_males(int(tableData[1]))
                    case "PCT012008":
                        county.setAge5yrs_males(int(tableData[1]))
                    case "PCT012009":
                        county.setAge6yrs_males(int(tableData[1]))
                    case "PCT012010":
                        county.setAge7yrs_males(int(tableData[1]))
                    case "PCT012011":
                        county.setAge8yrs_males(int(tableData[1]))
                    case "PCT012012":
                        county.setAge9yrs_males(int(tableData[1]))
                    case "PCT012013":
                        county.setAge10yrs_males(int(tableData[1]))
                    case "PCT012014":
                        county.setAge11yrs_males(int(tableData[1]))
                    case "PCT012015":
                        county.setAge12yrs_males(int(tableData[1]))
                    case "PCT012016":
                        county.setAge13yrs_males(int(tableData[1]))
                    case "PCT012017":
                        county.setAge14yrs_males(int(tableData[1]))
                    case "PCT012018":
                        county.setAge15yrs_males(int(tableData[1]))
                    case "PCT012019":
                        county.setAge16yrs_males(int(tableData[1]))
                    case "PCT012020":
                        county.setAge17yrs_males(int(tableData[1]))
                    case "PCT012021":
                        county.setAge18yrs_males(int(tableData[1]))
                    case "PCT012022":
                        county.setAge19yrs_males(int(tableData[1]))
                    case "PCT012023":
                        county.setAge20yrs_males(int(tableData[1]))
                    case "PCT012024":
                        county.setAge21yrs_males(int(tableData[1]))
                    case "PCT012025":
                        county.setAge22yrs_males(int(tableData[1]))
                    case "PCT012026":
                        county.setAge23yrs_males(int(tableData[1]))
                    case "PCT012027":
                        county.setAge24yrs_males(int(tableData[1]))
                    case "PCT012028":
                        county.setAge25yrs_males(int(tableData[1]))
                    case "PCT012029":
                        county.setAge26yrs_males(int(tableData[1]))
                    case "PCT012030":
                        county.setAge27yrs_males(int(tableData[1]))
                    case "PCT012031":
                        county.setAge28yrs_males(int(tableData[1]))
                    case "PCT012032":
                        county.setAge29yrs_males(int(tableData[1]))
                    case "PCT012033":
                        county.setAge30yrs_males(int(tableData[1]))
                    case "PCT012034":
                        county.setAge31yrs_males(int(tableData[1]))
                    case "PCT012035":
                        county.setAge32yrs_males(int(tableData[1]))
                    case "PCT012036":
                        county.setAge33yrs_males(int(tableData[1]))
                    case "PCT012037":
                        county.setAge34yrs_males(int(tableData[1]))
                    case "PCT012038":
                        county.setAge35yrs_males(int(tableData[1]))
                    case "PCT012039":
                        county.setAge36yrs_males(int(tableData[1]))
                    case "PCT012040":
                        county.setAge37yrs_males(int(tableData[1]))
                    case "PCT012041":
                        county.setAge38yrs_males(int(tableData[1]))
                    case "PCT012042":
                        county.setAge39yrs_males(int(tableData[1]))
                    case "PCT012043":
                        county.setAge40yrs_males(int(tableData[1]))
                    case "PCT012044":
                        county.setAge41yrs_males(int(tableData[1]))
                    case "PCT012045":
                        county.setAge42yrs_males(int(tableData[1]))
                    case "PCT012046":
                        county.setAge43yrs_males(int(tableData[1]))
                    case "PCT012047":
                        county.setAge44yrs_males(int(tableData[1]))
                    case "PCT012048":
                        county.setAge45yrs_males(int(tableData[1]))
                    case "PCT012049":
                        county.setAge46yrs_males(int(tableData[1]))
                    case "PCT012050":
                        county.setAge47yrs_males(int(tableData[1]))
                    case "PCT012051":
                        county.setAge48yrs_males(int(tableData[1]))
                    case "PCT012052":
                        county.setAge49yrs_males(int(tableData[1]))
                    case "PCT012053":
                        county.setAge50yrs_males(int(tableData[1]))
                    case "PCT012054":
                        county.setAge51yrs_males(int(tableData[1]))
                    case "PCT012055":
                        county.setAge52yrs_males(int(tableData[1]))
                    case "PCT012056":
                        county.setAge53yrs_males(int(tableData[1]))
                    case "PCT012057":
                        county.setAge54yrs_males(int(tableData[1]))
                    case "PCT012058":
                        county.setAge55yrs_males(int(tableData[1]))
                    case "PCT012059":
                        county.setAge56yrs_males(int(tableData[1]))
                    case "PCT012060":
                        county.setAge57yrs_males(int(tableData[1]))
                    case "PCT012061":
                        county.setAge58yrs_males(int(tableData[1]))
                    case "PCT012062":
                        county.setAge59yrs_males(int(tableData[1]))
                    case "PCT012063":
                        county.setAge60yrs_males(int(tableData[1]))
                    case "PCT012064":
                        county.setAge61yrs_males(int(tableData[1]))
                    case "PCT012065":
                        county.setAge62yrs_males(int(tableData[1]))
                    case "PCT012066":
                        county.setAge63yrs_males(int(tableData[1]))
                    case "PCT012067":
                        county.setAge64yrs_males(int(tableData[1]))
                    case "PCT012068":
                        county.setAge65yrs_males(int(tableData[1]))
                    case "PCT012069":
                        county.setAge66yrs_males(int(tableData[1]))
                    case "PCT012070":
                        county.setAge67yrs_males(int(tableData[1]))
                    case "PCT012071":
                        county.setAge68yrs_males(int(tableData[1]))
                    case "PCT012072":
                        county.setAge69yrs_males(int(tableData[1]))
                    case "PCT012073":
                        county.setAge70yrs_males(int(tableData[1]))
                    case "PCT012074":
                        county.setAge71yrs_males(int(tableData[1]))
                    case "PCT012075":
                        county.setAge72yrs_males(int(tableData[1]))
                    case "PCT012076":
                        county.setAge73yrs_males(int(tableData[1]))
                    case "PCT012077":
                        county.setAge74yrs_males(int(tableData[1]))
                    case "PCT012078":
                        county.setAge75yrs_males(int(tableData[1]))
                    case "PCT012079":
                        county.setAge76yrs_males(int(tableData[1]))
                    case "PCT012080":
                        county.setAge77yrs_males(int(tableData[1]))
                    case "PCT012081":
                        county.setAge78yrs_males(int(tableData[1]))
                    case "PCT012082":
                        county.setAge79yrs_males(int(tableData[1]))
                    case "PCT012083":
                        county.setAge80yrs_males(int(tableData[1]))
                    case "PCT012084":
                        county.setAge81yrs_males(int(tableData[1]))
                    case "PCT012085":
                        county.setAge82yrs_males(int(tableData[1]))
                    case "PCT012086":
                        county.setAge83yrs_males(int(tableData[1]))
                    case "PCT012087":
                        county.setAge84yrs_males(int(tableData[1]))
                    case "PCT012088":
                        county.setAge85yrs_males(int(tableData[1]))
                    case "PCT012089":
                        county.setAge86yrs_males(int(tableData[1]))
                    case "PCT012090":
                        county.setAge87yrs_males(int(tableData[1]))
                    case "PCT012091":
                        county.setAge88yrs_males(int(tableData[1]))
                    case "PCT012092":
                        county.setAge89yrs_males(int(tableData[1]))
                    case "PCT012093":
                        county.setAge90yrs_males(int(tableData[1]))
                    case "PCT012094":
                        county.setAge91yrs_males(int(tableData[1]))
                    case "PCT012095":
                        county.setAge92yrs_males(int(tableData[1]))
                    case "PCT012096":
                        county.setAge93yrs_males(int(tableData[1]))
                    case "PCT012097":
                        county.setAge94yrs_males(int(tableData[1]))
                    case "PCT012098":
                        county.setAge95yrs_males(int(tableData[1]))
                    case "PCT012099":
                        county.setAge96yrs_males(int(tableData[1]))
                    case "PCT012100":
                        county.setAge97yrs_males(int(tableData[1]))
                    case "PCT012101":
                        county.setAge98yrs_males(int(tableData[1]))
                    case "PCT012102":
                        county.setAge99yrs_males(int(tableData[1]))
                    case "PCT012103":
                        county.setAge100_104yrs_male(int(tableData[1]))
                    case "PCT012104":
                        county.setAge105_109yrs_male(int(tableData[1]))
                    case "PCT012105":
                        county.setAgeOver110yrs_male(int(tableData[1]))
                    case "PCT012107":
                        county.setAgeUnder1yrs_female(int(tableData[1]))
                    case "PCT012108":
                        county.setAge1yrs_female(int(tableData[1]))
                    case "PCT012109":
                        county.setAge2yrs_female(int(tableData[1]))
                    case "PCT012110":
                        county.setAge3yrs_female(int(tableData[1]))
                    case "PCT012111":
                        county.setAge4yrs_female(int(tableData[1]))
                    case "PCT012112":
                        county.setAge5yrs_female(int(tableData[1]))
                    case "PCT012113":
                        county.setAge6yrs_female(int(tableData[1]))
                    case "PCT012114":
                        county.setAge7yrs_female(int(tableData[1]))
                    case "PCT012115":
                        county.setAge8yrs_female(int(tableData[1]))
                    case "PCT012116":
                        county.setAge9yrs_female(int(tableData[1]))
                    case "PCT012117":
                        county.setAge10yrs_female(int(tableData[1]))
                    case "PCT012118":
                        county.setAge11yrs_female(int(tableData[1]))
                    case "PCT012119":
                        county.setAge12yrs_female(int(tableData[1]))
                    case "PCT012120":
                        county.setAge13yrs_female(int(tableData[1]))
                    case "PCT012121":
                        county.setAge14yrs_female(int(tableData[1]))
                    case "PCT012122":
                        county.setAge15yrs_female(int(tableData[1]))
                    case "PCT012123":
                        county.setAge16yrs_female(int(tableData[1]))
                    case "PCT012124":
                        county.setAge17yrs_female(int(tableData[1]))
                    case "PCT012125":
                        county.setAge18yrs_female(int(tableData[1]))
                    case "PCT012126":
                        county.setAge19yrs_female(int(tableData[1]))
                    case "PCT012127":
                        county.setAge20yrs_female(int(tableData[1]))
                    case "PCT012128":
                        county.setAge21yrs_female(int(tableData[1]))
                    case "PCT012129":
                        county.setAge22yrs_female(int(tableData[1]))
                    case "PCT012130":
                        county.setAge23yrs_female(int(tableData[1]))
                    case "PCT012131":
                        county.setAge24yrs_female(int(tableData[1]))
                    case "PCT012132":
                        county.setAge25yrs_female(int(tableData[1]))
                    case "PCT012133":
                        county.setAge26yrs_female(int(tableData[1]))
                    case "PCT012134":
                        county.setAge27yrs_female(int(tableData[1]))
                    case "PCT012135":
                        county.setAge28yrs_female(int(tableData[1]))
                    case "PCT012136":
                        county.setAge29yrs_female(int(tableData[1]))
                    case "PCT012137":
                        county.setAge30yrs_female(int(tableData[1]))
                    case "PCT012138":
                        county.setAge31yrs_female(int(tableData[1]))
                    case "PCT012139":
                        county.setAge32yrs_female(int(tableData[1]))
                    case "PCT012140":
                        county.setAge33yrs_female(int(tableData[1]))
                    case "PCT012141":
                        county.setAge34yrs_female(int(tableData[1]))
                    case "PCT012142":
                        county.setAge35yrs_female(int(tableData[1]))
                    case "PCT012143":
                        county.setAge36yrs_female(int(tableData[1]))
                    case "PCT012144":
                        county.setAge37yrs_female(int(tableData[1]))
                    case "PCT012145":
                        county.setAge38yrs_female(int(tableData[1]))
                    case "PCT012146":
                        county.setAge39yrs_female(int(tableData[1]))
                    case "PCT012147":
                        county.setAge40yrs_female(int(tableData[1]))
                    case "PCT012148":
                        county.setAge41yrs_female(int(tableData[1]))
                    case "PCT012149":
                        county.setAge42yrs_female(int(tableData[1]))
                    case "PCT012150":
                        county.setAge43yrs_female(int(tableData[1]))
                    case "PCT012151":
                        county.setAge44yrs_female(int(tableData[1]))
                    case "PCT012152":
                        county.setAge45yrs_female(int(tableData[1]))
                    case "PCT012153":
                        county.setAge46yrs_female(int(tableData[1]))
                    case "PCT012154":
                        county.setAge47yrs_female(int(tableData[1]))
                    case "PCT012155":
                        county.setAge48yrs_female(int(tableData[1]))
                    case "PCT012156":
                        county.setAge49yrs_female(int(tableData[1]))
                    case "PCT012157":
                        county.setAge50yrs_female(int(tableData[1]))
                    case "PCT012158":
                        county.setAge51yrs_female(int(tableData[1]))
                    case "PCT012159":
                        county.setAge52yrs_female(int(tableData[1]))
                    case "PCT012160":
                        county.setAge53yrs_female(int(tableData[1]))
                    case "PCT012161":
                        county.setAge54yrs_female(int(tableData[1]))
                    case "PCT012162":
                        county.setAge55yrs_female(int(tableData[1]))
                    case "PCT012163":
                        county.setAge56yrs_female(int(tableData[1]))
                    case "PCT012164":
                        county.setAge57yrs_female(int(tableData[1]))
                    case "PCT012165":
                        county.setAge58yrs_female(int(tableData[1]))
                    case "PCT012166":
                        county.setAge59yrs_female(int(tableData[1]))
                    case "PCT012167":
                        county.setAge60yrs_female(int(tableData[1]))
                    case "PCT012168":
                        county.setAge61yrs_female(int(tableData[1]))
                    case "PCT012169":
                        county.setAge62yrs_female(int(tableData[1]))
                    case "PCT012170":
                        county.setAge63yrs_female(int(tableData[1]))
                    case "PCT012171":
                        county.setAge64yrs_female(int(tableData[1]))
                    case "PCT012172":
                        county.setAge65yrs_female(int(tableData[1]))
                    case "PCT012173":
                        county.setAge66yrs_female(int(tableData[1]))
                    case "PCT012174":
                        county.setAge67yrs_female(int(tableData[1]))
                    case "PCT012175":
                        county.setAge68yrs_female(int(tableData[1]))
                    case "PCT012176":
                        county.setAge69yrs_female(int(tableData[1]))
                    case "PCT012177":
                        county.setAge70yrs_female(int(tableData[1]))
                    case "PCT012178":
                        county.setAge71yrs_female(int(tableData[1]))
                    case "PCT012179":
                        county.setAge72yrs_female(int(tableData[1]))
                    case "PCT012180":
                        county.setAge73yrs_female(int(tableData[1]))
                    case "PCT012181":
                        county.setAge74yrs_female(int(tableData[1]))
                    case "PCT012182":
                        county.setAge75yrs_female(int(tableData[1]))
                    case "PCT012183":
                        county.setAge76yrs_female(int(tableData[1]))
                    case "PCT012184":
                        county.setAge77yrs_female(int(tableData[1]))
                    case "PCT012185":
                        county.setAge78yrs_female(int(tableData[1]))
                    case "PCT012186":
                        county.setAge79yrs_female(int(tableData[1]))
                    case "PCT012187":
                        county.setAge80yrs_female(int(tableData[1]))
                    case "PCT012188":
                        county.setAge81yrs_female(int(tableData[1]))
                    case "PCT012189":
                        county.setAge82yrs_female(int(tableData[1]))
                    case "PCT012190":
                        county.setAge83yrs_female(int(tableData[1]))
                    case "PCT012191":
                        county.setAge84yrs_female(int(tableData[1]))
                    case "PCT012192":
                        county.setAge85yrs_female(int(tableData[1]))
                    case "PCT012193":
                        county.setAge86yrs_female(int(tableData[1]))
                    case "PCT012194":
                        county.setAge87yrs_female(int(tableData[1]))
                    case "PCT012195":
                        county.setAge88yrs_female(int(tableData[1]))
                    case "PCT012196":
                        county.setAge89yrs_female(int(tableData[1]))
                    case "PCT012197":
                        county.setAge90yrs_female(int(tableData[1]))
                    case "PCT012198":
                        county.setAge91yrs_female(int(tableData[1]))
                    case "PCT012199":
                        county.setAge92yrs_female(int(tableData[1]))
                    case "PCT012200":
                        county.setAge93yrs_female(int(tableData[1]))
                    case "PCT012201":
                        county.setAge94yrs_female(int(tableData[1]))
                    case "PCT012202":
                        county.setAge95yrs_female(int(tableData[1]))
                    case "PCT012203":
                        county.setAge96yrs_female(int(tableData[1]))
                    case "PCT012204":
                        county.setAge97yrs_female(int(tableData[1]))
                    case "PCT012205":
                        county.setAge98yrs_female(int(tableData[1]))
                    case "PCT012206":
                        county.setAge99yrs_female(int(tableData[1]))
                    case "PCT012207":
                        county.setAge100_104yrs_female(int(tableData[1]))
                    case "PCT012208":
                        county.setAge105_109yrs_female(int(tableData[1]))
                    case "PCT012209":
                        county.setAgeOver110yrs_female(int(tableData[1]))
                break  # Location Match Found, no need to search other county objs
    print("  >> Allocated Data to table <" + tableName + ">...")

tables = compile_EmployIncome_Tables()  # We separated these calls because they utilize diff. API urls/variables
print("[x] Compiling \"Employment & Income\" Tables...")
print("[ ] Running Data Allocation...")
for table in tables:
    # Call 1 Table at a time
    base_url = "https://api.census.gov/data/2010/acs/acs5"
    var = "?get=NAME," + table + "&for=county:*"
    package = base_url + var + "&key=" + API_Key
    request = requests.get(package).json()
    tableName = request.pop(0)[1]  # Get what type of data we're dealing w/ (employed, unemployed, etc.)
    for tableData in request:
        for county in countyObjs:
            location = tableData[0]

            # New table data location == created county obj location -> Add this new data to it
            if location == county.getCensusName():
                match tableName:
                    case "C24010_001E":
                        county.setEmployed(int(tableData[1]))
                    case "B23001_008E":
                        county.setUnemployed_16to19_males(int(tableData[1]))
                    case "B23001_015E":
                        county.setUnemployed_20to21_males(int(tableData[1]))
                    case "B23001_022E":
                        county.setUnemployed_22to24_males(int(tableData[1]))
                    case "B23001_029E":
                        county.setUnemployed_25to29_males(int(tableData[1]))
                    case "B23001_036E":
                        county.setUnemployed_30to34_males(int(tableData[1]))
                    case "B23001_043E":
                        county.setUnemployed_35to44_males(int(tableData[1]))
                    case "B23001_050E":
                        county.setUnemployed_45to54_males(int(tableData[1]))
                    case "B23001_057E":
                        county.setUnemployed_55to59_males(int(tableData[1]))
                    case "B23001_064E":
                        county.setUnemployed_60to61_males(int(tableData[1]))
                    case "B23001_071E":
                        county.setUnemployed_62to64_males(int(tableData[1]))
                    case "B23001_076E":
                        county.setUnemployed_65to69_males(int(tableData[1]))
                    case "B23001_081E":
                        county.setUnemployed_70to74_males(int(tableData[1]))
                    case "B23001_086E":
                        county.setUnemployed_75over_males(int(tableData[1]))
                    case "B23001_094E":
                        county.setUnemployed_16to19_females(int(tableData[1]))
                    case "B23001_101E":
                        county.setUnemployed_20to21_females(int(tableData[1]))
                    case "B23001_108E":
                        county.setUnemployed_22to24_females(int(tableData[1]))
                    case "B23001_115E":
                        county.setUnemployed_25to29_females(int(tableData[1]))
                    case "B23001_122E":
                        county.setUnemployed_30to34_females(int(tableData[1]))
                    case "B23001_129E":
                        county.setUnemployed_35to44_females(int(tableData[1]))
                    case "B23001_136E":
                        county.setUnemployed_45to54_females(int(tableData[1]))
                    case "B23001_143E":
                        county.setUnemployed_55to59_females(int(tableData[1]))
                    case "B23001_150E":
                        county.setUnemployed_60to61_females(int(tableData[1]))
                    case "B23001_157E":
                        county.setUnemployed_62to64_females(int(tableData[1]))
                    case "B23001_162E":
                        county.setUnemployed_65to69_females(int(tableData[1]))
                    case "B23001_167E":
                        county.setUnemployed_70to74_females(int(tableData[1]))
                    case "B23001_172E":
                        county.setUnemployed_75over_females(int(tableData[1]))
                    case "B23001_009E":
                        county.setNotinlaborforce_16to19_males(int(tableData[1]))
                    case "B23001_016E":
                        county.setNotinlaborforce_20to21_males(int(tableData[1]))
                    case "B23001_023E":
                        county.setNotinlaborforce_22to24_males(int(tableData[1]))
                    case "B23001_030E":
                        county.setNotinlaborforce_25to29_males(int(tableData[1]))
                    case "B23001_037E":
                        county.setNotinlaborforce_30to34_males(int(tableData[1]))
                    case "B23001_044E":
                        county.setNotinlaborforce_35to44_males(int(tableData[1]))
                    case "B23001_051E":
                        county.setNotinlaborforce_45to54_males(int(tableData[1]))
                    case "B23001_058E":
                        county.setNotinlaborforce_55to59_males(int(tableData[1]))
                    case "B23001_065E":
                        county.setNotinlaborforce_60to61_males(int(tableData[1]))
                    case "B23001_072E":
                        county.setNotinlaborforce_62to64_males(int(tableData[1]))
                    case "B23001_077E":
                        county.setNotinlaborforce_65to69_males(int(tableData[1]))
                    case "B23001_082E":
                        county.setNotinlaborforce_70to74_males(int(tableData[1]))
                    case "B23001_087E":
                        county.setNotinlaborforce_75over_males(int(tableData[1]))
                    case "B23001_095E":
                        county.setNotinlaborforce_16to19_females(int(tableData[1]))
                    case "B23001_102E":
                        county.setNotinlaborforce_20to21_females(int(tableData[1]))
                    case "B23001_109E":
                        county.setNotinlaborforce_22to24_females(int(tableData[1]))
                    case "B23001_116E":
                        county.setNotinlaborforce_25to29_females(int(tableData[1]))
                    case "B23001_123E":
                        county.setNotinlaborforce_30to34_females(int(tableData[1]))
                    case "B23001_130E":
                        county.setNotinlaborforce_35to44_females(int(tableData[1]))
                    case "B23001_137E":
                        county.setNotinlaborforce_45to54_females(int(tableData[1]))
                    case "B23001_144E":
                        county.setNotinlaborforce_55to59_females(int(tableData[1]))
                    case "B23001_151E":
                        county.setNotinlaborforce_60to61_females(int(tableData[1]))
                    case "B23001_158E":
                        county.setNotinlaborforce_62to64_females(int(tableData[1]))
                    case "B23001_163E":
                        county.setNotinlaborforce_65to69_females(int(tableData[1]))
                    case "B23001_168E":
                        county.setNotinlaborforce_70to74_females(int(tableData[1]))
                    case "B23001_173E":
                        county.setNotinlaborforce_75over_females(int(tableData[1]))
                    case "B19001_002E":
                        county.setIncome_less_than_10k(int(tableData[1]))
                    case "B19001_003E":
                        county.setIncome_10kto14k(int(tableData[1]))
                    case "B19001_004E":
                        county.setIncome_15kto19k(int(tableData[1]))
                    case "B19001_005E":
                        county.setIncome_20kto24k(int(tableData[1]))
                    case "B19001_006E":
                        county.setIncome_25kto29k(int(tableData[1]))
                    case "B19001_007E":
                        county.setIncome_30kto34k(int(tableData[1]))
                    case "B19001_008E":
                        county.setIncome_35kto39k(int(tableData[1]))
                    case "B19001_009E":
                        county.setIncome_40kto44k(int(tableData[1]))
                    case "B19001_010E":
                        county.setIncome_45kto49k(int(tableData[1]))
                    case "B19001_011E":
                        county.setIncome_50kto59k(int(tableData[1]))
                    case "B19001_012E":
                        county.setIncome_60kto74k(int(tableData[1]))
                    case "B19001_013E":
                        county.setIncome_75kto99k(int(tableData[1]))
                    case "B19001_014E":
                        county.setIncome_100kto124k(int(tableData[1]))
                    case "B19001_015E":
                        county.setIncome_125kto149k(int(tableData[1]))
                    case "B19001_016E":
                        county.setIncome_150kto199k(int(tableData[1]))
                    case "B19001_017E":
                        county.setIncome_200kover(int(tableData[1]))
                break  # Location Match Found, no need to search other county objs
    print("  >> Allocated Data to table <" + tableName + ">...")

# Print JSON
# printRequest(countyObjs)  # Prints output to console
writeToDatabase(countyObjs)  # Writes output to Database
print("Program Finished Successfully.")
