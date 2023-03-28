import os
import shutil

curdir = os.getcwd()
folders = []

for i in os.listdir(curdir):
	conpath = os.path.join(curdir,i)
	if os.path.isdir(conpath):
		folders.append(conpath)
export_path = os.path.join(curdir, "export")
os.mkdir(export_path)
for i in folders:
	folder_name = i.split(os.sep)[-1]
	path_to_create = os.path.join(export_path, folder_name)
	print(path_to_create)
	old_path = os.path.join(i, "vasprun.xml")
	os.mkdir(path_to_create)
	new_path = os.path.join(path_to_create, "vasprun.xml")
	try:
		rold = open(old_path, "r")
		vasprun_lines = rold.readlines()
		if "</modeling>" in vasprun_lines[-1]:
			shutil.copyfile(old_path, new_path)
		else:
			print("Calculation wasn't finnished yet in {}.".format(old_path))
	except:
		print("I can't open vaprun.xml file in {}".format(old_path))
