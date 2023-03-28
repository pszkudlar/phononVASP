curdir=$(pwd)
echo "$curdir"
for i in $curdir/*
do
if [ -d "$i" ]
then
echo "$i"
cp INCAR $i/INCAR
cp POTCAR $i/POTCAR
cp script.sh $i/script.sh
cp KPOINTS $i/KPOINTS
cd $i
sbatch script.sh
cd ..
fi
done