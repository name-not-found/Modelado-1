# DYNAMIC SYSTEM SIMULATION

## Python version 3

There are several branches in this repo, each one does something different.
They have a test.sh file with wich you can try what that branch does.

The branches are:

	master
	Unidad_2


To test the program use:

	:~/sh testing.sh

This program works with the equation __a*x**n+b__.

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
