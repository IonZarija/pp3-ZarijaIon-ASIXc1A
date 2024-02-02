"""
Ion Zarija
02/02/2024
ASIXc 1A M03 UF1 PPA
PARAULES amb NÚMEROS
"""
frase=str(input("Frase?: ")).lower()
fraseN=list(frase)
res=""
for x in range(len(fraseN)):
    if fraseN[x] == "a":
        res+="1"
    elif fraseN[x] == "e":
        res+="2"
    elif fraseN[x] == "i":
        res+="3"
    elif fraseN[x] == "o":
        res+="4"
    elif fraseN[x] == "u":
        res+="5"
    else:
        res+=frase[x]
print(str(res))
