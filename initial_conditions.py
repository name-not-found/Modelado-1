import sys

#./dynamic -f archivo.txt
#./dynamic -e ecuacion

def flags():
    file_flag = False
    equation_flag = False
    formulae_str = 'x'

    n = len(sys.argv)
    for i in range(n):
            if "-f" in sys.argv[i]:
                file_flag = True
                filename = sys.argv[i+1]
            if '-e' in sys.argv[i]:
                equation_flag = True
                formulae_str = sys.argv[i+1]

    if file_flag:
        with open(filename) as f:
            formulae = f.readlines()
            formulae_str = formulae[0]
            print("Using archive mode with " + formulae_str)
            return formulae_str
    if equation_flag:
        print("Using equation mode with " + formulae_str)
        return formulae_str