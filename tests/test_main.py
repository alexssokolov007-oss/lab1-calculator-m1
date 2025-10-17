import main

def fake_input(text):
    return text

def test_main_well-well_expression():
    main.input = lambda: "2 + 3"
    result = main.main()
    assert result == 5

def test_main_divide_by_zero():
    main.input = lambda: "5 / 0" 
    result = main.main()
    assert result == 'Ошибка!'

def test_main_bad_expression():
    main.input = lambda: "2 + + 3"
    result = main.main()
    assert result == 'Ошибка!'

def test_main_one_number():
    main.input = lambda: "42"
    result = main.main()
    assert result == 42

def test_main_with_brackets():
    main.input = lambda: "(2 + 3) * 4"
    result = main.main()
    assert result == 20
