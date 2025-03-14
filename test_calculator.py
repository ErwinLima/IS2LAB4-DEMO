from calculator import  *

def test_suma():
    a, b = 1, 2
    resul =  suma(a,b)
    expected = 3
    assert resul == expected, f"Error: suma({a}, {b}) debería ser {expected}, pero dio {resul}"

def test_resta():
    a, b = 4, 2
    resul = resta(a,b)
    expected = 2
    assert resul == expected, f"Error: resta({a}, {b}) debería ser {expected}, pero dio {resul}"