import re

class translator():
    
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
        
    
    #got the decipher down
    
    def switch(lang):
        lms = list(lang)
        for j in range(0,len(lang)):
            if lms[j] == 

        