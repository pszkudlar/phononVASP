# phononVASP
After I create tilted geometries, I use <b>fol_ph.py</b> to place those POSCARS in separate folders.<br>
After thet, I copy INCAR, KPOINTS, POTCAR  and script.sh to the folder with all singlepoints folders and modify them.<br>
Then I run <b>copy_and_run.py</b>.<br>
If I want to check if all the calculations are done, I simply run <b>exp_ph.py</b>. If calcutions are done, script. will only print directories of those singlepoint calculations.<br>
I copy those folders to my directory where <b>phonopy_disp.yaml</b> is.
I copy the directory and paste iit to the script that genereates the command.
I run  this command in phonopy.
