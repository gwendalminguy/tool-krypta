#!./venv/bin/python3
import sys
import argparse
import customtkinter
rot13 = __import__('methods').rot13
caesar = __import__('methods').caesar
vigenere = __import__('methods').vigenere


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", default="CLI", type=str, help="interface to use")
    args = parser.parse_args()
    interface = (args.interface).upper()

    if interface == "CLI":
        CLI()
    elif interface == "GUI":
        GUI()
    else:
        sys.exit("Interface must be either CLI or GUI")


def CLI():
    text = input("Text: ").strip()
    while True:
        method = input("Method: ([R]OT13 ; [C]AESAR ; [V]IGENERE) ").strip().lower()
        if method not in "rcv":
            print("Please choose one of the supported methods.")
            continue
        elif method == 'r':
            key = 0
            action = 0
        else:
            key = input("Key: ")
            action = input("Method: ([E]NCRYPT ; [D]ECRYPT) ").strip().lower()
            if action == 'e':
                action = 1
            elif action == 'd':
                action = -1
            else:
                continue
        break

    print(krypta(method, text, key, action))


def GUI():
    app = customtkinter.CTk()
    app.mainloop()
    print("Upcoming")


def krypta(method, text, key, action):
    """
    Encrypts or decrypts a text using a given method and key.

    Parameters:
    method (str):
    text (str):
    key (str):
    action (int):

    Return: the resulting string
    """
    if method == 'r':
        return rot13(text)
    elif method == 'c':
        key = int(key)
        return caesar(text, key, action)
    elif method == 'v':
        return vigenere(text, key, action)


if __name__ == "__main__":
    main()
