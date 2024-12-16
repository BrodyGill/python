import re

test = input("test: ")
spa = re.findall(" ", test)
lspa = len(list(map(str, spa)))
print(lspa)