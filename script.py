#!/usr/bin/python3
import sys
import argparse
rot13 = __import__('methods').rot13
caesar = __import__('methods').caesar
vigenere = __import__('methods').vigenere


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", choices=["encrypt", "decrypt"],
                        default="encrypt", type=str, help="encrypt or decrypt")
    parser.add_argument("-m", "--method", choices=["rot13", "caesar", "vigenere"],
                        default="rot13", type=str, help="method to use")
    args = parser.parse_args()
    action = args.action
    method = args.method

    if action == "encrypt":
        action = 1
    elif action == "decrypt":
        action = -1

    print(krypta(method, action))


def krypta(method, action):
    """
    Encrypts or decrypts a text using a given method.

    Parameters:
    method (str): method to use
    action (int): 1 to encrypt ; -1 to decrypt

    Return: the resulting string
    """
    try:
        text = input("Text: ").strip()
    except EOFError:
        sys.exit("Script Interruption")

    while True:
        if method == "rot13":
            key = None
        else:
            try:
                key = input("Key: ")
            except EOFError:
                sys.exit("Script Interruption")
        if method == "caesar":
            try:
                key = int(key)
            except ValueError:
                print("Invalid Key")
                continue
        break

    if method == 'rot13':
        return rot13(text)
    elif method == 'caesar':
        key = int(key)
        return caesar(text, key, action)
    elif method == 'vigenere':
        return vigenere(text, key, action)


if __name__ == "__main__":
    main()
