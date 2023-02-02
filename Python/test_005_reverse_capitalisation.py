from p005_reverse_capitalisation import reverse_capitalisation

def test_empty_string():
    assert reverse_capitalisation('') == ''

def test_single_car():
    assert reverse_capitalisation('a') == 'A'
    assert reverse_capitalisation('K') == 'k'

def test_string():
    assert reverse_capitalisation('abcdefg') == 'ABCDEFG'
    assert reverse_capitalisation('XYZIODPS') == 'xyziodps'

def test_mixed_string():
    assert reverse_capitalisation('AbCdEfGhI') == 'aBcDeFgHi'
    assert reverse_capitalisation('WeLCOMe to ThE JUNGlE') == 'wElcomE TO tHe jungLe'

def test_with_puncutation():
    assert reverse_capitalisation('hello, This iS THE greatest KATA evER!! :)') == 'HELLO, tHIS Is the GREATEST kata EVer!! :)'
    assert reverse_capitalisation('LinUX is... By FAR, the BETTER OpERAting SyStEm. YEAH ***(!!!)') == 'lINux IS... bY far, THE better oPeraTING sYsTeM. yeah ***(!!!)'
    assert reverse_capitalisation('19 is the first happy prime number, 4 is not, and 42 is the answer to everything --- it is!') == '19 IS THE FIRST HAPPY PRIME NUMBER, 4 IS NOT, AND 42 IS THE ANSWER TO EVERYTHING --- IT IS!'


    