def plus_two(num):
    num += 2
    return num

def test_plus_two_with_debugging(capsys):
    result = None
    with capsys.disabled():
        result = plus_two(5)
    print(result)
