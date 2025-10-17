import src.main as main_module

def test_main_good_expression():
    main_module.input = lambda: "2 + 3"
    result = main_module.main()  # main() а не mm()
    assert result == 5

def test_main_divide_by_zero():
    main_module.input = lambda: "5 / 0" 
    result = main_module.main()  # main() а не mm()
    assert result == 'Ошибка!'

def test_main_bad_expression():
    main_module.input = lambda: "2 + + 3"
    result = main_module.main()  # main() а не mm()
    assert result == 'Ошибка!'

def test_main_one_number():
    main_module.input = lambda: "42"
    result = main_module.main()  # main() а не mm()
    assert result == 42

def test_main_with_brackets():
    main_module.input = lambda: "(2 + 3) * 4"
    result = main_module.main()  # main() а не mm()
    assert result == 20
