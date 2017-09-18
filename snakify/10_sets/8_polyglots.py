# Each student at a certain school speaks a number of languages.
# We need to determine which languages are spoken by all the students,
# which languages are spoken by at least one student.
# Given, the number of students, and then for each student
# given the number of languages they speak followed by the name
# of each language spoken, find and print the number of languages spoken
# by all the students, followed by a list the languages by name,
# then print the number of languages spoken by at least one student,
# followed by the list of the languages by name. Print the languages in alphabetical order.

# all_languages = [{input() for j in range(int(input()))} for i in range(int(input()))]
# print(all_languages)

#обозначения *args и **kwargs распаковывают коллекцию и передают ее элементы в функцию.
# распаковка списка:
# https://djangofan.ru/args-kwargs-python
#https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html

import copy
set_temp = set()
list_language = []
for i in range(int(input())):
    for j in range(int(input())):
        set_temp.add(input())
    list_language.append(copy.deepcopy(set_temp))
    set_temp.clear()

all_languages = set.intersection(*list_language)
one_languages = set.union(*list_language)

#output:
print(len(all_languages))
for i in sorted(all_languages):
    print(i)

print(len(one_languages))
for i in sorted(one_languages):
    print(i)












