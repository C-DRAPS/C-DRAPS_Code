# TODO: This file is a translator for our "Standardize & ID Assign.py"
#  These are inconsistencies between years:
#    1. 2000s
#    2. 2010s
#      * Alaska, Skagway-Hoonah-Angoon  ->   * Skagway + Hoonah-Angoon
#      * Alaska, Wrangell-Petersburg    ->   * Wrangell + Petersburg
#    3. 2020s
#      * Alaska, Chugach                ->    *Alaska, Valdez-Cordova (2010)
#      * Alaska, Copper River           ->    *Alaska, Valdez-Cordova (2010)
#      * Alaska, Kusilvak               ->    Alaska, Wade Hampton    (2010)
#      * South Dakota, Oglala Lakota    ->    South Dakota, Shannon   (2010)
def Translate(location):
    countyDictionary = {
        # 2010 Census
        "Maryland,Baltimore": "Maryland,Baltimore County",
        "Maryland,Baltimore city": "Maryland,Baltimore City",
        "Missouri,St. Louis": "Missouri,St. Louis County",
        "Missouri,St. Louis city": "Missouri,St. Louis City",
        "New Mexico,Do?a Ana": "New Mexico,Doña Ana",
        "Virginia,Bedford": "Virginia,Bedford County",
        "Virginia,Fairfax": "Virginia,Fairfax County",
        "Virginia,Franklin": "Virginia,Franklin County",
        "Virginia,Richmond": "Virginia,Richmond County",
        "Virginia,Roanoke": "Virginia,Roanoke County",
        "Virginia,Alexandria city": "Virginia,Alexandria",
        "Virginia,Bedford city": "Virginia,Bedford City",
        "Virginia,Bristol city": "Virginia,Bristol",
        "Virginia,Buena Vista city": "Virginia,Buena Vista",
        "Virginia,Charlottesville city": "Virginia,Charlottesville",
        "Virginia,Chesapeake city": "Virginia,Chesapeake",
        "Virginia,Colonial Heights city": "Virginia,Colonial Heights",
        "Virginia,Covington city": "Virginia,Covington",
        "Virginia,Danville city": "Virginia,Danville",
        "Virginia,Emporia city": "Virginia,Emporia",
        "Virginia,Fairfax city": "Virginia,Fairfax City",
        "Virginia,Falls Church city": "Virginia,Falls Church",
        "Virginia,Franklin city": "Virginia,Franklin City",
        "Virginia,Fredericksburg city": "Virginia,Fredericksburg",
        "Virginia,Galax city": "Virginia,Galax",
        "Virginia,Hampton city": "Virginia,Hampton",
        "Virginia,Harrisonburg city": "Virginia,Harrisonburg",
        "Virginia,Hopewell city": "Virginia,Hopewell",
        "Virginia,Lexington city": "Virginia,Lexington",
        "Virginia,Lynchburg city": "Virginia,Lynchburg",
        "Virginia,Manassas city": "Virginia,Manassas",
        "Virginia,Manassas Park city": "Virginia,Manassas Park",
        "Virginia,Martinsville city": "Virginia,Martinsville",
        "Virginia,Newport News city": "Virginia,Newport News",
        "Virginia,Norfolk city": "Virginia,Norfolk",
        "Virginia,Norton city": "Virginia,Norton",
        "Virginia,Petersburg city": "Virginia,Petersburg",
        "Virginia,Poquoson city": "Virginia,Poquoson",
        "Virginia,Portsmouth city": "Virginia,Portsmouth",
        "Virginia,Radford city": "Virginia,Radford",
        "Virginia,Richmond city": "Virginia,Richmond City",
        "Virginia,Roanoke city": "Virginia,Roanoke City",
        "Virginia,Salem city": "Virginia,Salem",
        "Virginia,Staunton city": "Virginia,Staunton",
        "Virginia,Suffolk city": "Virginia,Suffolk",
        "Virginia,Virginia Beach city": "Virginia,Virginia Beach",
        "Virginia,Waynesboro city": "Virginia,Waynesboro",
        "Virginia,Williamsburg city": "Virginia,Williamsburg",
        "Virginia,Winchester city": "Virginia,Winchester",
        "Puerto Rico,AÃ±asco": "Puerto Rico,Anasco",
        "Puerto Rico,BayamÃ³n": "Puerto Rico,Bayamon",
        "Puerto Rico,CanÃ³vanas": "Puerto Rico,Canovanas",
        "Puerto Rico,CataÃ±o": "Puerto Rico,Catano",
        "Puerto Rico,ComerÃ­o": "Puerto Rico,Comerio",
        "Puerto Rico,GuÃ¡nica": "Puerto Rico,Guanica",
        "Puerto Rico,Juana DÃ­az": "Puero Rico,Juana Diaz",
        "Puerto Rico,Las MarÃ­as": "Puerto Rico,Las Marias",
        "Puerto Rico,LoÃ­za": "Puerto Rico,Loiza",
        "Puerto Rico,ManatÃ­": "Puerto Rico,Manati",
        "Puerto Rico,MayagÃ¼ez": "Puerto Rico,Mayaguez",
        "Puerto Rico,PeÃ±uelas": "Puerto Rico,Penuelas",
        "Puerto Rico,RincÃ³n": "Puerto Rico,Rincon",
        "Puerto Rico,RÃ­o Grande": "Puerto Rico,Rio Grande",
        "Puerto Rico,San GermÃ¡n": "Puerto Rico,San German",
        "Puerto Rico,San SebastiÃ¡n": "Puerto Rico,San Sebastian",
        "Puerto Rico,Aguas buenas": "Puerto Rico,Aguas Buenas",  # TODO: New starts here...
        "Puerto Rico,Aï¿½asco": "Puerto Rico,Anasco",
        "Puerto Rico,Bayamï¿½n": "Puerto Rico,Bayamon",
        "Puerto Rico,Cabo rojo": "Puerto Rico,Cabo Rojo",
        "Puerto Rico,Canï¿½vanas": "Puerto Rico,Canovanas",
        "Puerto Rico,Cataï¿½o": "Puerto Rico,Catano",
        "Puerto Rico,Comerï¿½o": "Puerto Rico,Comerio",
        "Puerto Rico,Guï¿½nica": "Puerto Rico,Guanica",
        "Puerto Rico,Juana dï¿½az": "Puerto Rico,Juana Diaz",
        "Puerto Rico,Las marï¿½as": "Puerto Rico,Las Marias",
        "Puerto Rico,Manatï¿½": "Puerto Rico,Manati",
        "Puerto Rico,Las piedras": "Puerto Rico,Las Piedras",
        "Puerto Rico,Loï¿½za": "Puerto Rico,Loiza",
        "Puerto Rico,Mayagï¿½ez": "Puerto Rico,Mayaguez",
        "Puerto Rico,Peï¿½uelas": "Puerto Rico,Penuelas",
        "Puerto Rico,Rincï¿½n": "Puerto Rico,Rincon",
        "Puerto Rico,Rï¿½o grande": "Puerto Rico,Rio Grande",
        "Puerto Rico,Sabana grande": "Puerto Rico,Sabana Grande",
        "Puerto Rico,San lorenzo": "Puerto Rico,San Lorenzo",
        "Puerto Rico,San juan": "Puerto Rico,San Juan",
        "Puerto Rico,San germï¿½n": "Puerto Rico,San German",
        "Puerto Rico,San sebastiï¿½n": "Puerto Rico,San Sebastian",
        "Puerto Rico,Santa isabel": "Puerto Rico,Santa Isabel",
        "Puerto Rico,Trujillo alto": "Puerto Rico,Trujillo Alto",
        "Puerto Rico,Toa alta": "Puerto Rico,Toa Alta",
        "Puerto Rico,Toa baja": "Puerto Rico,Toa Baja",
        "Puerto Rico,Vega alta": "Puerto Rico,Vega Alta",
        "Puerto Rico,Vega baja": "Puerto Rico,Vega Baja",

        # 2020 CENSUS
        "Alaska,Chugach": "Alaska,Valdez-Cordova",
        "Alaska,Copper River": "Alaska,Valdez-Cordova",
        "Alaska,Kusilvak": "Alaska,Wade Hampton",
        "Louisiana,LaSalle": "Louisiana,La Salle",
        "South Dakota,Oglala Lakota": "South Dakota,Shannon",

        # EPA
        "District Of Columbia,District of Columbia": "District of Columbia,District of Columbia",
        "Illinois,La Salle": "Illinois,LaSalle",
        "Illinois,Saint Clair": "Illinois,St. Clair",
        "Maryland,Baltimore (City)": "Maryland,Baltimore City",
        "Minnesota,Saint Louis": "Minnesota,St. Louis",
        "Missouri,Saint Charles": "Missouri,St. Charles",
        "Missouri,Saint Louis": "Missouri,St. Louis County",
        "Missouri,Sainte Genevieve": "Missouri,Ste. Genevieve",
        "New Mexico,Dona Ana": "New Mexico,Doña Ana",
        "Puerto Rico,Mayagnez": "Puerto Rico,Mayaguez",
        "Virginia,Alexandria City": "Virginia,Alexandria",
        "Virginia,Bristol City": "Virginia,Bristol",
        "Virginia,Charles": "Virginia,Charles City",
        "Virginia,Charlottesville City": "Virginia,Charlottesville",
        "Virginia,Chesapeake City": "Virginia,Chesapeake",
        "Virginia,Fredericksburg City": "Virginia,Fredericksburg",
        "Virginia,Hampton City": "Virginia,Hampton",
        "Virginia,Lynchburg City": "Virginia,Lynchburg",
        "Virginia,Newport News City": "Virginia,Newport News",
        "Virginia,Norfolk City": "Virginia,Norfolk",
        "Virginia,Salem City": "Virginia,Salem",
        "Virginia,Suffolk City": "Virginia,Suffolk",
        "Virginia,Virginia Beach City": "Virginia,Virginia Beach",
        "Virginia,Winchester City": "Virginia,Winchester",
        "Virginia,Hopewell City": "Virginia,Hopewell",

        # National County Health Rankings
        "Virginia,Virginia beach city": "Virginia,Virginia Beach",
        "Virginia,Newport news city": "Virginia,Newport News",
        "Virginia,Manassas park city": "Virginia,Manassas Park",
        "Virginia,Falls church city": "Virginia,Falls Church",
        "Virginia,Colonial heights city": "Virginia,Colonial Heights",
        "Virginia,Buena vista city": "Virginia,Buena Vista",
        "South Dakota,Oglala lakota": "South Dakota,Shannon",
        "Alabama,Dekalb": "Alabama,DeKalb",
        "Alabama,St. clair": "Alabama,St. Clair",
        "Alaska,Aleutians east": "Alaska,Aleutians East",
        "Alaska,Aleutians west": "Alaska,Aleutians West",
        "Alaska,Bristol bay": "Alaska,Bristol Bay",
        "Alaska,Fairbanks north star": "Alaska,Fairbanks North Star",
        "Alaska,Kenai peninsula": "Alaska,Kenai Peninsula",
        "Alaska,Ketchikan gateway": "Alaska,Ketchikan Gateway",
        "Alaska,Kodiak island": "Alaska,Kodiak Island",
        "Alaska,Lake and peninsula": "Alaska,Lake and Peninsula",
        "Alaska,Matanuska-susitna": "Alaska,Matanuska-Susitna",
        "Alaska,North slope": "Alaska,North Slope",
        "Alaska,Northwest arctic": "Alaska,Northwest Arctic",
        "Alaska,Prince of wales-outer ketchikan": "Alaska,Prince of Wales-Hyder",
        "Alaska,Prince of wales-hyder": "Alaska,Prince of Wales-Hyder",
        "Alaska,Hoonah-angoon": "Alaska,Hoonah-Angoon",
        "Alaska,Skagway (skagway-hoonah-angoon)": "Alaska,Skagway",
        "Alaska,Hoonah-angoon (skagway-hoonah-angoon)": "Alaska,Hoonah-Angoon",
        "Alaska,Southeast fairbanks": "Alaska,Southeast Fairbanks",
        "Alaska,Valdez-cordova": "Alaska,Valdez-Cordova",
        "Alaska,Wade hampton": "Alaska,Wade Hampton",
        "Alaska,Wrangell (wrangell-petersburg)": "Alaska,Wrangell",
        "Alaska,Petersburg (wrangell-petersburg)": "Alaska,Petersburg",
        "Alaska,Yukon-koyukuk": "Alaska,Yukon-Koyukuk",
        "Arizona,La paz": "Arizona,La Paz",
        "Arizona,Santa cruz": "Arizona,Santa Cruz",
        "Arkansas,Hot spring": "Arkansas,Hot Spring",
        "Arkansas,Little river": "Arkansas,Little River",
        "Arkansas,St. francis": "Arkansas,St. Francis",
        "Arkansas,Van buren": "Arkansas,Van Buren",
        "California,Contra costa": "California,Contra Costa",
        "California,Del norte": "California,Del Norte",
        "California,El dorado": "California,El Dorado",
        "California,Los angeles": "California,Los Angeles",
        "California,San benito": "California,San Benito",
        "California,San bernardino": "California,San Bernardino",
        "California,San diego": "California,San Diego",
        "California,San francisco": "California,San Francisco",
        "California,San joaquin": "California,San Joaquin",
        "California,San luis obispo": "California,San Luis Obispo",
        "California,San mateo": "California,San Mateo",
        "California,Santa barbara": "California,Santa Barbara",
        "California,Santa clara": "California,Santa Clara",
        "California,Santa cruz": "California,Santa Cruz",
        "Colorado,Clear creek": "Colorado,Clear Creek",
        "Colorado,El paso": "Colorado,El Paso",
        "Colorado,Kit carson": "Colorado,Kit Carson",
        "Colorado,La plata": "Colorado,La Plata",
        "Colorado,Las animas": "Colorado,Las Animas",
        "Colorado,Rio blanco": "Colorado,Rio Blanco",
        "Colorado,Rio grande": "Colorado,Rio Grande",
        "Colorado,San juan": "Colorado,San Juan",
        "Colorado,San miguel": "Colorado,San Miguel",
        "Connecticut,New haven": "Connecticut,New Haven",
        "Connecticut,New london": "Connecticut,New London",
        "Delaware,New castle": "Delaware,New Castle",
        "District of Columbia,District of columbia": "District of Columbia,District of Columbia",
        "Florida,Desoto": "Florida,DeSoto",
        "Florida,Indian river": "Florida,Indian River",
        "Florida,Miami-dade": "Florida,Miami-Dade",
        "Florida,Palm beach": "Florida,Palm Beach",
        "Florida,St. johns": "Florida,St. Johns",
        "Florida,St. lucie": "Florida,St. Lucie",
        "Florida,Santa rosa": "Florida,Santa Rosa",
        "Georgia,Ben hill": "Georgia,Ben Hill",
        "Georgia,Dekalb": "Georgia,DeKalb",
        "Georgia,Jeff davis": "Georgia,Jeff Davis",
        "Georgia,Mcduffie": "Georgia,McDuffie",
        "Georgia,Mcintosh": "Georgia,McIntosh",
        "Idaho,Bear lake": "Idaho,Bear Lake",
        "Idaho,Nez perce": "Idaho,Nez Perce",
        "Idaho,Twin falls": "Idaho,Twin Falls",
        "Illinois,Dekalb": "Illinois,DeKalb",
        "Illinois,De witt": "Illinois,De Witt",
        "Illinois,Dupage": "Illinois,DuPage",
        "Illinois,Jo daviess": "Illinois,Jo Daviess",
        "Illinois,Lasalle": "Illinois,LaSalle",
        "Illinois,Mcdonough": "Illinois,McDonough",
        "Illinois,Mchenry": "Illinois,McHenry",
        "Illinois,Mclean": "Illinois,McLean",
        "Illinois,Rock island": "Illinois,Rock Island",
        "Illinois,St. clair": "Illinois,St. Clair",
        "Indiana,Dekalb": "Indiana,DeKalb",
        "Indiana,Lagrange": "Indiana,LaGrange",
        "Indiana,Laporte": "Indiana,LaPorte",
        "Indiana,St. joseph": "Indiana,St. Joseph",
        "Iowa,Black hawk": "Iowa,Black Hawk",
        "Iowa,Buena vista": "Iowa,Buena Vista",
        "Iowa,Cerro gordo": "Iowa,Cerro Gordo",
        "Iowa,Des moines": "Iowa,Des Moines",
        "Iowa,O'brien": "Iowa,O'Brien",
        "Iowa,Palo alto": "Iowa,Palo Alto",
        "Iowa,Van buren": "Iowa,Van Buren",
        "Kansas,Mcpherson": "Kansas,McPherson",
        "Kentucky,Mccracken": "Kentucky,McCracken",
        "Kentucky,Mccreary": "Kentucky,McCreary",
        "Kentucky,Mclean": "Kentucky,McLean",
        "Louisiana,De soto": "Louisiana,De Soto",
        "Louisiana,East baton rouge": "Louisiana,East Baton Rouge",
        "Louisiana,East carroll": "Louisiana,East Carroll",
        "Louisiana,East feliciana": "Louisiana,East Feliciana",
        "Louisiana,Jefferson davis": "Louisiana,Jefferson Davis",
        "Louisiana,La salle": "Louisiana,La Salle",
        "Louisiana,Pointe coupee": "Louisiana,Pointe Coupee",
        "Louisiana,Red river": "Louisiana,Red River",
        "Louisiana,St. bernard": "Louisiana,St. Bernard",
        "Louisiana,St. charles": "Louisiana,St. Charles",
        "Louisiana,St. helena": "Louisiana,St. Helena",
        "Louisiana,St. james": "Louisiana,St. James",
        "Louisiana,St. john the baptist": "Louisiana,St. John the Baptist",
        "Louisiana,St. landry": "Louisiana,St. Landry",
        "Louisiana,St. martin": "Louisiana,St. Martin",
        "Louisiana,St. mary": "Louisiana,St. Mary",
        "Louisiana,St. tammany": "Louisiana,St. Tammany",
        "Louisiana,West baton rouge": "Louisiana,West Baton Rouge",
        "Louisiana,West carroll": "Louisiana,West Carroll",
        "Louisiana,West feliciana": "Louisiana,West Feliciana",
        "Maryland,Anne arundel": "Maryland,Anne Arundel",
        "Maryland,Prince george's": "Maryland,Prince George's",
        "Maryland,Queen anne's": "Maryland,Queen Anne's",
        "Maryland,St. mary's": "Maryland,St. Mary's",
        "Michigan,Grand traverse": "Michigan,Grand Traverse",
        "Michigan,Presque isle": "Michigan,Presque Isle",
        "Michigan,St. clair": "Michigan,St. Clair",
        "Michigan,St. joseph": "Michigan,St. Joseph",
        "Michigan,Van buren": "Michigan,Van Buren",
        "Minnesota,Big stone": "Minnesota,Big Stone",
        "Minnesota,Blue earth": "Minnesota,Blue Earth",
        "Minnesota,Crow wing": "Minnesota,Crow Wing",
        "Minnesota,Lac qui parle": "Minnesota,Lac qui Parle",
        "Minnesota,Lake of the woods": "Minnesota,Lake of the Woods",
        "Minnesota,Le sueur": "Minnesota,Le Sueur",
        "Minnesota,Mcleod": "Minnesota,McLeod",
        "Minnesota,Mille lacs": "Minnesota,Mille Lacs",
        "Minnesota,Otter tail": "Minnesota,Otter Tail",
        "Minnesota,Red lake": "Minnesota,Red Lake",
        "Minnesota,St. louis": "Minnesota,St. Louis",
        "Minnesota,Yellow medicine": "Minnesota,Yellow Medicine",
        "Mississippi,Desoto": "Mississippi,DeSoto",
        "Mississippi,Jefferson davis": "Mississippi,Jefferson Davis",
        "Mississippi,Pearl river": "Mississippi,Pearl River",
        "Missouri,Cape girardeau": "Missouri,Cape Girardeau",
        "Missouri,Dekalb": "Missouri,DeKalb",
        "Missouri,Mcdonald": "Missouri,McDonald",
        "Missouri,New madrid": "Missouri,New Madrid",
        "Missouri,St. charles": "Missouri,St. Charles",
        "Missouri,St. clair": "Missouri,St. Clair",
        "Missouri,Ste. genevieve": "Missouri,Ste. Genevieve",
        "Missouri,St. francois": "Missouri,St. Francois",
        "Missouri,St. louis": "Missouri,St. Louis County",
        "Missouri,St. louis city": "Missouri,St. Louis City",
        "Montana,Big horn": "Montana,Big Horn",
        "Montana,Deer lodge": "Montana,Deer Lodge",
        "Montana,Golden valley": "Montana,Golden Valley",
        "Montana,Judith basin": "Montana,Judith Basin",
        "Montana,Lewis and clark": "Montana,Lewis and Clark",
        "Montana,Mccone": "Montana,McCone",
        "Montana,Powder river": "Montana,Powder River",
        "Montana,Silver bow": "Montana,Silver Bow",
        "Montana,Sweet grass": "Montana,Sweet Grass",
        "Nebraska,Box butte": "Nebraska,Box Butte",
        "Nebraska,Keya paha": "Nebraska,Keya Paha",
        "Nebraska,Mcpherson": "Nebraska,McPherson",
        "Nebraska,Red willow": "Nebraska,Red Willow",
        "Nebraska,Scotts bluff": "Nebraska,Scotts Bluff",
        "Nevada,White pine": "Nevada,White Pine",
        "Nevada,Carson city": "Nevada,Carson City",
        "New Jersey,Cape may": "New Jersey,Cape May",
        "New Mexico,De baca": "New Mexico,De Baca",
        "New Mexico,Dona ana": "New Mexico,Doña Ana",
        "New Mexico,Los alamos": "New Mexico,Los Alamos",
        "New Mexico,Mckinley": "New Mexico,McKinley",
        "New Mexico,Rio arriba": "New Mexico,Rio Arriba",
        "New Mexico,San juan": "New Mexico,San Juan",
        "New Mexico,San miguel": "New Mexico,San Miguel",
        "New Mexico,Santa fe": "New Mexico,Santa Fe",
        "New York,New york": "New York,New York",
        "New York,St. lawrence": "New York,St. Lawrence",
        "North Carolina,Mcdowell": "North Carolina,McDowell",
        "North Carolina,New hanover": "North Carolina,New Hanover",
        "North Dakota,Golden valley": "North Dakota,Golden Valley",
        "North Dakota,Grand forks": "North Dakota,Grand Forks",
        "North Dakota,Lamoure": "North Dakota,LaMoure",
        "North Dakota,Mchenry": "North Dakota,McHenry",
        "North Dakota,Mcintosh": "North Dakota,McIntosh",
        "North Dakota,Mckenzie": "North Dakota,McKenzie",
        "North Dakota,Mclean": "North Dakota,McLean",
        "Ohio,Van wert": "Ohio,Van Wert",
        "Oklahoma,Le flore": "Oklahoma,Le Flore",
        "Oklahoma,Mcclain": "Oklahoma,McClain",
        "Oklahoma,Mccurtain": "Oklahoma,McCurtain",
        "Oklahoma,Mcintosh": "Oklahoma,McIntosh",
        "Oklahoma,Roger mills": "Oklahoma,Roger Mills",
        "Oregon,Hood river": "Oregon,Hood River",
        "Pennsylvania,Mckean": "Pennsylvania,McKean",
        "South Carolina,Mccormick": "South Carolina,McCormick",
        "South Dakota,Bon homme": "South Dakota,Bon Homme",
        "South Dakota,Charles mix": "South Dakota,Charles Mix",
        "South Dakota,Fall river": "South Dakota,Fall River",
        "South Dakota,Mccook": "South Dakota,McCook",
        "South Dakota,Mcpherson": "South Dakota,McPherson",
        "Tennessee,Dekalb": "Tennessee,DeKalb",
        "Tennessee,Mcminn": "Tennessee,McMinn",
        "Tennessee,Mcnairy": "Tennessee,McNairy",
        "Tennessee,Van buren": "Tennessee,Van Buren",
        "Texas,Deaf smith": "Texas,Deaf Smith",
        "Texas,Dewitt": "Texas,DeWitt",
        "Texas,El paso": "Texas,El Paso",
        "Texas,Fort bend": "Texas,Fort Bend",
        "Texas,Jeff davis": "Texas,Jeff Davis",
        "Texas,Jim hogg": "Texas,Jim Hogg",
        "Texas,Jim wells": "Texas,Jim Wells",
        "Texas,La salle": "Texas,La Salle",
        "Texas,Live oak": "Texas,Live Oak",
        "Texas,Mcculloch": "Texas,McCulloch",
        "Texas,Mclennan": "Texas,McLennan",
        "Texas,Mcmullen": "Texas,McMullen",
        "Texas,Palo pinto": "Texas,Palo Pinto",
        "Texas,Red river": "Texas,Red River",
        "Texas,San augustine": "Texas,San Augustine",
        "Texas,San jacinto": "Texas,San Jacinto",
        "Texas,San patricio": "Texas,San Patricio",
        "Texas,San saba": "Texas,San Saba",
        "Texas,Tom green": "Texas,Tom Green",
        "Texas,Val verde": "Texas,Val Verde",
        "Texas,Van zandt": "Texas,Van Zandt",
        "Utah,Box elder": "Utah,Box Elder",
        "Utah,Salt lake": "Utah,Salt Lake",
        "Utah,San juan": "Utah,San Juan",
        "Vermont,Grand isle": "Vermont,Grand Isle",
        "Virginia,Charles city": "Virginia,Charles City",
        "Virginia,Isle of wight": "Virginia,Isle of Wight",
        "Virginia,James city": "Virginia,James City",
        "Virginia,King and queen": "Virginia,King and Queen",
        "Virginia,King george": "Virginia,King George",
        "Virginia,King william": "Virginia,King William",
        "Virginia,New kent": "Virginia,New Kent",
        "Virginia,Prince edward": "Virginia,Prince Edward",
        "Virginia,Prince george": "Virginia,Prince George",
        "Virginia,Prince william": "Virginia,Prince William",
        "Virginia,Buena vista": "Virginia,Buena Vista",
        "Virginia,Colonial heights": "Virginia,Colonial Heights",
        "Virginia,Falls church": "Virginia,Falls Church",
        "Virginia,Manassas park": "Virginia,Manassas Park",
        "Virginia,Newport news": "Virginia,Newport News",
        "Virginia,Virginia beach": "Virginia,Virginia Beach",
        "Washington,Grays harbor": "Washington,Grays Harbor",
        "Washington,Pend oreille": "Washington,Pend Oreille",
        "Washington,San juan": "Washington,San Juan",
        "Washington,Walla walla": "Washington,Walla Walla",
        "West Virginia,Mcdowell": "West Virginia,McDowell",
        "Wisconsin,Eau claire": "Wisconsin,Eau Claire",
        "Wisconsin,Fond du lac": "Wisconsin,Fond du Lac",
        "Wisconsin,Green lake": "Wisconsin,Green Lake",
        "Wisconsin,La crosse": "Wisconsin,La Crosse",
        "Wisconsin,St. croix": "Wisconsin,St. Croix",
        "Wyoming,Big horn": "Wyoming,Big Horn",
        "Wyoming,Hot springs": "Wyoming,Hot Springs",

        # 2000s Census
        "Illinois,La salle": "Illinois,LaSalle",

        # AQIs
        "Canada,New brunswick": "",
        "Canada,Saskatchewan": "",
        "District Of Columbia,District of columbia": "District of Columbia,District of Columbia",
        "Illinois,Saint clair": "Illinois,St. Clair",
        "Maine,Mobile monitors": "",
        "Maryland,Baltimore (city)": "Maryland,Baltimore City",
        "Minnesota,Saint louis": "Minnesota,St. Louis",
        "Missouri,Saint charles": "Missouri,St. Charles",
        "Missouri,Saint louis": "Missouri,St. Louis County",
        "Missouri,Sainte genevieve": "Missouri,Ste. Genevieve",
        "Puerto Rico,Rio grande": "Puerto Rico,Rio Grande",
        "New Mexico,Doï¿½a ana": "New Mexico,Doña Ana",


        # Census CRE
        "Alaska,Copper river": "Alaska,Valdez-Cordova",
        "Louisiana,Lasalle": "Louisiana,La Salle",
        "New Mexico,Doña ana": "New Mexico,Doña Ana",


        # FBI Violence Statistics
        "New Mexico,Zuni Tribal": "New Mexico,Zuni",
        "New Mexico,Ramah Navajo Tribal": "New Mexico,Navajo Nation",
        "New Mexico,Jicarilla Apache Tribal": "New Mexico,Jicarilla Apache Nation",
        "New Mexico,Ohkay Owingeh Tribal": "New Mexico,Ohkay Owingeh",
        "New Mexico,Santa Clara Pueblo": "New Mexico,Santa Clara",
        "New Mexico,Santa Ana Tribal": "New Mexico,Santa Ana",
        "New Mexico,Tesuque Pueblo": "New Mexico,Tesuque",
        "New Mexico,Taos Pueblo": "New Mexico,Taos",
        "New Mexico,Laguna Tribal": "New Mexico,Laguna",
        "New Mexico,Acoma Tribal": "New Mexico,Acoma",
        "New Mexico,Pojoaque Tribal": "New Mexico,Pojoaque",
        "New Mexico,Jemez Pueblo": "New Mexico,Jemez",
        "New Mexico,Isleta Tribal": "New Mexico,Isleta",
        "New Mexico,Mescalero Tribal": "New Mexico,Mescalero",
        "New Mexico,Zia Pueblo": "New Mexico,Zia",

        # Food Resource Environments
        "Indiana,De kalb": "Indiana,DeKalb",
        "Indiana,La porte": "Indiana,LaPorte",
        "Maryland,Prince George": "Maryland,Prince George's",
        "Maryland,Queen anne": "Maryland,Queen Anne's",
        "Maryland,St. Mary": "Maryland,St. Mary's",
        "New Mexico,DeBaca": "New Mexico,De Baca",
        "Pennsylvania,Mc Kean": "Pennsylvania,McKean"
    }

    return countyDictionary.get(location, "N/A")
