# import os
# x = os.system("dir") #wywołanie ściezki folderów
# y=os.system("ipconfig") #adres IP
# print(y)
# print(x)
#
#
# x = os.popen("ipconfig").read()
# print(x)

#otwieranie innych aplikaci


import subprocess
p = subprocess.Popen("notepad.exe")

    #p.terminate() z konsoli pythona powoduje zamknięcie otwartej aplikacji

print("xxxxx")
