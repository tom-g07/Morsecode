import os
from sys import platform  # import von main (welches System, clear())
import Morsezeichen_data

# clear funktion
if platform == "linux" or platform == "linux2" or platform == "darwin":
    clear = lambda: os.system('clear')
elif platform == "win32" or platform == "win64" or platform == "cygwin":
    clear = lambda: os.system('cls')
    platform_is_windows = True

def menu_func():
    clear()
    print("Gib bitte an was du übersetzten möchtest.")
    userInput = str(input("übersetzten: "))
    text = str(userInput)

    contains_no_morsecode = text.find("a") >= 0 or text.find("b") >= 0 or text.find("c") >= 0 or text.find("d") >= 0 or text.find("e") >= 0 or text.find("f") >= 0 or text.find("g") >= 0 or text.find("h") >= 0 or text.find("i") >= 0 or text.find("j") >= 0 or text.find("k") >= 0 or text.find("l") >= 0 or text.find("m") >= 0 or text.find("n") >= 0 or text.find("o") >= 0 or text.find("p") >= 0 or text.find("q") >= 0 or text.find("r") >= 0 or text.find("s") >= 0 or text.find("t") >= 0 or text.find("u") >= 0 or text.find("v") >= 0 or text.find("w") >= 0 or text.find("x") >= 0 or text.find("y") >= 0 or text.find("z") >= 0 or text.find("ö") >= 0 or text.find("ä") >= 0 or text.find("ü") >= 0 or text.find(",") >= 0 or text.find(">= 0 or") >= 0 or text.find("?") >= 0 or text.find("!") >= 0 or text.find(":") >= 0 or text.find(";") >= 0 or text.find(")") >= 0 or text.find("'") >= 0 or text.find("=") >= 0 or text.find("(") >= 0 or text.find("&")

    if contains_no_morsecode == -1:
        menu_choice = 2
    else:
        menu_choice = 1

    if menu_choice == 1:
        clear()

        print("Deine Eingabe:")
        print(text)
        print("")
        print("Als Morsecode:")

        verschlüsseln(userInput)
    elif menu_choice == 2:
        clear()

        print("Deine Eingabe:")
        print(text)
        print("")
        print("In Schrift:")

        entschlüsseln(userInput)
    else:
        print("Ein Fehler ist aufgetreten, das von dir genutzte Menü ist nicht vorhanden.")


