# Modeling in Python

To test the program:
	
	:~/sh testing.sh
	
## Unidad_2 Branch
In this branch we added functionality by beign able to evaluate a function and its error as well as accepting parameters to generate a dynamic system simulation, similar to that in branch master.

<<<<<<< HEAD
### Evaluating error 
We added a __noise generator__ wich help us model natural "noise" in a given real-life observated function. 
We are able to compare this observations against a theoretical model by mesuring the error between these two.
=======
There are several branches in this repo, each one does something different.
They have a test.sh file with wich you can try what that branch does.

The branches are:

	master
	Unidad_2

### Branch master: Dynamic system; bacteria growth.

The program shows the possible growth (in gr) of a bacteria colony inside the body against hours (h) using the equation __a*x**n+b__. 

To test the program use:
>>>>>>> 72351e93b7110b8cdd47b78a2660257995d88678

This program has the following additional params:

   1. The __observations file__: use it to model observations stored in a given file. 

   2. The __noise__ or "r". An integer wich indicates de amount of noise to be used. 

   3. The __histogram__ or "-hist". Integer wich indicates bins to be used. Use it if you want to plot a histogram.

   4. The __dynamic__ mode or "d". Use it if you want to model a dynamic system instead of evaluating a function.

All the params used in branch master apply here. 


Usage Example:

<<<<<<< HEAD
	python3 main.py -f formulae.dat -a "4000 4001 1." -b "0 1. 1." -n "1. 2. 1." -x "0 1.75 0.1" -r 20 -histo 20 -o sn_data.txt
=======
This program has the following params:
	
   1. The __mode__: use -f filename to use file mode or -e to use equation mode.
	e.g.
	-f filename 

   2. The __coeficient__ or "a". 
	
   3. The __power__ or "n".
	
   4. The __constant__ term or "b".
	
   5. The __initial__ conditions.
	
   6. The __number__ of iterations.

Example use:
	
	python3 main.py -f formulae.dat -a "2. 3. 1." -b "0. 1. 1." -n "1. 2. 1." -x "1. 11. 1." -N 9
or

	python3 main.py -e a*x**n+b -a "2. 3. 1." -b "0. 1. 1." -n "1. 2. 1." -x "1. 11. 1." -N 9
>>>>>>> 72351e93b7110b8cdd47b78a2660257995d88678
