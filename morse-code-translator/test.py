import re

test = input("test: ")
#spa = re.findall(" ", test)
#lspa = len(list(map(str, spa)))
#n3 = re.split("", test) 

#ns = re.findall(r"\s", test)
#jb = list(test)
qb = re.findall("^-", test)
print(qb)