def przytnij(data, start, stop):

    zbior=[]

    for x in data:
        if x > start:
            zbior.append(x)
        if x == stop:
            break
    return zbior

dane=[1,2,3,4,5]
sta = 2
st = 4
print(przytnij(dane,sta,st))


#sposob z zajec

def przytnij(data, start, stop):

    zbior=[]

    for element in data:
        if start(element):
            zbior.append(element)
        if stop(element):
            break
    return zbior

def test_przytnij():
    assert przytnij(
        data =[1,2,3,4,5,6,7],
        start = lambda x:x>3,
        stop = lambda x:x==6,
    ) == [4,5,6]