import re

class translator():

    def morseToText(str2):
        s2 = str2
        ms = []
        h = " "
        ls2 = list(s2)
        for i in range(0,len(s2)):
            #if ls2[i] ==  " " and i>0 and ls2[i-1] == " ":
            #if ls2[i]    
             #   ms+=" "
              #  continue
            if ls2[i] == " ":
                ms+=" "
                continue
            elif ls2[i]=="-" or ls2[i]==".":
                ms+=ls2[i]
                continue  
        def Focc(e, sr):
            el = list(e)
            se = sr
            nl = []
            for p in range(0,len(el)):
                if(el[p]==se):
                    nl.append(p)
            return nl
        def decode(lang):
        #use switch to decode morse to readable text
            l = lang
            d = []
            sp=Focc(l, " ")
            for t in range(0,len(l)):
                for g in range(0,len(sp)):
                    if t>0 and t==sp[g] and t-1==sp[g]:
                        d.append(" ")
                    

            return 
        return 
        #if(l==)

        #decode morse to text then merge indices its easier
    
    #got the decipher down

        

    
    


        