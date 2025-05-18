#!/usr/bin/python3
import sys
import argparse
rot13 = __import__('methods').rot13
caesar = __import__('methods').caesar
vigenere = __import__('methods').vigenere


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", default="encrypt", type=str, help="encrypt or decrypt")
    args = parser.parse_args()
    action = (args.action).lower()

    if action == "encrypt":
        action = 1
    elif action == "decrypt":
        action = -1
    else:
        sys.exit("Action must be either <encrypt> or <decrypt>")

    try:
        text = input("Text: ").strip()
    except EOFError:
        sys.exit("Script Interruption")

    while True:
        try:
            method = input("Method: ([R]OT13 ; [C]AESAR ; [V]IGÈNERE) ").strip().lower()
        except EOFError:
            sys.exit("Script Interruption")
        if method not in "rcv":
            print("Please choose one of the supported methods.")
            continue
        elif method != 'r':
            key = input("Key: ")
        else:
            key = 0
        break

    print(krypta(method, text, key, action))


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
