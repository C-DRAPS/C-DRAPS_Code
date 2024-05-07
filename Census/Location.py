class Location:
    def __init__(self, censusName):
        self.censusname = censusName
        self.county = censusName.split(", ")[0]
        self.state = censusName.split(", ")[1]
        self.totalMales = -1
        self.totalFemales = -1
        self.whiteAlone = -1
        self.blackAlone = -1
        self.indianAlone = -1
        self.asianAlone = -1
        self.hawaiianAlone = -1
        self.otherRaceAlone = -1
        self.twoOrMoreRaces = -1
        self.hispanicOrLatino = -1
        self.whiteAlone_NotHisp = -1

        self.ageUnder1yr_males = -1
        self.age1yrs_male = -1
        self.age2yrs_male = -1
        self.age3yrs_male = -1
        self.age4yrs_male = -1
        self.age5yrs_male = -1
        self.age6yrs_male = -1
        self.age7yrs_male = -1
        self.age8yrs_male = -1
        self.age9yrs_male = -1
        self.age10yrs_male = -1
        self.age11yrs_male = -1
        self.age12yrs_male = -1
        self.age13yrs_male = -1
        self.age14yrs_male = -1
        self.age15yrs_male = -1
        self.age16yrs_male = -1
        self.age17yrs_male = -1
        self.age18yrs_male = -1
        self.age19yrs_male = -1
        self.age20yrs_male = -1
        self.age21yrs_male = -1
        self.age22yrs_male = -1
        self.age23yrs_male = -1
        self.age24yrs_male = -1
        self.age25yrs_male = -1
        self.age26yrs_male = -1
        self.age27yrs_male = -1
        self.age28yrs_male = -1
        self.age29yrs_male = -1
        self.age30yrs_male = -1
        self.age31yrs_male = -1
        self.age32yrs_male = -1
        self.age33yrs_male = -1
        self.age34yrs_male = -1
        self.age35yrs_male = -1
        self.age36yrs_male = -1
        self.age37yrs_male = -1
        self.age38yrs_male = -1
        self.age39yrs_male = -1
        self.age40yrs_male = -1
        self.age41yrs_male = -1
        self.age42yrs_male = -1
        self.age43yrs_male = -1
        self.age44yrs_male = -1
        self.age45yrs_male = -1
        self.age46yrs_male = -1
        self.age47yrs_male = -1
        self.age48yrs_male = -1
        self.age49yrs_male = -1
        self.age50yrs_male = -1
        self.age51yrs_male = -1
        self.age52yrs_male = -1
        self.age53yrs_male = -1
        self.age54yrs_male = -1
        self.age55yrs_male = -1
        self.age56yrs_male = -1
        self.age57yrs_male = -1
        self.age58yrs_male = -1
        self.age59yrs_male = -1
        self.age60yrs_male = -1
        self.age61yrs_male = -1
        self.age62yrs_male = -1
        self.age63yrs_male = -1
        self.age64yrs_male = -1
        self.age65yrs_male = -1
        self.age66yrs_male = -1
        self.age67yrs_male = -1
        self.age68yrs_male = -1
        self.age69yrs_male = -1
        self.age70yrs_male = -1
        self.age71yrs_male = -1
        self.age72yrs_male = -1
        self.age73yrs_male = -1
        self.age74yrs_male = -1
        self.age75yrs_male = -1
        self.age76yrs_male = -1
        self.age77yrs_male = -1
        self.age78yrs_male = -1
        self.age79yrs_male = -1
        self.age80yrs_male = -1
        self.age81yrs_male = -1
        self.age82yrs_male = -1
        self.age83yrs_male = -1
        self.age84yrs_male = -1
        self.age85yrs_male = -1
        self.age86yrs_male = -1
        self.age87yrs_male = -1
        self.age88yrs_male = -1
        self.age89yrs_male = -1
        self.age90yrs_male = -1
        self.age91yrs_male = -1
        self.age92yrs_male = -1
        self.age93yrs_male = -1
        self.age94yrs_male = -1
        self.age95yrs_male = -1
        self.age96yrs_male = -1
        self.age97yrs_male = -1
        self.age98yrs_male = -1
        self.age99yrs_male = -1
        self.age100_104yrs_male = -1
        self.age105_108yrs_male = -1
        self.ageOver110yrs_male = -1

        self.ageUnder1yr_female = -1
        self.age1yrs_female = -1
        self.age2yrs_female = -1
        self.age3yrs_female = -1
        self.age4yrs_female = -1
        self.age5yrs_female = -1
        self.age6yrs_female = -1
        self.age7yrs_female = -1
        self.age8yrs_female = -1
        self.age9yrs_female = -1
        self.age10yrs_female = -1
        self.age11yrs_female = -1
        self.age12yrs_female = -1
        self.age13yrs_female = -1
        self.age14yrs_female = -1
        self.age15yrs_female = -1
        self.age16yrs_female = -1
        self.age17yrs_female = -1
        self.age18yrs_female = -1
        self.age19yrs_female = -1
        self.age20yrs_female = -1
        self.age21yrs_female = -1
        self.age22yrs_female = -1
        self.age23yrs_female = -1
        self.age24yrs_female = -1
        self.age25yrs_female = -1
        self.age26yrs_female = -1
        self.age27yrs_female = -1
        self.age28yrs_female = -1
        self.age29yrs_female = -1
        self.age30yrs_female = -1
        self.age31yrs_female = -1
        self.age32yrs_female = -1
        self.age33yrs_female = -1
        self.age34yrs_female = -1
        self.age35yrs_female = -1
        self.age36yrs_female = -1
        self.age37yrs_female = -1
        self.age38yrs_female = -1
        self.age39yrs_female = -1
        self.age40yrs_female = -1
        self.age41yrs_female = -1
        self.age42yrs_female = -1
        self.age43yrs_female = -1
        self.age44yrs_female = -1
        self.age45yrs_female = -1
        self.age46yrs_female = -1
        self.age47yrs_female = -1
        self.age48yrs_female = -1
        self.age49yrs_female = -1
        self.age50yrs_female = -1
        self.age51yrs_female = -1
        self.age52yrs_female = -1
        self.age53yrs_female = -1
        self.age54yrs_female = -1
        self.age55yrs_female = -1
        self.age56yrs_female = -1
        self.age57yrs_female = -1
        self.age58yrs_female = -1
        self.age59yrs_female = -1
        self.age60yrs_female = -1
        self.age61yrs_female = -1
        self.age62yrs_female = -1
        self.age63yrs_female = -1
        self.age64yrs_female = -1
        self.age65yrs_female = -1
        self.age66yrs_female = -1
        self.age67yrs_female = -1
        self.age68yrs_female = -1
        self.age69yrs_female = -1
        self.age70yrs_female = -1
        self.age71yrs_female = -1
        self.age72yrs_female = -1
        self.age73yrs_female = -1
        self.age74yrs_female = -1
        self.age75yrs_female = -1
        self.age76yrs_female = -1
        self.age77yrs_female = -1
        self.age78yrs_female = -1
        self.age79yrs_female = -1
        self.age80yrs_female = -1
        self.age81yrs_female = -1
        self.age82yrs_female = -1
        self.age83yrs_female = -1
        self.age84yrs_female = -1
        self.age85yrs_female = -1
        self.age86yrs_female = -1
        self.age87yrs_female = -1
        self.age88yrs_female = -1
        self.age89yrs_female = -1
        self.age90yrs_female = -1
        self.age91yrs_female = -1
        self.age92yrs_female = -1
        self.age93yrs_female = -1
        self.age94yrs_female = -1
        self.age95yrs_female = -1
        self.age96yrs_female = -1
        self.age97yrs_female = -1
        self.age98yrs_female = -1
        self.age99yrs_female = -1
        self.age100_104yrs_female = -1
        self.age105_108yrs_female = -1
        self.ageOver110yrs_female = -1

        self.employed = -1

        self.unemployed_16to19_Males = -1
        self.unemployed_20to21_Males = -1
        self.unemployed_22to24_Males = -1
        self.unemployed_25to29_Males = -1
        self.unemployed_30to34_Males = -1
        self.unemployed_35to44_Males = -1
        self.unemployed_45to54_Males = -1
        self.unemployed_55to59_Males = -1
        self.unemployed_60to61_Males = -1
        self.unemployed_62to64_Males = -1
        self.unemployed_65to69_Males = -1
        self.unemployed_70to74_Males = -1
        self.unemployed_75Over_Males = -1
        self.unemployed_16to19_Females = -1
        self.unemployed_20to21_Females = -1
        self.unemployed_22to24_Females = -1
        self.unemployed_25to29_Females = -1
        self.unemployed_30to34_Females = -1
        self.unemployed_35to44_Females = -1
        self.unemployed_45to54_Females = -1
        self.unemployed_55to59_Females = -1
        self.unemployed_60to61_Females = -1
        self.unemployed_62to64_Females = -1
        self.unemployed_65to69_Females = -1
        self.unemployed_70to74_Females = -1
        self.unemployed_75Over_Females = -1

        self.notInLaborForce_16to19_Males = -1
        self.notInLaborForce_20to21_Males = -1
        self.notInLaborForce_22to24_Males = -1
        self.notInLaborForce_25to29_Males = -1
        self.notInLaborForce_30to34_Males = -1
        self.notInLaborForce_35to44_Males = -1
        self.notInLaborForce_45to54_Males = -1
        self.notInLaborForce_55to59_Males = -1
        self.notInLaborForce_60to61_Males = -1
        self.notInLaborForce_62to64_Males = -1
        self.notInLaborForce_65to69_Males = -1
        self.notInLaborForce_70to74_Males = -1
        self.notInLaborForce_75Over_Males = -1
        self.notInLaborForce_16to19_Females = -1
        self.notInLaborForce_20to21_Females = -1
        self.notInLaborForce_22to24_Females = -1
        self.notInLaborForce_25to29_Females = -1
        self.notInLaborForce_30to34_Females = -1
        self.notInLaborForce_35to44_Females = -1
        self.notInLaborForce_45to54_Females = -1
        self.notInLaborForce_55to59_Females = -1
        self.notInLaborForce_60to61_Females = -1
        self.notInLaborForce_62to64_Females = -1
        self.notInLaborForce_65to69_Females = -1
        self.notInLaborForce_70to74_Females = -1
        self.notInLaborForce_75Over_Females = -1

        self.income_Less_than_10K = -1
        self.income_10Kto14K = -1
        self.income_15Kto19K = -1
        self.income_20Kto24K = -1
        self.income_25Kto29K = -1
        self.income_30Kto34K = -1
        self.income_35Kto39K = -1
        self.income_40Kto44K = -1
        self.income_45Kto49K = -1
        self.income_50Kto59K = -1
        self.income_60Kto74K = -1
        self.income_75Kto99K = -1
        self.income_100Kto124K = -1
        self.income_125Kto149K = -1
        self.income_150Kto199K = -1
        self.income_200KOver = -1

    #
    # ALL GETTERS
    #

    def getCensusName(self):
        return self.censusname

    def getCounty(self):
        return self.county

    def getState(self):
        return self.state

    def getTotalMales(self):
        return self.totalMales

    def getTotalFemales(self):
        return self.totalFemales

    def getWhiteAlone(self):
        return self.whiteAlone

    def getBlackAlone(self):
        return self.blackAlone

    def getIndianAlone(self):
        return self.indianAlone

    def getAsianAlone(self):
        return self.asianAlone

    def getHawaiianAlone(self):
        return self.hawaiianAlone

    def getOtherRaceAlone(self):
        return self.otherRaceAlone

    def getTwoOrMoreRaces(self):
        return self.twoOrMoreRaces

    def getHispanicOrLatino(self):
        return self.hispanicOrLatino

    def getWhiteAlone_NotHisp(self):
        return self.whiteAlone_NotHisp

    def getAgeUnder6yrs(self):
        maleTotals = self.ageUnder1yr_males + self.age1yrs_male + self.age2yrs_male + self.age3yrs_male + \
                     self.age4yrs_male + self.age5yrs_male
        femaleTotals = self.ageUnder1yr_female + self.age1yrs_female + self.age2yrs_female + self.age3yrs_female + \
                       self.age4yrs_female + self.age5yrs_female
        return maleTotals + femaleTotals

    def getAge6to18yrs(self):
        maleTotals = self.age6yrs_male + self.age7yrs_male + self.age8yrs_male + self.age9yrs_male + \
                     self.age10yrs_male + self.age11yrs_male + self.age12yrs_male + self.age13yrs_male + \
                     self.age14yrs_male + self.age15yrs_male + self.age16yrs_male + self.age17yrs_male + \
                     self.age18yrs_male
        femaleTotals = self.age6yrs_female + self.age7yrs_female + self.age8yrs_female + self.age9yrs_female + \
                       self.age10yrs_female + self.age11yrs_female + self.age12yrs_female + self.age13yrs_female + \
                       self.age14yrs_female + self.age15yrs_female + self.age14yrs_female + self.age15yrs_female + \
                       self.age16yrs_female + self.age17yrs_female + self.age18yrs_female
        return maleTotals + femaleTotals

    def getAge19to25yrs(self):
        maleTotals = self.age19yrs_male + self.age20yrs_male + self.age21yrs_male + self.age22yrs_male + \
                     self.age23yrs_male + self.age24yrs_male + self.age25yrs_male
        femaleTotals = self.age19yrs_female + self.age20yrs_female + self.age21yrs_female + self.age22yrs_female + \
                       self.age23yrs_female + self.age24yrs_female + self.age25yrs_female
        return maleTotals + femaleTotals

    def getAge26to34yrs(self):
        maleTotals = self.age26yrs_male + self.age27yrs_male + self.age28yrs_male + self.age29yrs_male + \
                     self.age30yrs_male + self.age31yrs_male + self.age32yrs_male + self.age33yrs_male + \
                     self.age34yrs_male
        femaleTotals = self.age26yrs_female + self.age27yrs_female + self.age28yrs_female + self.age29yrs_female + \
                       self.age30yrs_female + self.age31yrs_female + self.age32yrs_female + self.age33yrs_female + \
                       self.age34yrs_female
        return maleTotals + femaleTotals

    def getAge35to44yrs(self):
        maleTotals = self.age35yrs_male + self.age36yrs_male + self.age37yrs_male + self.age38yrs_male + \
                     self.age39yrs_male + self.age40yrs_male + self.age41yrs_male + self.age42yrs_male + \
                     self.age43yrs_male + self.age44yrs_male
        femaleTotals = self.age35yrs_female + self.age36yrs_female + self.age37yrs_female + self.age38yrs_female + \
                       self.age39yrs_female + self.age40yrs_female + self.age41yrs_female + self.age42yrs_female + \
                       self.age43yrs_female + self.age44yrs_female
        return maleTotals + femaleTotals

    def getAge45to54yrs(self):
        maleTotals = self.age45yrs_male + self.age46yrs_male + self.age47yrs_male + self.age48yrs_male + \
                     self.age49yrs_male + self.age50yrs_male + self.age51yrs_male + self.age52yrs_male + \
                     self.age53yrs_male + self.age54yrs_male
        femaleTotals = self.age45yrs_female + self.age46yrs_female + self.age47yrs_female + self.age48yrs_female + \
                       self.age49yrs_female + self.age50yrs_female + self.age51yrs_female + self.age52yrs_female + \
                       self.age53yrs_female + self.age54yrs_female
        return maleTotals + femaleTotals

    def getAge55to64yrs(self):
        maleTotals = self.age55yrs_male + self.age56yrs_male + self.age57yrs_male + self.age58yrs_male + \
                     self.age59yrs_male + self.age60yrs_male + self.age61yrs_male + self.age62yrs_male + \
                     self.age63yrs_male + self.age64yrs_male
        femaleTotals = self.age55yrs_female + self.age56yrs_female + self.age57yrs_female + self.age58yrs_female + \
                       self.age59yrs_female + self.age60yrs_female + self.age61yrs_female + self.age62yrs_female + \
                       self.age63yrs_female + self.age64yrs_female
        return maleTotals + femaleTotals

    def getAge65to74yrs(self):
        maleTotals = self.age65yrs_male + self.age66yrs_male + self.age67yrs_male + self.age68yrs_male + \
                     self.age69yrs_male + self.age70yrs_male + self.age71yrs_male + self.age72yrs_male + \
                     self.age73yrs_male + self.age74yrs_male
        femaleTotals = self.age65yrs_female + self.age66yrs_female + self.age67yrs_female + self.age68yrs_female + \
                       self.age69yrs_female + self.age70yrs_female + self.age71yrs_female + self.age72yrs_female + \
                       self.age73yrs_female + self.age74yrs_female
        return maleTotals + femaleTotals

    def getAgeAbove75yrs(self):
        maleTotals = self.age75yrs_male + self.age76yrs_male + self.age77yrs_male + self.age78yrs_male + \
                     self.age79yrs_male + self.age80yrs_male + self.age81yrs_male + self.age82yrs_male + \
                     self.age83yrs_male + self.age84yrs_male + self.age85yrs_male + self.age86yrs_male + \
                     self.age87yrs_male + self.age88yrs_male + self.age89yrs_male + self.age90yrs_male + \
                     self.age91yrs_male + self.age92yrs_male + self.age93yrs_male + self.age94yrs_male + \
                     self.age95yrs_male + self.age96yrs_male + self.age97yrs_male + self.age98yrs_male + \
                     self.age99yrs_male + self.age100_104yrs_male + self.age105_108yrs_male + \
                     self.ageOver110yrs_male
        femaleTotals = self.age75yrs_female + self.age76yrs_female + self.age77yrs_female + self.age78yrs_female + \
                       self.age79yrs_female + self.age80yrs_female + self.age81yrs_female + self.age82yrs_female + \
                       self.age83yrs_female + self.age84yrs_female + self.age85yrs_female + self.age86yrs_female + \
                       self.age87yrs_female + self.age88yrs_female + self.age89yrs_female + self.age90yrs_female + \
                       self.age91yrs_female + self.age92yrs_female + self.age93yrs_female + self.age94yrs_female + \
                       self.age95yrs_female + self.age96yrs_female + self.age97yrs_female + self.age98yrs_female + \
                       self.age99yrs_female + self.age100_104yrs_female + self.age105_108yrs_female + \
                       self.ageOver110yrs_female
        return maleTotals + femaleTotals

    def getEmployed(self):
        return self.employed

    def getUnemployed(self):
        maleTotals = self.unemployed_16to19_Males + self.unemployed_20to21_Males + self.unemployed_22to24_Males + \
                     self.unemployed_25to29_Males + self.unemployed_30to34_Males + self.unemployed_35to44_Males + \
                     self.unemployed_45to54_Males + self.unemployed_55to59_Males + self.unemployed_60to61_Males + \
                     self.unemployed_62to64_Males + self.unemployed_65to69_Males + self.unemployed_70to74_Males + \
                     self.unemployed_75Over_Males
        femaleTotals = self.unemployed_16to19_Females + self.unemployed_20to21_Females + self.unemployed_22to24_Females + \
                       self.unemployed_25to29_Females + self.unemployed_30to34_Females + self.unemployed_35to44_Females + \
                       self.unemployed_45to54_Females + self.unemployed_55to59_Females + self.unemployed_60to61_Females + \
                       self.unemployed_62to64_Females + self.unemployed_65to69_Females + self.unemployed_70to74_Females + \
                       self.unemployed_75Over_Females

        return maleTotals + femaleTotals

    def getNotinLaborForce(self):
        maleTotals = self.notInLaborForce_16to19_Males + self.notInLaborForce_20to21_Males + \
                     self.notInLaborForce_22to24_Males + self.notInLaborForce_25to29_Males + \
                     self.notInLaborForce_30to34_Males + self.notInLaborForce_35to44_Males + \
                     self.notInLaborForce_45to54_Males + self.notInLaborForce_55to59_Males + \
                     self.notInLaborForce_60to61_Males + self.notInLaborForce_62to64_Males + \
                     self.notInLaborForce_65to69_Males + self.notInLaborForce_70to74_Males + \
                     self.notInLaborForce_75Over_Males
        femaleTotals = self.notInLaborForce_16to19_Females + self.notInLaborForce_20to21_Females + \
                       self.notInLaborForce_22to24_Females + self.notInLaborForce_25to29_Females + \
                       self.notInLaborForce_30to34_Females + self.notInLaborForce_35to44_Females + \
                       self.notInLaborForce_45to54_Females + self.notInLaborForce_55to59_Females + \
                       self.notInLaborForce_60to61_Females + self.notInLaborForce_62to64_Females + \
                       self.notInLaborForce_65to69_Females + self.notInLaborForce_70to74_Females + \
                       self.notInLaborForce_75Over_Females

        return maleTotals + femaleTotals

    def getIncomeUnder25K(self):
        income = self.income_Less_than_10K + self.income_10Kto14K + self.income_15Kto19K + self.income_20Kto24K
        return income

    def getIncome25Kto49K(self):
        income = self.income_25Kto29K + self.income_30Kto34K + self.income_35Kto39K + self.income_40Kto44K + \
                 self.income_45Kto49K
        return income

    def getIncome50Kto74K(self):
        income = self.income_50Kto59K + self.income_60Kto74K
        return income

    def getIncome75Kto99K(self):
        income = self.income_75Kto99K
        return income

    def getIncome100KOver(self):
        income = self.income_100Kto124K + self.income_125Kto149K + self.income_150Kto199K + self.income_200KOver
        return income

    #
    # RACE & ETHNICITIES (setters)
    #

    def setWhiteAlone(self, whiteAlone):
        self.whiteAlone = whiteAlone

    def setBlackAlone(self, blackAlone):
        self.blackAlone = blackAlone

    def setIndianAlone(self, indianAlone):
        self.indianAlone = indianAlone

    def setAsianAlone(self, asianAlone):
        self.asianAlone = asianAlone

    def setHawaiianAlone(self, hawaiianAlone):
        self.hawaiianAlone = hawaiianAlone

    def setOtherRaceAlone(self, otherRaceAlone):
        self.otherRaceAlone = otherRaceAlone

    def setTwoOrMoreRaces(self, twoOrMoreRaces):
        self.twoOrMoreRaces = twoOrMoreRaces

    def setHispanicOrLatino(self, hispanicOrLatino):
        self.hispanicOrLatino = hispanicOrLatino

    def setWhiteAlone_NotHisp(self, whiteAlone_NotHisp):
        self.whiteAlone_NotHisp = whiteAlone_NotHisp

    #
    # MALE DATA (setters)
    #
    def setTotalMales(self, males):
        self.totalMales = males

    def setAgeUnder1yrs_males(self, ageUnder1yrs_males):
        self.ageUnder1yr_males = ageUnder1yrs_males

    def setAge1yrs_males(self, age1yrs_males):
        self.age1yrs_male = age1yrs_males

    def setAge2yrs_males(self, age2yrs_males):
        self.age2yrs_male = age2yrs_males

    def setAge3yrs_males(self, age3yrs_males):
        self.age3yrs_male = age3yrs_males

    def setAge4yrs_males(self, age4yrs_males):
        self.age4yrs_male = age4yrs_males

    def setAge5yrs_males(self, age5yrs_males):
        self.age5yrs_male = age5yrs_males

    def setAge6yrs_males(self, age6yrs_males):
        self.age6yrs_male = age6yrs_males

    def setAge7yrs_males(self, age7yrs_males):
        self.age7yrs_male = age7yrs_males

    def setAge8yrs_males(self, age8yrs_males):
        self.age8yrs_male = age8yrs_males

    def setAge9yrs_males(self, age9yrs_males):
        self.age9yrs_male = age9yrs_males

    def setAge10yrs_males(self, age10yrs_males):
        self.age10yrs_male = age10yrs_males

    def setAge11yrs_males(self, age11yrs_males):
        self.age11yrs_male = age11yrs_males

    def setAge12yrs_males(self, age12yrs_males):
        self.age12yrs_male = age12yrs_males

    def setAge13yrs_males(self, age13yrs_males):
        self.age13yrs_male = age13yrs_males

    def setAge14yrs_males(self, age14yrs_males):
        self.age14yrs_male = age14yrs_males

    def setAge15yrs_males(self, age15yrs_males):
        self.age15yrs_male = age15yrs_males

    def setAge16yrs_males(self, age16yrs_males):
        self.age16yrs_male = age16yrs_males

    def setAge17yrs_males(self, age17yrs_males):
        self.age17yrs_male = age17yrs_males

    def setAge18yrs_males(self, age18yrs_males):
        self.age18yrs_male = age18yrs_males

    def setAge19yrs_males(self, age19yrs_males):
        self.age19yrs_male = age19yrs_males

    def setAge20yrs_males(self, age20yrs_males):
        self.age20yrs_male = age20yrs_males

    def setAge21yrs_males(self, age21yrs_males):
        self.age21yrs_male = age21yrs_males

    def setAge22yrs_males(self, age22yrs_males):
        self.age22yrs_male = age22yrs_males

    def setAge23yrs_males(self, age23yrs_males):
        self.age23yrs_male = age23yrs_males

    def setAge24yrs_males(self, age24yrs_males):
        self.age24yrs_male = age24yrs_males

    def setAge25yrs_males(self, age25yrs_males):
        self.age25yrs_male = age25yrs_males

    def setAge26yrs_males(self, age26yrs_males):
        self.age26yrs_male = age26yrs_males

    def setAge27yrs_males(self, age27yrs_males):
        self.age27yrs_male = age27yrs_males

    def setAge28yrs_males(self, age28yrs_males):
        self.age28yrs_male = age28yrs_males

    def setAge29yrs_males(self, age29yrs_males):
        self.age29yrs_male = age29yrs_males

    def setAge30yrs_males(self, age30yrs_males):
        self.age30yrs_male = age30yrs_males

    def setAge31yrs_males(self, age31yrs_males):
        self.age31yrs_male = age31yrs_males

    def setAge32yrs_males(self, age32yrs_males):
        self.age32yrs_male = age32yrs_males

    def setAge33yrs_males(self, age33yrs_males):
        self.age33yrs_male = age33yrs_males

    def setAge34yrs_males(self, age34yrs_males):
        self.age34yrs_male = age34yrs_males

    def setAge35yrs_males(self, age35yrs_males):
        self.age35yrs_male = age35yrs_males

    def setAge36yrs_males(self, age36yrs_males):
        self.age36yrs_male = age36yrs_males

    def setAge37yrs_males(self, age37yrs_males):
        self.age37yrs_male = age37yrs_males

    def setAge38yrs_males(self, age38yrs_males):
        self.age38yrs_male = age38yrs_males

    def setAge39yrs_males(self, age39yrs_males):
        self.age39yrs_male = age39yrs_males

    def setAge40yrs_males(self, age40yrs_males):
        self.age40yrs_male = age40yrs_males

    def setAge41yrs_males(self, age41yrs_males):
        self.age41yrs_male = age41yrs_males

    def setAge42yrs_males(self, age42yrs_males):
        self.age42yrs_male = age42yrs_males

    def setAge43yrs_males(self, age43yrs_males):
        self.age43yrs_male = age43yrs_males

    def setAge44yrs_males(self, age44yrs_males):
        self.age44yrs_male = age44yrs_males

    def setAge45yrs_males(self, age45yrs_males):
        self.age45yrs_male = age45yrs_males

    def setAge46yrs_males(self, age46yrs_males):
        self.age46yrs_male = age46yrs_males

    def setAge47yrs_males(self, age47yrs_males):
        self.age47yrs_male = age47yrs_males

    def setAge48yrs_males(self, age48yrs_males):
        self.age48yrs_male = age48yrs_males

    def setAge49yrs_males(self, age49yrs_males):
        self.age49yrs_male = age49yrs_males

    def setAge50yrs_males(self, age50yrs_males):
        self.age50yrs_male = age50yrs_males

    def setAge51yrs_males(self, age51yrs_males):
        self.age51yrs_male = age51yrs_males

    def setAge52yrs_males(self, age52yrs_males):
        self.age52yrs_male = age52yrs_males

    def setAge53yrs_males(self, age53yrs_males):
        self.age53yrs_male = age53yrs_males

    def setAge54yrs_males(self, age54yrs_males):
        self.age54yrs_male = age54yrs_males

    def setAge55yrs_males(self, age55yrs_males):
        self.age55yrs_male = age55yrs_males

    def setAge56yrs_males(self, age56yrs_males):
        self.age56yrs_male = age56yrs_males

    def setAge57yrs_males(self, age57yrs_males):
        self.age57yrs_male = age57yrs_males

    def setAge58yrs_males(self, age58yrs_males):
        self.age58yrs_male = age58yrs_males

    def setAge59yrs_males(self, age59yrs_males):
        self.age59yrs_male = age59yrs_males

    def setAge60yrs_males(self, age60yrs_males):
        self.age60yrs_male = age60yrs_males

    def setAge61yrs_males(self, age61yrs_males):
        self.age61yrs_male = age61yrs_males

    def setAge62yrs_males(self, age62yrs_males):
        self.age62yrs_male = age62yrs_males

    def setAge63yrs_males(self, age63yrs_males):
        self.age63yrs_male = age63yrs_males

    def setAge64yrs_males(self, age64yrs_males):
        self.age64yrs_male = age64yrs_males

    def setAge65yrs_males(self, age65yrs_males):
        self.age65yrs_male = age65yrs_males

    def setAge66yrs_males(self, age66yrs_males):
        self.age66yrs_male = age66yrs_males

    def setAge67yrs_males(self, age67yrs_males):
        self.age67yrs_male = age67yrs_males

    def setAge68yrs_males(self, age68yrs_males):
        self.age68yrs_male = age68yrs_males

    def setAge69yrs_males(self, age69yrs_males):
        self.age69yrs_male = age69yrs_males

    def setAge70yrs_males(self, age70yrs_males):
        self.age70yrs_male = age70yrs_males

    def setAge71yrs_males(self, age71yrs_males):
        self.age71yrs_male = age71yrs_males

    def setAge72yrs_males(self, age72yrs_males):
        self.age72yrs_male = age72yrs_males

    def setAge73yrs_males(self, age73yrs_males):
        self.age73yrs_male = age73yrs_males

    def setAge74yrs_males(self, age74yrs_males):
        self.age74yrs_male = age74yrs_males

    def setAge75yrs_males(self, age75yrs_males):
        self.age75yrs_male = age75yrs_males

    def setAge76yrs_males(self, age76yrs_males):
        self.age76yrs_male = age76yrs_males

    def setAge77yrs_males(self, age77yrs_males):
        self.age77yrs_male = age77yrs_males

    def setAge78yrs_males(self, age78yrs_males):
        self.age78yrs_male = age78yrs_males

    def setAge79yrs_males(self, age79yrs_males):
        self.age79yrs_male = age79yrs_males

    def setAge80yrs_males(self, age80yrs_males):
        self.age80yrs_male = age80yrs_males

    def setAge81yrs_males(self, age81yrs_males):
        self.age81yrs_male = age81yrs_males

    def setAge82yrs_males(self, age82yrs_males):
        self.age82yrs_male = age82yrs_males

    def setAge83yrs_males(self, age83yrs_males):
        self.age83yrs_male = age83yrs_males

    def setAge84yrs_males(self, age84yrs_males):
        self.age84yrs_male = age84yrs_males

    def setAge85yrs_males(self, age85yrs_males):
        self.age85yrs_male = age85yrs_males

    def setAge86yrs_males(self, age86yrs_males):
        self.age86yrs_male = age86yrs_males

    def setAge87yrs_males(self, age87yrs_males):
        self.age87yrs_male = age87yrs_males

    def setAge88yrs_males(self, age88yrs_males):
        self.age88yrs_male = age88yrs_males

    def setAge89yrs_males(self, age89yrs_males):
        self.age89yrs_male = age89yrs_males

    def setAge90yrs_males(self, age90yrs_males):
        self.age90yrs_male = age90yrs_males

    def setAge91yrs_males(self, age91yrs_males):
        self.age91yrs_male = age91yrs_males

    def setAge92yrs_males(self, age92yrs_males):
        self.age92yrs_male = age92yrs_males

    def setAge93yrs_males(self, age93yrs_males):
        self.age93yrs_male = age93yrs_males

    def setAge94yrs_males(self, age94yrs_males):
        self.age94yrs_male = age94yrs_males

    def setAge95yrs_males(self, age95yrs_males):
        self.age95yrs_male = age95yrs_males

    def setAge96yrs_males(self, age96yrs_males):
        self.age96yrs_male = age96yrs_males

    def setAge97yrs_males(self, age97yrs_males):
        self.age97yrs_male = age97yrs_males

    def setAge98yrs_males(self, age98yrs_males):
        self.age98yrs_male = age98yrs_males

    def setAge99yrs_males(self, age99yrs_males):
        self.age99yrs_male = age99yrs_males

    def setAge100_104yrs_male(self, age100_104yrs_male):
        self.age100_104yrs_male = age100_104yrs_male

    def setAge105_109yrs_male(self, age105_108yrs_male):
        self.age105_108yrs_male = age105_108yrs_male

    def setAgeOver110yrs_male(self, ageOver110yrs_male):
        self.ageOver110yrs_male = ageOver110yrs_male

    #
    # FEMALE Data (setters)
    #

    def setTotalFemales(self, females):
        self.totalFemales = females

    def setAgeUnder1yrs_female(self, ageUnder1yrs_female):
        self.ageUnder1yr_males = ageUnder1yrs_female

    def setAge1yrs_female(self, age1yrs_female):
        self.age1yrs_female = age1yrs_female

    def setAge2yrs_female(self, age2yrs_female):
        self.age2yrs_female = age2yrs_female

    def setAge3yrs_female(self, age3yrs_female):
        self.age3yrs_female = age3yrs_female

    def setAge4yrs_female(self, age4yrs_female):
        self.age4yrs_female = age4yrs_female

    def setAge5yrs_female(self, age5yrs_female):
        self.age5yrs_female = age5yrs_female

    def setAge6yrs_female(self, age6yrs_female):
        self.age6yrs_female = age6yrs_female

    def setAge7yrs_female(self, age7yrs_female):
        self.age7yrs_female = age7yrs_female

    def setAge8yrs_female(self, age8yrs_female):
        self.age8yrs_female = age8yrs_female

    def setAge9yrs_female(self, age9yrs_female):
        self.age9yrs_female = age9yrs_female

    def setAge10yrs_female(self, age10yrs_female):
        self.age10yrs_female = age10yrs_female

    def setAge11yrs_female(self, age11yrs_female):
        self.age11yrs_female = age11yrs_female

    def setAge12yrs_female(self, age12yrs_female):
        self.age12yrs_female = age12yrs_female

    def setAge13yrs_female(self, age13yrs_female):
        self.age13yrs_female = age13yrs_female

    def setAge14yrs_female(self, age14yrs_female):
        self.age14yrs_female = age14yrs_female

    def setAge15yrs_female(self, age15yrs_female):
        self.age15yrs_female = age15yrs_female

    def setAge16yrs_female(self, age16yrs_female):
        self.age16yrs_female = age16yrs_female

    def setAge17yrs_female(self, age17yrs_female):
        self.age17yrs_female = age17yrs_female

    def setAge18yrs_female(self, age18yrs_female):
        self.age18yrs_female = age18yrs_female

    def setAge19yrs_female(self, age19yrs_female):
        self.age19yrs_female = age19yrs_female

    def setAge20yrs_female(self, age20yrs_female):
        self.age20yrs_female = age20yrs_female

    def setAge21yrs_female(self, age21yrs_female):
        self.age21yrs_female = age21yrs_female

    def setAge22yrs_female(self, age22yrs_female):
        self.age22yrs_female = age22yrs_female

    def setAge23yrs_female(self, age23yrs_female):
        self.age23yrs_female = age23yrs_female

    def setAge24yrs_female(self, age24yrs_female):
        self.age24yrs_female = age24yrs_female

    def setAge25yrs_female(self, age25yrs_female):
        self.age25yrs_female = age25yrs_female

    def setAge26yrs_female(self, age26yrs_female):
        self.age26yrs_female = age26yrs_female

    def setAge27yrs_female(self, age27yrs_female):
        self.age27yrs_female = age27yrs_female

    def setAge28yrs_female(self, age28yrs_female):
        self.age28yrs_female = age28yrs_female

    def setAge29yrs_female(self, age29yrs_female):
        self.age29yrs_female = age29yrs_female

    def setAge30yrs_female(self, age30yrs_female):
        self.age30yrs_female = age30yrs_female

    def setAge31yrs_female(self, age31yrs_female):
        self.age31yrs_female = age31yrs_female

    def setAge32yrs_female(self, age32yrs_female):
        self.age32yrs_female = age32yrs_female

    def setAge33yrs_female(self, age33yrs_female):
        self.age33yrs_female = age33yrs_female

    def setAge34yrs_female(self, age34yrs_female):
        self.age34yrs_female = age34yrs_female

    def setAge35yrs_female(self, age35yrs_female):
        self.age35yrs_female = age35yrs_female

    def setAge36yrs_female(self, age36yrs_female):
        self.age36yrs_female = age36yrs_female

    def setAge37yrs_female(self, age37yrs_female):
        self.age37yrs_female = age37yrs_female

    def setAge38yrs_female(self, age38yrs_female):
        self.age38yrs_female = age38yrs_female

    def setAge39yrs_female(self, age39yrs_female):
        self.age39yrs_female = age39yrs_female

    def setAge40yrs_female(self, age40yrs_female):
        self.age40yrs_female = age40yrs_female

    def setAge41yrs_female(self, age41yrs_female):
        self.age41yrs_female = age41yrs_female

    def setAge42yrs_female(self, age42yrs_female):
        self.age42yrs_female = age42yrs_female

    def setAge43yrs_female(self, age43yrs_female):
        self.age43yrs_female = age43yrs_female

    def setAge44yrs_female(self, age44yrs_female):
        self.age44yrs_female = age44yrs_female

    def setAge45yrs_female(self, age45yrs_female):
        self.age45yrs_female = age45yrs_female

    def setAge46yrs_female(self, age46yrs_female):
        self.age46yrs_female = age46yrs_female

    def setAge47yrs_female(self, age47yrs_female):
        self.age47yrs_female = age47yrs_female

    def setAge48yrs_female(self, age48yrs_female):
        self.age48yrs_female = age48yrs_female

    def setAge49yrs_female(self, age49yrs_female):
        self.age49yrs_female = age49yrs_female

    def setAge50yrs_female(self, age50yrs_female):
        self.age50yrs_female = age50yrs_female

    def setAge51yrs_female(self, age51yrs_female):
        self.age51yrs_female = age51yrs_female

    def setAge52yrs_female(self, age52yrs_female):
        self.age52yrs_female = age52yrs_female

    def setAge53yrs_female(self, age53yrs_female):
        self.age53yrs_female = age53yrs_female

    def setAge54yrs_female(self, age54yrs_female):
        self.age54yrs_female = age54yrs_female

    def setAge55yrs_female(self, age55yrs_female):
        self.age55yrs_female = age55yrs_female

    def setAge56yrs_female(self, age56yrs_female):
        self.age56yrs_female = age56yrs_female

    def setAge57yrs_female(self, age57yrs_female):
        self.age57yrs_female = age57yrs_female

    def setAge58yrs_female(self, age58yrs_female):
        self.age58yrs_female = age58yrs_female

    def setAge59yrs_female(self, age59yrs_female):
        self.age59yrs_female = age59yrs_female

    def setAge60yrs_female(self, age60yrs_female):
        self.age60yrs_female = age60yrs_female

    def setAge61yrs_female(self, age61yrs_female):
        self.age61yrs_female = age61yrs_female

    def setAge62yrs_female(self, age62yrs_female):
        self.age62yrs_female = age62yrs_female

    def setAge63yrs_female(self, age63yrs_female):
        self.age63yrs_female = age63yrs_female

    def setAge64yrs_female(self, age64yrs_female):
        self.age64yrs_female = age64yrs_female

    def setAge65yrs_female(self, age65yrs_female):
        self.age65yrs_female = age65yrs_female

    def setAge66yrs_female(self, age66yrs_female):
        self.age66yrs_female = age66yrs_female

    def setAge67yrs_female(self, age67yrs_female):
        self.age67yrs_female = age67yrs_female

    def setAge68yrs_female(self, age68yrs_female):
        self.age68yrs_female = age68yrs_female

    def setAge69yrs_female(self, age69yrs_female):
        self.age69yrs_female = age69yrs_female

    def setAge70yrs_female(self, age70yrs_female):
        self.age70yrs_female = age70yrs_female

    def setAge71yrs_female(self, age71yrs_female):
        self.age71yrs_female = age71yrs_female

    def setAge72yrs_female(self, age72yrs_female):
        self.age72yrs_female = age72yrs_female

    def setAge73yrs_female(self, age73yrs_female):
        self.age73yrs_female = age73yrs_female

    def setAge74yrs_female(self, age74yrs_female):
        self.age74yrs_female = age74yrs_female

    def setAge75yrs_female(self, age75yrs_female):
        self.age75yrs_female = age75yrs_female

    def setAge76yrs_female(self, age76yrs_female):
        self.age76yrs_female = age76yrs_female

    def setAge77yrs_female(self, age77yrs_female):
        self.age77yrs_female = age77yrs_female

    def setAge78yrs_female(self, age78yrs_female):
        self.age78yrs_female = age78yrs_female

    def setAge79yrs_female(self, age79yrs_female):
        self.age79yrs_female = age79yrs_female

    def setAge80yrs_female(self, age80yrs_female):
        self.age80yrs_female = age80yrs_female

    def setAge81yrs_female(self, age81yrs_female):
        self.age81yrs_female = age81yrs_female

    def setAge82yrs_female(self, age82yrs_female):
        self.age82yrs_female = age82yrs_female

    def setAge83yrs_female(self, age83yrs_female):
        self.age83yrs_female = age83yrs_female

    def setAge84yrs_female(self, age84yrs_female):
        self.age84yrs_female = age84yrs_female

    def setAge85yrs_female(self, age85yrs_female):
        self.age85yrs_female = age85yrs_female

    def setAge86yrs_female(self, age86yrs_female):
        self.age86yrs_female = age86yrs_female

    def setAge87yrs_female(self, age87yrs_female):
        self.age87yrs_female = age87yrs_female

    def setAge88yrs_female(self, age88yrs_female):
        self.age88yrs_female = age88yrs_female

    def setAge89yrs_female(self, age89yrs_female):
        self.age89yrs_female = age89yrs_female

    def setAge90yrs_female(self, age90yrs_female):
        self.age90yrs_female = age90yrs_female

    def setAge91yrs_female(self, age91yrs_female):
        self.age91yrs_female = age91yrs_female

    def setAge92yrs_female(self, age92yrs_female):
        self.age92yrs_female = age92yrs_female

    def setAge93yrs_female(self, age93yrs_female):
        self.age93yrs_female = age93yrs_female

    def setAge94yrs_female(self, age94yrs_female):
        self.age94yrs_female = age94yrs_female

    def setAge95yrs_female(self, age95yrs_female):
        self.age95yrs_female = age95yrs_female

    def setAge96yrs_female(self, age96yrs_female):
        self.age96yrs_female = age96yrs_female

    def setAge97yrs_female(self, age97yrs_female):
        self.age97yrs_female = age97yrs_female

    def setAge98yrs_female(self, age98yrs_female):
        self.age98yrs_female = age98yrs_female

    def setAge99yrs_female(self, age99yrs_female):
        self.age99yrs_female = age99yrs_female

    def setAge100_104yrs_female(self, age100_104yrs_female):
        self.age100_104yrs_female = age100_104yrs_female

    def setAge105_109yrs_female(self, age105_108yrs_female):
        self.age105_108yrs_female = age105_108yrs_female

    def setAgeOver110yrs_female(self, ageOver110yrs_female):
        self.ageOver110yrs_female = ageOver110yrs_female

    def setEmployed(self, employed):
        self.employed = employed

    def setUnemployed_16to19_males(self, unemployed_16to19_Males):
        self.unemployed_16to19_Males = unemployed_16to19_Males

    def setUnemployed_20to21_males(self, unemployed_20to21_Males):
        self.unemployed_20to21_Males = unemployed_20to21_Males

    def setUnemployed_22to24_males(self, unemployed_22to24_Males):
        self.unemployed_22to24_Males = unemployed_22to24_Males

    def setUnemployed_25to29_males(self, unemployed_25to29_Males):
        self.unemployed_25to29_Males = unemployed_25to29_Males

    def setUnemployed_30to34_males(self, unemployed_30to34_Males):
        self.unemployed_30to34_Males = unemployed_30to34_Males

    def setUnemployed_35to44_males(self, unemployed_35to44_Males):
        self.unemployed_35to44_Males = unemployed_35to44_Males

    def setUnemployed_45to54_males(self, unemployed_45to54_Males):
        self.unemployed_45to54_Males = unemployed_45to54_Males

    def setUnemployed_55to59_males(self, unemployed_55to59_Males):
        self.unemployed_55to59_Males = unemployed_55to59_Males

    def setUnemployed_60to61_males(self, unemployed_60to61_Males):
        self.unemployed_60to61_Males = unemployed_60to61_Males

    def setUnemployed_62to64_males(self, unemployed_62to64_Males):
        self.unemployed_62to64_Males = unemployed_62to64_Males

    def setUnemployed_65to69_males(self, unemployed_65to69_Males):
        self.unemployed_65to69_Males = unemployed_65to69_Males

    def setUnemployed_70to74_males(self, unemployed_70to74_Males):
        self.unemployed_70to74_Males = unemployed_70to74_Males

    def setUnemployed_75over_males(self, unemployed_75Over_Males):
        self.unemployed_75Over_Males = unemployed_75Over_Males

    def setUnemployed_16to19_females(self, unemployed_16to19_Females):
        self.unemployed_16to19_Females = unemployed_16to19_Females

    def setUnemployed_20to21_females(self, unemployed_20to21_Females):
        self.unemployed_20to21_Females = unemployed_20to21_Females

    def setUnemployed_22to24_females(self, unemployed_22to24_Females):
        self.unemployed_22to24_Females = unemployed_22to24_Females

    def setUnemployed_25to29_females(self, unemployed_25to29_Females):
        self.unemployed_25to29_Females = unemployed_25to29_Females

    def setUnemployed_30to34_females(self, unemployed_30to34_Females):
        self.unemployed_30to34_Females = unemployed_30to34_Females

    def setUnemployed_35to44_females(self, unemployed_35to44_Females):
        self.unemployed_35to44_Females = unemployed_35to44_Females

    def setUnemployed_45to54_females(self, unemployed_45to54_Females):
        self.unemployed_45to54_Females = unemployed_45to54_Females

    def setUnemployed_55to59_females(self, unemployed_55to59_Females):
        self.unemployed_55to59_Females = unemployed_55to59_Females

    def setUnemployed_60to61_females(self, unemployed_60to61_Females):
        self.unemployed_60to61_Females = unemployed_60to61_Females

    def setUnemployed_62to64_females(self, unemployed_62to64_Females):
        self.unemployed_62to64_Females = unemployed_62to64_Females

    def setUnemployed_65to69_females(self, unemployed_65to69_Females):
        self.unemployed_65to69_Females = unemployed_65to69_Females

    def setUnemployed_70to74_females(self, unemployed_70to74_Females):
        self.unemployed_70to74_Females = unemployed_70to74_Females

    def setUnemployed_75over_females(self, unemployed_75Over_Females):
        self.unemployed_75Over_Females = unemployed_75Over_Females

    def setNotinlaborforce_16to19_males(self, notInLaborForce_16to19_Males):
        self.notInLaborForce_16to19_Males = notInLaborForce_16to19_Males

    def setNotinlaborforce_20to21_males(self, notInLaborForce_20to21_Males):
        self.notInLaborForce_20to21_Males = notInLaborForce_20to21_Males

    def setNotinlaborforce_22to24_males(self, notInLaborForce_22to24_Males):
        self.notInLaborForce_22to24_Males = notInLaborForce_22to24_Males

    def setNotinlaborforce_25to29_males(self, notInLaborForce_25to29_Males):
        self.notInLaborForce_25to29_Males = notInLaborForce_25to29_Males

    def setNotinlaborforce_30to34_males(self, notInLaborForce_30to34_Males):
        self.notInLaborForce_30to34_Males = notInLaborForce_30to34_Males

    def setNotinlaborforce_35to44_males(self, notInLaborForce_35to44_Males):
        self.notInLaborForce_35to44_Males = notInLaborForce_35to44_Males

    def setNotinlaborforce_45to54_males(self, notInLaborForce_45to54_Males):
        self.notInLaborForce_45to54_Males = notInLaborForce_45to54_Males

    def setNotinlaborforce_55to59_males(self, notInLaborForce_55to59_Males):
        self.notInLaborForce_55to59_Males = notInLaborForce_55to59_Males

    def setNotinlaborforce_60to61_males(self, notInLaborForce_60to61_Males):
        self.notInLaborForce_60to61_Males = notInLaborForce_60to61_Males

    def setNotinlaborforce_62to64_males(self, notInLaborForce_62to64_Males):
        self.notInLaborForce_62to64_Males = notInLaborForce_62to64_Males

    def setNotinlaborforce_65to69_males(self, notInLaborForce_65to69_Males):
        self.notInLaborForce_65to69_Males = notInLaborForce_65to69_Males

    def setNotinlaborforce_70to74_males(self, notInLaborForce_70to74_Males):
        self.notInLaborForce_70to74_Males = notInLaborForce_70to74_Males

    def setNotinlaborforce_75over_males(self, notInLaborForce_75Over_Males):
        self.notInLaborForce_75Over_Males = notInLaborForce_75Over_Males

    def setNotinlaborforce_16to19_females(self, notInLaborForce_16to19_Females):
        self.notInLaborForce_16to19_Females = notInLaborForce_16to19_Females

    def setNotinlaborforce_20to21_females(self, notInLaborForce_20to21_Females):
        self.notInLaborForce_20to21_Females = notInLaborForce_20to21_Females

    def setNotinlaborforce_22to24_females(self, notInLaborForce_22to24_Females):
        self.notInLaborForce_22to24_Females = notInLaborForce_22to24_Females

    def setNotinlaborforce_25to29_females(self, notInLaborForce_25to29_Females):
        self.notInLaborForce_25to29_Females = notInLaborForce_25to29_Females

    def setNotinlaborforce_30to34_females(self, notInLaborForce_30to34_Females):
        self.notInLaborForce_30to34_Females = notInLaborForce_30to34_Females

    def setNotinlaborforce_35to44_females(self, notInLaborForce_35to44_Females):
        self.notInLaborForce_35to44_Females = notInLaborForce_35to44_Females

    def setNotinlaborforce_45to54_females(self, notInLaborForce_45to54_Females):
        self.notInLaborForce_45to54_Females = notInLaborForce_45to54_Females

    def setNotinlaborforce_55to59_females(self, notInLaborForce_55to59_Females):
        self.notInLaborForce_55to59_Females = notInLaborForce_55to59_Females

    def setNotinlaborforce_60to61_females(self, notInLaborForce_60to61_Females):
        self.notInLaborForce_60to61_Females = notInLaborForce_60to61_Females

    def setNotinlaborforce_62to64_females(self, notInLaborForce_62to64_Females):
        self.notInLaborForce_62to64_Females = notInLaborForce_62to64_Females

    def setNotinlaborforce_65to69_females(self, notInLaborForce_65to69_Females):
        self.notInLaborForce_65to69_Females = notInLaborForce_65to69_Females

    def setNotinlaborforce_70to74_females(self, notInLaborForce_70to74_Females):
        self.notInLaborForce_70to74_Females = notInLaborForce_70to74_Females

    def setNotinlaborforce_75over_females(self, notInLaborForce_75Over_Females):
        self.notInLaborForce_75Over_Females = notInLaborForce_75Over_Females

    def setIncome_less_than_10k(self, income_Less_than_10K):
        self.income_Less_than_10K = income_Less_than_10K

    def setIncome_10kto14k(self, income_10Kto14K):
        self.income_10Kto14K = income_10Kto14K

    def setIncome_15kto19k(self, income_15Kto19K):
        self.income_15Kto19K = income_15Kto19K

    def setIncome_20kto24k(self, income_20Kto24K):
        self.income_20Kto24K = income_20Kto24K

    def setIncome_25kto29k(self, income_25Kto29K):
        self.income_25Kto29K = income_25Kto29K

    def setIncome_30kto34k(self, income_30Kto34K):
        self.income_30Kto34K = income_30Kto34K

    def setIncome_35kto39k(self, income_35Kto39K):
        self.income_35Kto39K = income_35Kto39K

    def setIncome_40kto44k(self, income_40Kto44K):
        self.income_40Kto44K = income_40Kto44K

    def setIncome_45kto49k(self, income_45Kto49K):
        self.income_45Kto49K = income_45Kto49K

    def setIncome_50kto59k(self, income_50Kto59K):
        self.income_50Kto59K = income_50Kto59K

    def setIncome_60kto74k(self, income_60Kto74K):
        self.income_60Kto74K = income_60Kto74K

    def setIncome_75kto99k(self, income_75Kto99K):
        self.income_75Kto99K = income_75Kto99K

    def setIncome_100kto124k(self, income_100Kto124K):
        self.income_100Kto124K = income_100Kto124K

    def setIncome_125kto149k(self, income_125Kto149K):
        self.income_125Kto149K = income_125Kto149K

    def setIncome_150kto199k(self, income_150Kto199K):
        self.income_150Kto199K = income_150Kto199K

    def setIncome_200kover(self, income_200KOver):
        self.income_200KOver = income_200KOver
