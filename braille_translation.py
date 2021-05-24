braille_translation_map = {
    "a": "100000",
    "b": "110000",
    "c": "100100",
    "d": "100110",
    "e": "100010",
    "f": "110100",
    "g": "110110",
    "h": "110010",
    "i": "010100",
    "j": "010110",
    "k": "101000",
    "l": "111000",
    "m": "101100",
    "n": "101110",
    "o": "101010",
    "p": "111100",
    "q": "111110",
    "r": "111010",
    "s": "011100",
    "t": "011110",
    "u": "101001",
    "v": "111001",
    "w": "010111",
    "x": "101101",
    "y": "101111",
    "z": "101011",
    ".": "010011",
    ",": "010000",
    "?": "011001",
    "!": "011010",
    ":": "010010",
    ";": "011000",
    "-": "001001",
    "'": "001000",
}


def translate_string_to_braille(x):
    translation = ""
    if len(x) > 0:
        for char in x:
            if char == " ":
                translation = translation + "000000"
            if char.isupper():
                translation = translation + "000001"
            if char != " ":
                translation = translation + braille_translation_map[char.lower()]
    return translation
