def get_category(age):
    result = None
    
    if age < 6:
        raise ValueError("Age incorrect")
    elif age >= 6 and age < 8:
        result = "Poussin"
    elif age >= 8 and age < 10:
        result = "Pupille"
    elif age >= 10 and age < 12:
        result = "Minime"
    else:
        result = "Cadet"
    
    return result

def run():
    assert get_category(6) == "Poussin"
    assert get_category(7) == "Poussin"
    assert get_category(8) == "Pupille"
    assert get_category(9) == "Pupille"
    assert get_category(10) == "Minime"
    assert get_category(11) == "Minime"
    assert get_category(12) == "Cadet"
    assert get_category(99) == "Cadet"
    
    try:
        get_category(1)
        raise AssertionError()
    except ValueError:
        pass
