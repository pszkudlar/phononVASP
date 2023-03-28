import os
import shutil

curdir = os.getcwd()
print(curdir)
for i in os.listdir(curdir):
	if "POSCAR" in i:
		old_path = os.path.join(curdir, i)
		folder_name = i.replace("POSCAR-0", "f")
		new_fol = os.path.join(curdir, folder_name)
		os.mkdir(new_fol)
		new_path = os.path.join(new_fol, "POSCAR")
		shutil.copyfile(old_path, new_path)
print("Pamietaj by zmienic kp, ladunek, ibr, nsw!!!!")