import ast

with open("obekty_tekstowo.txt")as f:
    obiekty= f.read()
    obiekty=ast.literal_eval(obiekty)
    print(type(obiekty))
    print(obiekty)