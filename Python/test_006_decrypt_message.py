from p006_decrypt_message import decrypt_message


def test_no_changes():
    assert decrypt_message("", 0) == ""
    assert decrypt_message("hello", 0) == "hello"


def test_decrypt_negative():
    assert decrypt_message("dpejoh", -1) == "coding"
    assert decrypt_message("rdxyjwntzx", -5) == "mysterious"


def test_decrypt_positive():
    assert decrypt_message("q", 10) == "a"
    assert decrypt_message("qjgbc", 2) == "slide"


def test_decrypt_uppercase():
    assert (
        decrypt_message("XKYARZ JUKY TKKJ ZU HK OT AVVKXIGYK", -6)
        == "RESULT DOES NEED TO BE IN UPPERCASE"
    )
    assert decrypt_message("SCRiX GfJk", 9) == "BLArG PoSt"


def test_abnormal_shifts():
    assert (
        decrypt_message("mabl bl t oxkr vktsr mxlm...", -253)
        == "this is a very crazy test..."
    )
    assert decrypt_message("Jul ner jr qbvat guvf?", 1027) == "Why are we doing this?"
