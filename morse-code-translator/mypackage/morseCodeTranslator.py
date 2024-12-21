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
            nstr=""
            sp = Focc(l, " ")
            #p = sp[0]
            #for t in range(0,len(l)):
                #ch=0
                #for g in range(0,len(sp)):
                 #   if t>0 and t==sp[g] and t-1==sp[g]:
                  #      d.append(" ")
                   #     ch=1
                    #elif t==sp[g]:
                     #   ch=1

                #used for fixing spaces
                #if t>0 and l[t]==" " and l[t-1]== " ":
                 #   d.append(" ")
                    #d.pop(t-1)
                #elif l[t]!=" ":
                #   d.append(l[t])
                #elif t>0 or t==len(l)-2:
                #    d[t-1] = [''.join(l[t-2:t])]
                #    d.pop(t-2)
            ch=0
            if(len(sp)>0):
                while(len(sp)>0):
                    d.append([''.join(l[ch:sp[0]])]) 
                    ch=sp[0]+1
                    if(len(sp)==1):
                        lsp = sp[0]
                    sp.pop(0)
                if(d[len(d)-1]!=[''.join(l[lsp:len(l)])]):
                    d.append([''.join(l[lsp+1:len(l)])])
            elif(len(sp)==0):
                d.append([''.join(l[0:len(l)])])
            ns = ''.join(str(d[0]))
            return d
            for y in range(0,len(d)):
                if d[y][0]=="":
                    nstr+= " "
                elif d[y][0]==".-":
                    nstr+="a"
                elif d[y][0]=="-...":
                    nstr+="b"
                elif d[y][0]=="-.-.":
                    nstr+="c"
                elif d[y][0]=="-..":
                    nstr+="d"
                elif d[y][0]==".":
                    nstr+="e"
                elif d[y][0]=="..-.":
                    nstr+="f"
                elif d[y][0]=="--.":
                    nstr+="g"
                elif d[y][0]=="....":
                    nstr+="h"
                elif d[y][0]=="..":
                    nstr+="i"
                elif d[y][0]==".---":
                    nstr+="j"
                elif d[y][0]=="-.-":
                    nstr+="k"
                elif d[y][0]==".-..":
                    nstr+="l"
                elif d[y][0]=="--":
                    nstr+="m"
                elif d[y][0]=="-.":
                    nstr+="n"
                elif d[y][0]=="---":
                    nstr+="o"
                elif d[y][0]==".--.":
                    nstr+="p"
                elif d[y][0]=="--.-":
                    nstr+="q"
                elif d[y][0]==".-.":
                    nstr+="r"
                elif d[y][0]=="...":
                    nstr+="s"
                elif d[y][0]=="-":
                    nstr+="t"
                elif d[y][0]=="..-":
                    nstr+="u"
                elif d[y][0]=="...-":
                    nstr+="v"
                elif d[y][0]==".--":
                    nstr+="w"
                elif d[y][0]=="-..-":
                    nstr+="x"
                elif d[y][0]=="-.--":
                    nstr+="y"
                elif d[y][0]=="--..":
                    nstr+="z"
                elif d[y][0]==".----":
                    nstr+="1"
                elif d[y][0]=="..---":
                    nstr+="2"
                elif d[y][0]=="...--":
                    nstr+="3"
                elif d[y][0]=="....-":
                    nstr+="4"
                elif d[y][0]==".....":
                    nstr+="5"
                elif d[y][0]=="-....":
                    nstr+="6"
                elif d[y][0]=="--...":
                    nstr+="7"
                elif d[y][0]=="---..":
                    nstr+="8"
                elif d[y][0]=="----.":
                    nstr+="9"
                elif d[y][0]=="-----":
                    nstr+="0"
                elif d[y][0]=="..--..":
                    nstr+="?"
                elif d[y][0]=="-.-.--":
                    nstr+="!"
                elif d[y][0]==".-.-.-":
                    nstr+="."
                elif d[y][0]=="--..--":
                    nstr+=","
                elif d[y][0]=="-.-.-.":
                    nstr+=";"
                elif d[y][0]=="---...":
                    nstr+=":"
                elif d[y][0]==".-.-.":
                    nstr+="+"
                elif d[y][0]=="-....-":
                    nstr+="-"
                elif d[y][0]=="-..-.":
                    nstr+="/"
                elif d[y][0]=="-...-":
                    nstr+="="
                else:
                    return "Error: Incorrect Data Entered."
                
            return nstr
            #for y in range(0,len(d)):
             #   nstr+= d[y]
            #return nstr
            #for y in range(0,len(ns)):
             #   ns.index(".")

            #lns = list(ns)
            

            #return nst
            #for y in range(0,len(ns)):
             #   if lns[y]=="[" or lns[y] == "]" or lns[y] == "\'" or lns[y] == ",":
              #     lns.pop(y)
            #for y in range(0,len(ns)):
             #   if map(ns)==
            

        return decode(ms)
        #if(l==)

        #decode morse to text then merge indices its easier
    
    #got the decipher down

        

    
    


        