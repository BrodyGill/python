import re

def translate(string1: str):
    str1 = string1
    morseToText(str1)
    #sp = len(list(map(str, re.findall(" ", str1))))
    
def morseToText(str2):
    s2 = str2
    ms = ""
    ls2 = list(s2)
    for i in range(0,len(s2)):
        if ls2[i] ==  " " and ls2[i-1] == " " and i>0:
            ms+=" "
            continue
        elif ls2[i] == " ":
            continue
        if ls2[i]=="-" or ls2[i]==".":
            ms+=ls2[i]
            continue  
    return ms
    #ql = use regex to get text ending at a space 
    #use regex to get double spaces in text use for loop to check
    #for i in sp1:
        