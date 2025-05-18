# Krypta

Krypta is a simple tool offering several common methods to encrypt or decrypt text messages.

## 📋 Description

...

## 📂 Project Structure

The project contains several files, which are the following:

| Files | Description |
| :---- | :---------- |
| [`methods.py`](https://github.com/gwendalminguy/tool-krypta/blob/main/methods.py) | The module containing functions for all  methods. |
| [`script.py`](https://github.com/gwendalminguy/tool-krypta/blob/main/script.py) | The python file containing the script. |

## ⚙️ Installation

To use Krypta, this repository must be cloned locally, using the following command:

```
$ git clone https://github.com/gwendalminguy/tool-krypta.git
```

## 🖥️ Usage

Krypta can be launched using the following commands:

```
$ cd tool-krypta/
$ ./script.py
```

### Methods:

Several methods can be used to encrypt or decrypt a message with Krypta. The currently supported methods and the way they work are the following:

| Methods | Description |
| :---- | :---------- |
| [`ROT13`](https://en.wikipedia.org/wiki/ROT13) | Shifts each letter of a text by 13 places. |
| [`Caesar`](https://en.wikipedia.org/wiki/Caesar_cipher) | Shifts each letter of a text using a given numeric key. |
| [`Vigenère`](https://en.wikipedia.org/wiki/Vigenère_cipher) | Shifts each letter of a text using a given text key. |
