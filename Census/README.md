# Data on "Yearly Summary Files"
All files and APIs (unless specified) were found from: [https://api.census.gov/data.html](https://api.census.gov/data.html)

* *Census_API_Calls is the Updated version of "Census API Calls".*


### 2000 Decennial SF1
* Ex: [https://api.census.gov/data/2000/dec/sf1/examples.html](https://api.census.gov/data/2000/dec/sf1/examples.html)
* Var:
  [https://api.census.gov/data/2000/dec/sf1/examples.html](https://api.census.gov/data/2000/dec/sf1/variables.html)

| Year |             Data Pulled              |  Table   | Comments |
|:----:|:------------------------------------:|:--------:|:--------:|
| 2000 |             white alone              | P003003  |          |
| 2000 |             black alone              | P003004  |          |
| 2000 |             indian alone             | P003005  |          |
| 2000 |             asian alone              | P003006  |          |
| 2000 |            hawaiian alone            | P003007  |          |
| 2000 |           other race alone           | P003008  |          |
| 2000 |          two or more races           | P003009  |          |
| 2000 |          hispanic or latino          | P004002  |          |
| 2000 | white alone (not hispanic or latino) | P008003  |          |



| Year |       Data Pulled        |   Table   |                    Comments                    |
|:----:|:------------------------:|:---------:|:----------------------------------------------:|
| 2000 |       Total Males        |  P012002  |                                                |
| 2000 |      Total Females       |  P012026  |                                                |
|      |                          |           |                                                |
| 2000 |    males under 1 year    | PCT012003 | Just add males + females to get each age group |
| 2000 |         ~ 1 year         | PCT012004 |                                                |
| 2000 |         ~ 2 year         | PCT012005 |                                                |
| 2000 |         ~ 3 year         | PCT012006 |                                                |
| 2000 |         ~ 4 year         | PCT012007 |                                                |
| 2000 |         ~ 5 year         | PCT012008 |                                                |
| 2000 |         ~ 6 year         | PCT012009 |                                                |
| 2000 |         ~ 7 year         | PCT012010 |                                                |
| 2000 |         ~ 8 year         | PCT012011 |                                                |
| 2000 |         ~ 9 year         | PCT012012 |                                                |
| 2000 |        ~ 10 year         | PCT012013 |                                                |
|      |          ~ etc.          |           |                                                |
| 2000 |        ~ 99 years        | PCT012102 |                                                |
| 2000 |    ~ 100 to 104 years    | PCT012103 |                                                |
| 2000 |    ~ 105 to 109 years    | PCT012104 |                                                |
| 2000 |   ~ 110 years and over   | PCT012105 |                                                |
|      |                          |           |                                                |
| 2000 |   females under 1 year   | PCT012107 | Just add males + females to get each age group |
| 2000 |         ~ 1 year         | PCT012108 |                                                |
| 2000 |         ~ 2 year         | PCT012109 |                                                |
| 2000 |         ~ 3 year         | PCT012110 |                                                |
| 2000 |         ~ 4 year         | PCT012111 |                                                |
| 2000 |         ~ 5 year         | PCT012112 |                                                |
| 2000 |         ~ 6 year         | PCT012113 |                                                |
| 2000 |         ~ 7 year         | PCT012114 |                                                |
| 2000 |         ~ 8 year         | PCT012115 |                                                |
| 2000 |         ~ 9 year         | PCT012116 |                                                |
| 2000 |        ~ 10 year         | PCT012117 |                                                |
|      |          ~ etc.          |           |                                                |
| 2000 |        ~ 99 years        | PCT012206 |                                                |
| 2000 |    ~ 100 to 104 years    | PCT012207 |                                                |
| 2000 | ~ 105 years to 109 years | PCT012208 |                                                |
| 2000 |   ~ 110 years and over   | PCT012209 |                                                |

---
### 2000 Congressional District SF
* Ex: [https://api.census.gov/data/2000/dec/cd110s/examples.html](https://api.census.gov/data/2000/dec/cd110s/examples.html)
* Var: [https://api.census.gov/data/2000/dec/cd110s/variables.html](https://api.census.gov/data/2000/dec/cd110s/variables.html)
* Congressional Districts: [https://api.census.gov/data/2000/dec/cd110s?get=H015001,NAME&for=congressional%20district:*](https://api.census.gov/data/2000/dec/cd110s?get=H015001,NAME&for=congressional%20district:*)

***--> Congressional Districts pulled from "Ex" (link above). Used to fill out API JSON request.***

| Year |      Data Pulled      |       Table       | Comments                                                                 |
|:-----|:---------------------:|:-----------------:|:-------------------------------------------------------------------------|
| 2000 | Population 16 & Over  |     (NEW) N/A     | Add "Under 6 yrs" + "6-18 yrs" = children population                     |
| 2000 | Population 16 & Over  | (NEW) *See Above* | Population 16 & Over = (Males + Females) - childPop + Get age "16-18yrs" |
| 2000 | Population 16 & Over  |       (NEW)       | Divide each Employment Category w/ "Population 16 & Over" NOT Total Pop! |
|      |                       |                   |                                                                          |
| 2000 |       Employed        |      P050001      |                                                                          |
| 2000 |      Unemployed       |      P043007      | Males only                                                               |
| 2000 |      Unemployed       |      P043014      | Females only                                                             |
|      |                       |                   |                                                                          |
| 2000 |  Not in Labor Force   |      P043008      | Males only                                                               |
| 2000 |  Not in Labor Force   |      P043015      | Females only                                                             |


| Year |     Data Pulled      |  Table  | Comments         |
|:-----|:--------------------:|:-------:|:-----------------|
| 2000 |      Households      | P055001 | Total Households |
|      |                      |         |                  |
| 2000 |        Income        |         |                  |
| 2000 |  Less than $10,000   | P052002 |                  |
| 2000 |  $10,000 to $14,999  | P052003 |                  |
| 2000 |  $15,000 to $19,999  | P052004 |                  |
| 2000 |  $20,000 to $24,999  | P052005 |                  |
| 2000 |  $25,000 to $29,999  | P052006 |                  |
| 2000 |  $30,000 to $34,999  | P052007 |                  |
| 2000 |  $35,000 to $39,999  | P052008 |                  |
| 2000 |  $40,000 to $44,999  | P052009 |                  |
| 2000 |  $45,000 to $49,999  | P052010 |                  |
| 2000 |  $50,000 to $59,999  | P052011 |                  |
| 2000 |  $60,000 to $74,999  | P052012 |                  |
| 2000 |  $75,000 to $99,999  | P052013 |                  |
| 2000 | $100,000 to $124,999 | P052014 |                  |
| 2000 | $125,000 to $149,999 | P052015 |                  |
| 2000 | $150,000 to $199,999 | P052016 |                  |
| 2000 |   $200,000 or more   | P052017 |                  |


---
### 2010 Decennial SF1
* Ex: [https://api.census.gov/data/2010/dec/sf1/examples.html](https://api.census.gov/data/2010/dec/sf1/examples.html)
* Var: [https://api.census.gov/data/2010/dec/sf1/variables.html](https://api.census.gov/data/2010/dec/sf1/variables.html)

* Ex (NEW): [https://api.census.gov/data/2010/acs/acs5/examples.html](https://api.census.gov/data/2010/acs/acs5/examples.html)
* Var (NEW): [https://api.census.gov/data/2010/acs/acs5/variables.html](https://api.census.gov/data/2010/acs/acs5/variables.html)

| Year |         Data Pulled         |  Table  | Comments                            |
|:-----|:---------------------------:|:-------:|:------------------------------------|
| 2010 |         white alone         | P003002 | (NEW) B01001A_001E                  |
| 2010 |         black alone         | P003003 | (NEW) B01001B_001E                  |
| 2010 |        indian alone         | P003004 | (NEW) B01001C_001E                  |
| 2010 |         asian alone         | P003005 | (NEW) B01001D_001E                  |
| 2010 |       hawaiian alone        | P003006 | (NEW) B01001E_001E                  |
| 2010 |      other race alone       | P003007 | (NEW) B01001F_001E                  |
| 2010 |      two or more races      | P003008 | (NEW) B01001G_001E                  |
| 2010 |     hispanic or latino      | P009002 | **(NEW) B01001I_001E, order flipped |
| 2010 | white alone (not hispanic)  | P005003 | **(NEW) B01001H_001E                |

| Year |       Data Pulled        |   Table   |                    Comments                     |
|:----:|:------------------------:|:---------:|:-----------------------------------------------:|
| 2010 |       Total Males        | PCT012002 |                                                 |
| 2010 |      Total Females       | PCT012106 |                                                 |
| 2010 |    males under 1 year    | PCT012003 | Just add males + females to get each age group  |
| 2010 |         ~ 1 year         | PCT012004 |                                                 |
| 2010 |         ~ 2 year         | PCT012005 |                                                 |
| 2010 |         ~ 3 year         | PCT012006 |                                                 |
| 2010 |         ~ 4 year         | PCT012007 |                                                 |
| 2010 |         ~ 5 year         | PCT012008 |                                                 |
| 2010 |         ~ 6 year         | PCT012009 |                                                 |
| 2010 |         ~ 7 year         | PCT012010 |                                                 |
| 2010 |         ~ 8 year         | PCT012011 |                                                 |
| 2010 |         ~ 9 year         | PCT012012 |                                                 |
| 2010 |        ~ 10 year         | PCT012013 |                                                 |
|      |          ~ etc.          |           |                                                 |
| 2010 |        ~ 99 years        | PCT012102 |                                                 |
| 2010 |    ~ 100 to 104 years    | PCT012103 |                                                 |
| 2010 |    ~ 105 to 109 years    | PCT012104 |                                                 |
| 2010 |   ~ 110 years and over   | PCT012105 |                                                 |
| 2010 |   females under 1 year   | PCT012107 | Just add males + females to get each age group  |
| 2010 |         ~ 1 year         | PCT012108 |                                                 |
| 2010 |         ~ 2 year         | PCT012109 |                                                 |
| 2010 |         ~ 3 year         | PCT012110 |                                                 |
| 2010 |         ~ 4 year         | PCT012111 |                                                 |
| 2010 |         ~ 5 year         | PCT012112 |                                                 |
| 2010 |         ~ 6 year         | PCT012113 |                                                 |
| 2010 |         ~ 7 year         | PCT012114 |                                                 |
| 2010 |         ~ 8 year         | PCT012115 |                                                 |
| 2010 |         ~ 9 year         | PCT012116 |                                                 |
| 2010 |        ~ 10 year         | PCT012117 |                                                 |
|      |          ~ etc.          |           |                                                 |
| 2010 |        ~ 99 years        | PCT012206 |                                                 |
| 2010 |    ~ 100 to 104 years    | PCT012207 |                                                 |
| 2010 | ~ 105 years to 109 years | PCT012208 |                                                 |
| 2010 |   ~ 110 years and over   | PCT012209 |                                                 |


---
### 2010 ACS 5-Year Detailed Tables
* Ex: [https://api.census.gov/data/2010/acs/acs5/examples.html](https://api.census.gov/data/2010/acs/acs5/examples.html)
* Var: [https://api.census.gov/data/2010/acs/acs5/variables.html](https://api.census.gov/data/2010/acs/acs5/variables.html)

| Year |     Data Pulled      |       Table       | Comments                                                                 |
|:-----|:--------------------:|:-----------------:|:-------------------------------------------------------------------------|
| 2010 | Population 16 & Over |     (NEW) N/A     | Add "Under 6 yrs" + "6-18 yrs" = children population                     |
| 2010 | Population 16 & Over | (NEW) *See Above* | Population 16 & Over = (Males + Females) - childPop + Get age "16-18yrs" |
| 2010 | Population 16 & Over |       (NEW)       | Divide each Employment Category w/ "Population 16 & Over" NOT Total Pop! |
|      |                      |                   |                                                                          |
| 2010 |       Employed       |    C24010_001E    |                                                                          |
| 2010 |                      |                   |                                                                          |
| 2010 |      Unemployed      |                   | Males                                                                    |
| 2010 |      Unemployed      |    B23001_008E    | 16-19 Males                                                              |
| 2010 |      Unemployed      |    B23001_015E    | 20-21 Males                                                              |
| 2010 |      Unemployed      |    B23001_022E    | 22-24 Males                                                              |
| 2010 |      Unemployed      |    B23001_029E    | 25-29 Males                                                              |
| 2010 |      Unemployed      |    B23001_036E    | 30-34 Males                                                              |
| 2010 |      Unemployed      |    B23001_043E    | 35-44 Males                                                              |
| 2010 |      Unemployed      |    B23001_050E    | 45-54 Males                                                              |
| 2010 |      Unemployed      |    B23001_057E    | 55-59 Males                                                              |
| 2010 |      Unemployed      |    B23001_064E    | 60-61 Males                                                              |
| 2010 |      Unemployed      |    B23001_071E    | 62-64 Males                                                              |
| 2010 |      Unemployed      |    B23001_076E    | 65-69 Males                                                              |
| 2010 |      Unemployed      |    B23001_081E    | 70-74 Males                                                              |
| 2010 |      Unemployed      |    B23001_086E    | 75+ Males                                                                |
| 2010 |      Unemployed      |                   | Females                                                                  |
| 2010 |      Unemployed      |    B23001_094E    | 16-19 Females                                                            |
| 2010 |      Unemployed      |    B23001_101E    | 20-21 Females                                                            |
| 2010 |      Unemployed      |    B23001_108E    | 22-24 Females                                                            |
| 2010 |      Unemployed      |    B23001_115E    | 25-29 Females                                                            |
| 2010 |      Unemployed      |    B23001_122E    | 30-34 Females                                                            |
| 2010 |      Unemployed      |    B23001_129E    | 35-44 Females                                                            |
| 2010 |      Unemployed      |    B23001_136E    | 45-54 Females                                                            |
| 2010 |      Unemployed      |    B23001_143E    | 55-59 Females                                                            |
| 2010 |      Unemployed      |    B23001_150E    | 60-61 Females                                                            |
| 2010 |      Unemployed      |    B23001_157E    | 62-64 Females                                                            |
| 2010 |      Unemployed      |    B23001_162E    | 65-69 Females                                                            |
| 2010 |      Unemployed      |    B23001_167E    | 70-74 Females                                                            |
| 2010 |      Unemployed      |    B23001_172E    | 75+ Females                                                              |
| 2010 |                      |                   |                                                                          |
| 2010 |  Not in Labor Force  |                   | Males                                                                    |
| 2010 |  Not in Labor Force  |    B23001_009E    | 16-19 Males                                                              |
| 2010 |  Not in Labor Force  |    B23001_016E    | 20-21 Males                                                              |
| 2010 |  Not in Labor Force  |    B23001_023E    | 22-24 Males                                                              |
| 2010 |  Not in Labor Force  |    B23001_030E    | 25-29 Males                                                              |
| 2010 |  Not in Labor Force  |    B23001_037E    | 30-34 Males                                                              |
| 2010 |  Not in Labor Force  |    B23001_044E    | 35-44 Males                                                              |
| 2010 |  Not in Labor Force  |    B23001_051E    | 45-54 Males                                                              |
| 2010 |  Not in Labor Force  |    B23001_058E    | 55-59 Males                                                              |
| 2010 |  Not in Labor Force  |    B23001_065E    | 60-61 Males                                                              |
| 2010 |  Not in Labor Force  |    B23001_072E    | 62-64 Males                                                              |
| 2010 |  Not in Labor Force  |    B23001_077E    | 65-69 Males                                                              |
| 2010 |  Not in Labor Force  |    B23001_082E    | 70-74 Males                                                              |
| 2010 |  Not in Labor Force  |    B23001_087E    | 75+ Males                                                                |
| 2010 |  Not in Labor Force  |                   | Females                                                                  |
| 2010 |  Not in Labor Force  |    B23001_095E    | 16-19 Females                                                            |
| 2010 |  Not in Labor Force  |    B23001_102E    | 20-21 Females                                                            |
| 2010 |  Not in Labor Force  |    B23001_109E    | 22-24 Females                                                            |
| 2010 |  Not in Labor Force  |    B23001_116E    | 25-29 Females                                                            |
| 2010 |  Not in Labor Force  |    B23001_123E    | 30-34 Females                                                            |
| 2010 |  Not in Labor Force  |    B23001_130E    | 35-44 Females                                                            |
| 2010 |  Not in Labor Force  |    B23001_137E    | 45-54 Females                                                            |
| 2010 |  Not in Labor Force  |    B23001_144E    | 55-59 Females                                                            |
| 2010 |  Not in Labor Force  |    B23001_151E    | 60-61 Females                                                            |
| 2010 |  Not in Labor Force  |    B23001_158E    | 62-64 Females                                                            |
| 2010 |  Not in Labor Force  |    B23001_163E    | 65-69 Females                                                            |
| 2010 |  Not in Labor Force  |    B23001_168E    | 70-74 Females                                                            |
| 2010 |  Not in Labor Force  |    B23001_173E    | 75+ Females                                                              |


***=> NOTE: Individual income values diff by A LOT comp. to 2020 Census. 
Couldn't find alt. tables. Investigate!***

| Year | Data Pulled |    Table    | Comments          |
|:-----|:-----------:|:-----------:|:------------------|
| 2010 |   Income    | B19001_001E | Total Households  |
|      |             |             |                   |
| 2010 |   Income    | B19001_002E | Less than $10,000 |
| 2010 |   Income    | B19001_003E | $10,000-$14,999   |
| 2010 |   Income    | B19001_004E | $15,000-$19,999   |
| 2010 |   Income    | B19001_005E | $20,000-$24,999   |
| 2010 |   Income    | B19001_006E | $25,000-$29,999   |
| 2010 |   Income    | B19001_007E | $30,000-$34,999   |
| 2010 |   Income    | B19001_008E | $35,000-$39,999   |
| 2010 |   Income    | B19001_009E | $40,000-$44,999   |
| 2010 |   Income    | B19001_010E | $45,999-$49,999   |
| 2010 |   Income    | B19001_011E | $50,000-$59,999   |
| 2010 |   Income    | B19001_012E | $60,000-$74,999   |
| 2010 |   Income    | B19001_013E | $75,000-$99,999   |
| 2010 |   Income    | B19001_014E | $100,000-$124,999 |
| 2010 |   Income    | B19001_015E | $125,000-$149,999 |
| 2010 |   Income    | B19001_016E | $150,000-$199,999 |
| 2010 |   Income    | B19001_017E | $200,000+         |


---
### 2020 Census Database
The 2020 Census Database is copy-pasted from our previous working models. It's not recreated.


---
### 2010 & 2020 Insurance Estimates?? (Check to see if there's another true-value database to compare figures)
https://www.census.gov/data/developers/data-sets/Health-Insurance-Statistics.html

| Year | Data Pulled | Table  | Comments |
|:-----|:-----------:|:------:|:---------|
| 2010 |   Insured   | NIC_PT |          |
| 2010 |  Uninsured  | NUI_PT |          |


***Kalawao County, Hawaii is the only dataset w/ "N/A" insured and uninsured values, given by the Census Bureau.***


