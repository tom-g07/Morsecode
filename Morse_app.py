from Morsezeichen import clear
from Morsezeichen import menu_func

def startscreen():
    # Startscreen
    clear()

    print("Willkommen beim Morsecodierer!")
    print("")
    print(".-- .. .-.. .-.. -.- --- -- -- . -.")
    input("")

    # Hinweibildschirm
    clear()
    print("Notizen".upper())
    print("")
    print("Die Ausgabe in Morsecode:")
    print("/ -> Wortrennung")
    print("- -> lang")
    print(". -> kurz")
    print("' -> Anführungszeichen")
    print("Umlaute werden ausgeschrieben (ä->ae)")
    print("")
    print("Wie du schreiben musst:")
    print("PUNKT -> .")
    print("MINUS -> -")
    print("Anführungszeichen -> '")
    print("start, ende (für start und ende)")
    input("")

    menu_func()

startscreen()