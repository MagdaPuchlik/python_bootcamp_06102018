import B

print("jestem w modolue A")

def foo():
    return "moduł foo we modluleA"

print (foo())

#kolejnośc wykjonywania:
    #  najpierw import, a w imporcie mamy
        # import A (czyliwykonywane jest A)
        # wykonywane B (nadal w imporcie)
    # wykonywane jest to co jest w tym module czyli moduł A



