import os

folderek = input("Podaj ściezkę do folderu, w którym znajdują się fodlery z kolejnymi singlepointami: \n")
command = "phonopy -f "
for i in os.listdir(folderek):
    con = os.path.join(folderek, i)
    if os.path.isdir(con) and "inne" not in con:
        command += "{}\\vasprun.xml ".format(i)
        for j in os.listdir(con):
            con2 = os.path.join(con, j)
            if "vasprun" not in j:
                os.remove(con2)
print(command)
