import re

test = input("test: ")
#spa = re.findall(" ", test)
#lspa = len(list(map(str, spa)))
#n3 = re.split("", test) 

#ns = re.findall(r"\s", test)
#jb = list(test)
#qb = re.findall("^-", test)
def findList(s):
    ls = list(s)
    nst=""
    x=0
    for i in range(0,len(ls)):
        if ls[i]=="-":
            x+=1
            nst+=ls[i]
        if ls[i]==".":
            x+=1
            nst+=ls[i]
        if ls[i]==" ":
            x+=1
    if(x!=len(ls)):
        return "ERROR: Incorrect input ; Only use .'s and -'s"
    lls = re.split("\s", ls)
    wls = re.findall("\s", ls)


print()