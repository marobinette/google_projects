import pytest
import braille_translation.braille_translation as bt


def test_lower_case():
    assert bt.translate_string_to_braille("code") == "100100101010100110100010"


def test_upper_and_lower_case():
    assert (
        bt.translate_string_to_braille("Braille")
        == "000001110000111010100000010100111000111000100010"
    )


def test_sentence():
    assert (
        bt.translate_string_to_braille("The quick brown fox jumps over the lazy dog")
        == "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
    )


def test_h():
    assert bt.translate_string_to_braille("h") == "110010"


def test_k():
    assert bt.translate_string_to_braille("k") == "101000"


def test_m():
    assert bt.translate_string_to_braille("m") == "101100"


def test_q():
    assert bt.translate_string_to_braille("q") == "111110"


def test_v():
    assert bt.translate_string_to_braille("v") == "111001"


def test_x():
    assert bt.translate_string_to_braille("x") == "101101"


def test_z():
    assert bt.translate_string_to_braille("z") == "101011"


def test_period():
    bt.translate_string_to_braille(".") == "010011"


def test_period_after_word():
    bt.translate_string_to_braille("cat.") == "100100010011"


def test_comma():
    bt.translate_string_to_braille("but, it") == "110000010000000000010100011110"


def test_question_mark():
    bt.translate_string_to_braille("?") == "011001"


def test_question():
    bt.translate_string_to_braille("What?") == "000001010111110010100000011110011001"


def test_exclamation():
    bt.translate_string_to_braille(
        "What?!"
    ) == "000001010111110010100000011110011001011010"


def test_colon():
    bt.translate_string_to_braille(":") == "010010"


def test_semi_colon():
    bt.translate_string_to_braille(";") == "011000"


def test_dash():
    bt.translate_string_to_braille("-") == "001001"
