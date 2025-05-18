#!/usr/bin/python3

"""
Module containing functions to encrypt and decrypt messages.
Supported methods: ROT13 ; Caesar ; ...
"""


def main():
    text = input("Text: ").strip()
    method = input("Method: ([R]OT13 / [C]AESAR) ").strip().lower()
    if method == 'r':
        print(rot13(text))
    else:
        key = input("Key: ")
        action = input("Method: ([E]NCRYPT / [D]ECRYPT) ").strip().lower()
        if action == 'e':
            action = 1
        elif action == 'd':
            action == -1
        if method == 'c':
            key = int(key)
            print(caesar(text, key, action))


def rot13(text):
    """
    Encrypts or decrypts a text using ROT13.

    Parameters:
    text (str): text to encrypt or decrypt

    Return: the resulting string
    """
    result = ""
    for char in text:
        if 65 <= ord(char) <= 77 or 97 <= ord(char) <= 109:
            char = chr(ord(char) + 13)
        elif 78 <= ord(char) <= 90 or 110 <= ord(char) <= 122:
            char = chr(ord(char) - 13)
        result += char

    return result


def caesar(text, key, action):
    """
    Encrypts or decrypts a text using Caesar method.

    Parameters:
    text (str): text to encrypt or decrypt
    key (int): key to use
    action (int): 1 to encrypt ; -1 to decrypt

    Return: the resulting string
    """
    key = action * (key % 26)
    result = ""
    for char in text:
        if 65 <= ord(char) <= 90:
            char = chr(ord(char) + key)
            if ord(char) > 90:
                char = chr(ord(char) - 26)
            elif ord(char) < 65:
                char = chr(ord(char) + 26)
        elif 97 <= ord(char) <= 122:
            char = chr(ord(char) + key)
            if ord(char) > 122:
                char = chr(ord(char) - 26)
            elif ord(char) < 97:
                char = chr(ord(char) + 26)
        result += char

    return result


if __name__ == "__main__":
    main()
