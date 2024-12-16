import re

def translate(string1: str):
    str1 = string1
    sp = len(list(map(str, re.findall(" ", str1))))
    
def morseToText(s2, spaces1):
    str2 = s2
    sp1 = spaces1
    al = ""
    #ql = use regex to get text ending at a space 
    #for i in sp1:
        