
#jeżeli zaimportuję sobie ten moduł własnis wa takiej postaci wówczas przy imporcie zostanie wywołany cały program i zwrócony
#zostanie jego wynik ponieważ mamy tu nie tyko funkcje ale również zmienne i wywołanie (nie tylko defninicję funkcji)





def add_matrices(a,b):
    if len(a)!=len(b) or (len(a[0])!=len(b[0])):
        raise ValueError("Różna ilość wierszy")

    result = []

    for i in range(len(a)):
        new_row=[]
        for j in range(len(a[0])):
            new_row.append(a[i][j]+b[i][j])

        result.append(new_row)
            # war = (((a[i])[j]) + ((b[i])[j]))

    return result

print(add_matrices(a,b))


def sub_matrices(a,b):
    if len(a)!=len(b) or (len(a[0])!=len(b[0])):
        raise ValueError("Różna ilość wierszy")

    result = []

    for i in range(len(a)):
        new_row=[]
        for j in range(len(a[0])):
            new_row.append(a[i][j]-b[i][j])

        result.append(new_row)


    return result

if __name__ == "__main__":
    # main to atrybut skryptu, jeżeli jesteśmy w danym module to ma on nazwę main, jeżeli wywołujemy go z innego modułu
    # wóczas widoczna jest faktyczna nazwa (własna) moduły, czyli dla tego będzie to matrices

    a = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    b = [
        [7, 8, 9],
        [10, 11, 12],
    ]

    print(sub_matrices(a,b))

