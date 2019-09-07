# Modeling in Python

To test the program:
	
	:~/sh testing.sh
	
## Unidad_2 Branch
In this branch we added functionality by beign able to evaluate a function and its error as well as accepting parameters to generate a dynamic system simulation, similar to that in branch master.

### Evaluating error 
We added a __noise generator__ wich help us model natural "noise" in a given real-life observated function. 
We are able to compare this observations against a theoretical model by mesuring the error between these two.

This program has the following additional params:

   1. The __observations file__: use it to model observations stored in a given file. 

   2. The __noise__ or "r". An integer wich indicates de amount of noise to be used. 

   3. The __histogram__ or "-hist". Integer wich indicates bins to be used. Use it if you want to plot a histogram.

   4. The __dynamic__ mode or "d". Use it if you want to model a dynamic system instead of evaluating a function.

All the params used in branch master apply here. 


Usage Example:

	python3 main.py -f formulae.dat -a "4000 4001 1." -b "0 1. 1." -n "1. 2. 1." -x "0 1.75 0.1" -r 20 -histo 20 -o sn_data.txt
