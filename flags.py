import sys

#./dynamic -f archivo.txt
#./dynamic -e ecuacion

def flags():
    file_flag = False
    equation_flag = False
    formulae_str = 'x'
    a = '1'
    b = '0'
    n = '1'
    x0 = '1.'
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
                a = float(sys.argv[i+1])
            if '-b' in sys.argv[i]:
                b = float(sys.argv[i+1])
            if '-n' in sys.argv[i]:
                n = float(sys.argv[i+1])
            if '-x0' in sys.argv[i]:
                x0 = float(sys.argv[i+1])
            if '-N' in sys.argv[i]:
                N = int(sys.argv[i+1])
            

    if file_flag:
        with open(filename) as f:
            formulae = f.readlines()
            formulae_str = formulae[0]
            print("Using archive mode with " + formulae_str)
            return formulae_str
    if equation_flag:
        print("Using equation mode with " + formulae_str)
        return formulae_str, a, b, n, x0, N 