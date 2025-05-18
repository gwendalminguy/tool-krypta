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

Krypta can be launched using the following command:

```
$ ./script.py -a <action> -m <method>
```

The user will be prompted for a text (the message to encrypt or decrypt), then a key (if required by the chosen method). The *caesar* method requires a numeric key, while the *vigenere* method requires a textual key. The text will then be encrypted or decrypted, and the result will be printed to the terminal.

### Action:

Krypta can be used to *encrypt* or *decrypt* a text message. In order to choose the action to execute, it can be called as a command-line argument with **-a** or **--action**, followed by either *encrypt* or *decrypt*. If not specified, the default action is set to be *encrypt*.

### Method:

Several methods can be used to encrypt or decrypt a message with Krypta. In order to choose the method to use, it can be called as a command-line argument with **-m** or **--method**, followed by either *rot13*, *caesar* or *vigenere*. If not specified, the default action is set to be *rot13*. The currently supported methods and the way they work are the following:

| Methods | Description |
| :---- | :---------- |
| [`ROT13`](https://en.wikipedia.org/wiki/ROT13) | Shifts each letter of a text by 13 places. |
| [`Caesar`](https://en.wikipedia.org/wiki/Caesar_cipher) | Shifts each letter of a text using a given numeric key. |
| [`Vigenère`](https://en.wikipedia.org/wiki/Vigenère_cipher) | Shifts each letter of a text using a given textual key. |
