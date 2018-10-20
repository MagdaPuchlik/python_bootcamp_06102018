
#
# zmienne1 = [x/10 for x in range(1,10)]
# print(zmienne1)

zmienne2 = {(x,x**2,x**3) for x in range(-10,10)} #zbior , nie jest po kolei
print(zmienne2)

zmienne2 = [(x,x**2,x**3) for x in range(-10,10)] # lista po kolei
print(zmienne2)

zmienne2 = ((x,x**2,x**3) for x in range(-10,10)) # tupla
print(zmienne2)


zbior_napisow ={'abc','ala','beta'}

print({x:len(x) for x in zbior_napisow})

print([x for x in range(1,101) if x%3==0])
# 0print([[y for y in range(1,101)]]