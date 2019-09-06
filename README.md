# DYNAMIC SYSTEM SIMULATION

## Python version 3
There are several branches in this repo, each one does something different.
They have a test.sh file with wich you can try what that branch does.

To test the program use:

	:~/sh testing.sh

This program works with the equation __a*x**n+b__.

This program has the following params:
	
   1. The mode: use -f filename to use file mode or -e to use equation mode.

   2. The coeficient or "a", use -a initial_val final_val step
	
   3. The power or "n", use -n initial_val final_val step
	
   4. The constant term or "b", use -b initial_val final_val step
	
   5. The initial conditions, use -x init stop step
	
   6. The number of iterations, use -N number_of_its
