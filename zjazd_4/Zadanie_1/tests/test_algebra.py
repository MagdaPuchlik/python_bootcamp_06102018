from mathematica.algebra.matrices import add_matrices,sub_matrices
import pytest

def test1():

    a = [
        [1,2,3],
        [4,5,6],
    ]

    b = [
        [7,8,9],
        [10,11,12],
    ]
    result = add_matrices(a,b)

    assert result == [
        [8,10,12],
        [14,16,18],
    ]

# def test2():
#     assert sub_matrices()==0



def test2():

    a = [
        [1,2,3],
        [4,5,6],
    ]

    b = [
        [7,8,9],
        [10,11,12],
    ]
    result = sub_matrices(a,b)

    assert result == [
        [-6,-6,-6],
        [-6,-6,-6],
    ]