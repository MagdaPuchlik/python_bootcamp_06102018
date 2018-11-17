import sys

if len(sys.argv)>1:
    print("hello",sys.argv[1])
else:
    print("hello world")

input() #input powoduje że jest to plik exe, bez tego jest to format spec

#polecenie do wpisania w terminalu (muszę się znajdować w aktualnym module)
# pyinstaller --onefile [nazwa pliku do uruchomienia]