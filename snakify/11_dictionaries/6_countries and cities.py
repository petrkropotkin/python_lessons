# Given a list of countries and cities of each country.
# Then given the names of the cities. For each city specify the country in which it is located.

# ========input==========
"""
2
USA Boston Pittsburgh Washington Seattle
UK London Edinburgh Cardiff Belfast
3
Cardiff
Seattle
London
"""

# ------output----------
# UK
# USA
# UK

country_dict = {}
for i in range(int(input())):
    country,*cities = input().split()
    country_dict[country] = set(cities)
#{'USA': {'Washington', 'Boston', 'Pittsburgh', 'Seattle'}, 'UK': {'Cardiff', 'London', 'Belfast', 'Edinburgh'}}
for i in range(int(input())):
    city = input()
    for country in country_dict:
        if city in country_dict[country]:
            print(country)

# =========suggested solution===============

motherland = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        motherland[city] = country

for i in range(int(input())):
    print(motherland[input()])