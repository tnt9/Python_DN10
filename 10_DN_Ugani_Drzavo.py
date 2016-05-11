import random
from datetime import datetime
city_country = {"VIENNA": "Austria", "BRUSSELS": "Belgium", "SOFIA": "Bulgaria",
                "NICOSIA": "Cyprus", "PRAGUE": "Czech Republic", "COPENHAGEN": "Denmark",
                "TALLINN": "Estonia", "HELSINKI": "Finland", "PARIS": "France",
                "ATHENS": "Greece", "ZAGREB": "Croatia", "DUBLIN": "Ireland",
                "ROME": "Italy", "RIGA": "Latvia", "VILNIUS": "Lithuania",
                "LUXEMBOURG": "Luxembourg", "BUDAPEST": "Hungary",
                "VALLETTA": "Malta", "BERLIN": "Germany", "AMSTERDAM": "Netherlands",
                "WARSAW": "Poland", "LISBON": "Portugal", "BUCHAREST":
                "Romania", "BRATISLAVA": "Slovakia", "LJUBLJANA": "Slovenia",
                "MADRID": "Spain", "STOCKHOLM": "Sweden", "LONDON": "United Kingdom"}

n = 0
c = 0
correct = []
wrong = []
keys = city_country.keys()
random.shuffle(keys)

for key in keys:
    country = city_country[key]
    print "Name the Capital of",  country
    city = raw_input("Capital is ")
    if city.upper() == key:
        print "Correct!"
        c = c + 1
        correct.append(country)
    else:
        print "NOUP, the capital is", key
        n = n + 1
        wrong.append(country)
a = n + c
print "correct answers = ", c
print (correct)
print "wrong answered = ", n
print (wrong)
print "total answers = ", a




