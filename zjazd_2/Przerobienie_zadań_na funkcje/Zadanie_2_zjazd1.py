def pole_trapezu(a,b,h):

    pole =0

    pole = (a*b)*h/2
    return pole

def test_pole_trapezu():
    assert pole_trapezu(3,9,2)==27




