import mi_modulo as mm

def test_saludar():
    assert mm.saludar() == 'Hola mundo'

def test_sumar():
    assert mm.sumar(3, 5) == 8
    assert mm.sumar(-1, 110) == 109
