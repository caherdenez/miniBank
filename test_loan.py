from loan import interest,get_cuota

def test_interest():
    # numero completo 0.3414425878159899
    assert interest(110,5,0.25) == 0.341

def test_get_cuota():
    # numero completo 1836.0428231562244
    assert get_cuota(5000,3,0.05) == 1836.0