# funktion zum verschlüsseln
def verschlüsseln(userInput):
    text_changed = userInput.lower()
    text_changed = text_changed.replace("/", Morsezeichen_data.slash)
    text_changed = text_changed.replace("-", Morsezeichen_data.minus)
    text_changed = text_changed.replace(".", Morsezeichen_data.punkt)
    text_changed = text_changed.replace(" ", "/")

    text_encode = text_changed

    text_encode = text_encode.replace("ä", "ae")
    text_encode = text_encode.replace("ö", "oe")
    text_encode = text_encode.replace("ü", "ue")

    text_encode = text_encode.replace("", " ")
    text_encode = text_encode.replace("- . . - .", Morsezeichen_data.slash)
    text_encode = text_encode.replace("- . . . . -", Morsezeichen_data.minus)
    text_encode = text_encode.replace(". - . - . -", Morsezeichen_data.punkt)
    text_encode = text_encode.replace("$", Morsezeichen_data.dollar_zeichen)
    text_encode = text_encode.replace(",", Morsezeichen_data.komma)
    text_encode = text_encode.replace("?", Morsezeichen_data.frage_zeichen)
    text_encode = text_encode.replace("!", Morsezeichen_data.ausrufe_zeichen)
    text_encode = text_encode.replace(":", Morsezeichen_data.doppel_punkt)
    text_encode = text_encode.replace(";", Morsezeichen_data.semi_colon)
    text_encode = text_encode.replace("_", Morsezeichen_data.unter_strich)
    text_encode = text_encode.replace(")", Morsezeichen_data.klammer_zu)
    text_encode = text_encode.replace("'", Morsezeichen_data.anfuehrungs_zeichen)
    text_encode = text_encode.replace("@", Morsezeichen_data.at_zeichen)
    text_encode = text_encode.replace("+", Morsezeichen_data.plus)
    text_encode = text_encode.replace("=", Morsezeichen_data.gleich_zeichen)
    text_encode = text_encode.replace("(", Morsezeichen_data.klammer_auf)
    text_encode = text_encode.replace("&", Morsezeichen_data.und_zeichen)

    text_encode = text_encode.replace("s t a r t", Morsezeichen_data.start, 1)
    if bool(int(text_encode.find("e n d e")) == int(len(text_encode)) - int(len("e n d e")) - 1):
        text_encode = text_encode.replace("e n d e", Morsezeichen_data.ende, 1)

    text_encode = text_encode.replace("a", Morsezeichen_data.a)
    text_encode = text_encode.replace("b", Morsezeichen_data.b)
    text_encode = text_encode.replace("c", Morsezeichen_data.c)
    text_encode = text_encode.replace("d", Morsezeichen_data.d)
    text_encode = text_encode.replace("e", Morsezeichen_data.e)
    text_encode = text_encode.replace("f", Morsezeichen_data.f)
    text_encode = text_encode.replace("g", Morsezeichen_data.g)
    text_encode = text_encode.replace("h", Morsezeichen_data.h)
    text_encode = text_encode.replace("i", Morsezeichen_data.i)
    text_encode = text_encode.replace("j", Morsezeichen_data.j)
    text_encode = text_encode.replace("k", Morsezeichen_data.k)
    text_encode = text_encode.replace("l", Morsezeichen_data.l)
    text_encode = text_encode.replace("m", Morsezeichen_data.m)
    text_encode = text_encode.replace("n", Morsezeichen_data.n)
    text_encode = text_encode.replace("o", Morsezeichen_data.o)
    text_encode = text_encode.replace("p", Morsezeichen_data.p)
    text_encode = text_encode.replace("q", Morsezeichen_data.q)
    text_encode = text_encode.replace("r", Morsezeichen_data.r)
    text_encode = text_encode.replace("s", Morsezeichen_data.s)
    text_encode = text_encode.replace("t", Morsezeichen_data.t)
    text_encode = text_encode.replace("u", Morsezeichen_data.u)
    text_encode = text_encode.replace("v", Morsezeichen_data.v)
    text_encode = text_encode.replace("w", Morsezeichen_data.w)
    text_encode = text_encode.replace("x", Morsezeichen_data.x)
    text_encode = text_encode.replace("y", Morsezeichen_data.y)
    text_encode = text_encode.replace("z", Morsezeichen_data.z)

    text_encode = text_encode.replace("1", Morsezeichen_data.eins)
    text_encode = text_encode.replace("2", Morsezeichen_data.zwei)
    text_encode = text_encode.replace("3", Morsezeichen_data.drei)
    text_encode = text_encode.replace("4", Morsezeichen_data.vier)
    text_encode = text_encode.replace("5", Morsezeichen_data.fuenf)
    text_encode = text_encode.replace("6", Morsezeichen_data.sechs)
    text_encode = text_encode.replace("7", Morsezeichen_data.sieben)
    text_encode = text_encode.replace("8", Morsezeichen_data.acht)
    text_encode = text_encode.replace("9", Morsezeichen_data.neun)
    text_encode = text_encode.replace("0", Morsezeichen_data.null)

    global text_encoded
    text_encoded = "Fehler"
    text_encoded = text_encode.lower()

    if text_encoded.find(" ") == 0:
        text_encoded = text_encoded.replace(" ", "", 1)

    print(text_encoded)

    input("")
    menu_func()


