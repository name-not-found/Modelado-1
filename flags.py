import sys

#./dynamic -f archivo.txt
#./dynamic -e ecuacion

def flags():
    file_flag = False
    equation_flag = False
    formulae_str = 'x'
    a_str = '1'
    b_str = '0'
    n_str = '1'
    x0_str = '1.'
    N = '8'


    n = len(sys.argv)
    for i in range(n):
            if "-f" in sys.argv[i]:
                file_flag = True
                filename = sys.argv[i+1]
            if '-e' in sys.argv[i]:
                equation_flag = True
                formulae_str = sys.argv[i+1]
            if '-a' in sys.argv[i]:
                a_str = sys.argv[i+1]
            if '-b' in sys.argv[i]:
                b_str = sys.argv[i+1]
            if '-n' in sys.argv[i]:
                n_str =sys.argv[i+1]
            if '-x0' in sys.argv[i]:
                x0_str =sys.argv[i+1]
            if '-N' in sys.argv[i]:
                N =sys.argv[i+1]
            

    if file_flag:
        with open(filename) as f:
            formulae = f.readlines()
            formulae_str = formulae[0]
            print("Using archive mode with " + formulae_str)
            return formulae_str
    if equation_flag:
        print("Using equation mode with " + formulae_str)
        return formulae_str, a_str, b_str, n_str, x0_str, N
