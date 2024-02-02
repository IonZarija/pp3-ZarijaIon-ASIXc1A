"""
Ion Zarija
02/02/2024
ASIXc 1A M03 UF1 PPA
MATRIU H
"""

try:
    matriu=[]
    files = int(input("Quantes files?: "))
    columnes=int(input("Quantes columnes?: "))
    while files != columnes or files % 2 == 0 or columnes % 2 == 0:
        files = int(input("Quantes files2: "))
        columnes = int(input("Quantes columnes?: "))
    matriu = [[0]*columnes for i in range(files)]
    for i in range(files):
        for j in range(columnes):
            if j==0 or j==columnes-1 or i==(files//2):
                matriu[i][j]=1
    for fila in matriu:
        for c in fila:
            print(c, end=" ")
        print()

except ValueError:
    print("ERROR")