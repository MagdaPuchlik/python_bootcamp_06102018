import sys


if len(sys.argv)>1:
    adres = sys.argv[1]

    with open(adres) as f:
        i=1
        for line in f:
            print(i,line,end="")
            i +=1
else:
    print("podaje nazwę pliku")

