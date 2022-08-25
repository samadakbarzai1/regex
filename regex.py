import re

with open('regex_test.txt') as f:
    information = f.readlines()

path = re.compile('([A-Z][a-z]+)\s?([A-Z][a-z]*)?\s?([A-Z][a-z]*)')

for person in path:
    match = path.search(person)
    if match:
        if match.group(2):
            print("\n" f"{match.group(1)} {match.group(2)} {match.group(3)}")
        else:
            print("\n" f"{match.group(1)} {match.group(3)}")

path = re.compile('(\w+), ([A-Za-z]+-)*([A-Za-z]+). *\s(@[a-z]+$)')