# executable function
def entschlüsseln(userInput):
    global text_decode
    text_decode = userInput

    # Morsecodes mit x Zeichen
    text_decode = text_decode.replace(Morsezeichen_data.ende, "ENDE")
    text_decode = text_decode.replace(Morsezeichen_data.dollar_zeichen, "$")
    text_decode = text_decode.replace(Morsezeichen_data.minus, "€MINUS€")
    text_decode = text_decode.replace(Morsezeichen_data.punkt, "€PUNKT€")
    text_decode = text_decode.replace(Morsezeichen_data.komma, ",")
    text_decode = text_decode.replace(Morsezeichen_data.frage_zeichen, "?")
    text_decode = text_decode.replace(Morsezeichen_data.ausrufe_zeichen, "!")
    text_decode = text_decode.replace(Morsezeichen_data.doppel_punkt, ":")
    text_decode = text_decode.replace(Morsezeichen_data.semi_colon, ";")
    text_decode = text_decode.replace(Morsezeichen_data.unter_strich, "_")
    text_decode = text_decode.replace(Morsezeichen_data.klammer_zu, ")")
    text_decode = text_decode.replace(Morsezeichen_data.anfuehrungs_zeichen, "'")
    text_decode = text_decode.replace(Morsezeichen_data.at_zeichen, "@")
    text_decode = text_decode.replace(Morsezeichen_data.plus, "+")
    text_decode = text_decode.replace(Morsezeichen_data.slash, "€€")
    text_decode = text_decode.replace(Morsezeichen_data.gleich_zeichen, "=")
    text_decode = text_decode.replace(Morsezeichen_data.klammer_auf, "(")
    text_decode = text_decode.replace(Morsezeichen_data.und_zeichen, "&")

    # Morsecodes mit x Zeichen
    text_decode = text_decode.replace(Morsezeichen_data.eins, "1")
    text_decode = text_decode.replace(Morsezeichen_data.zwei, "2")
    text_decode = text_decode.replace(Morsezeichen_data.drei, "3")
    text_decode = text_decode.replace(Morsezeichen_data.vier, "4")
    text_decode = text_decode.replace(Morsezeichen_data.fuenf, "5")
    text_decode = text_decode.replace(Morsezeichen_data.sechs, "6")
    text_decode = text_decode.replace(Morsezeichen_data.sieben, "7")
    text_decode = text_decode.replace(Morsezeichen_data.acht, "8")
    text_decode = text_decode.replace(Morsezeichen_data.neun, "9")
    text_decode = text_decode.replace(Morsezeichen_data.null, "0")
    text_decode = text_decode.replace(Morsezeichen_data.start, "START")

    # Morsecodes mit x Zeichen
    text_decode = text_decode.replace(Morsezeichen_data.x, "x")
    text_decode = text_decode.replace(Morsezeichen_data.y, "y")
    text_decode = text_decode.replace(Morsezeichen_data.z, "z")
    text_decode = text_decode.replace(Morsezeichen_data.p, "p")
    text_decode = text_decode.replace(Morsezeichen_data.q, "q")
    text_decode = text_decode.replace(Morsezeichen_data.l, "l")
    text_decode = text_decode.replace(Morsezeichen_data.j, "j")
    text_decode = text_decode.replace(Morsezeichen_data.h, "h")
    text_decode = text_decode.replace(Morsezeichen_data.f, "f")
    text_decode = text_decode.replace(Morsezeichen_data.b, "b")
    text_decode = text_decode.replace(Morsezeichen_data.v, "v")

    # Morsecodes mit x Zeichen
    text_decode = text_decode.replace(Morsezeichen_data.o, "o")
    text_decode = text_decode.replace(Morsezeichen_data.c, "c")
    text_decode = text_decode.replace(Morsezeichen_data.r, "r")
    text_decode = text_decode.replace(Morsezeichen_data.s, "s")
    text_decode = text_decode.replace(Morsezeichen_data.w, "w")
    text_decode = text_decode.replace(Morsezeichen_data.u, "u")
    text_decode = text_decode.replace(Morsezeichen_data.k, "k")
    text_decode = text_decode.replace(Morsezeichen_data.d, "d")
    text_decode = text_decode.replace(Morsezeichen_data.g, "g")

    # Morsecodes mit 2 Zeichen
    text_decode = text_decode.replace(Morsezeichen_data.i, "i")
    text_decode = text_decode.replace(Morsezeichen_data.m, "m")
    text_decode = text_decode.replace(Morsezeichen_data.n, "n")
    text_decode = text_decode.replace(Morsezeichen_data.a, "a")

    # Morsecodes mit 1 Zeichen
    text_decode = text_decode.replace(Morsezeichen_data.e, "e")
    text_decode = text_decode.replace(Morsezeichen_data.t, "t")

    # spezielle Änderungen die spezifische Lösungen brauchten wie €€ für /
    text_decode = text_decode.replace(" ", "")
    text_decode = text_decode.replace("/", " ")
    text_decode = text_decode.replace("€€", "/")

    text_decode = text_decode.replace("ae", "ä")
    text_decode = text_decode.replace("oe", "ö")
    text_decode = text_decode.replace("ue", "ü")
    text_decode = text_decode.replace("€PUNKT€", ".")
    text_decode = text_decode.replace("€MINUS€", "-")

    global text_decoded
    text_decoded = "Fehler"
    text_decoded = text_decode

    if text_decoded.find(" ") == 0:
        text_decoded = text_decoded.replace(" ", "", 1)

    print(text_decoded)

    input("")
    menu_func()
