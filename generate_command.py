 import os

folderek = input("Tell me a directory contaibning all the folders with vasprun.xml files: \n")
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
