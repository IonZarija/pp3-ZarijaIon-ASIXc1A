"""
Ion Zarija
02/02/2024
ASIXc 1A M03 UF1 PPA
Mida de les PARAULES-mitjana
"""
PLS=333
var, par =[], str
mitjana=0
totVar=0
lPetits=[]
while len(var)!=PLS and par != "\q":
    par=input("Paraula?: ")
    if par != "\q":
        var += [par]
print(var)
for x in range(len(var)):
    totVar += (len(list(var[x])))
mitjana=totVar/len(var)
for x in range(len(var)):
    if (len(list(var[x]))) < mitjana:
        lPetits.append(var[x])
print(f"La mitjana de totes les paraules és: {mitjana}")
print(f"Les paraules més petites que la mitjana són: {lPetits}")
