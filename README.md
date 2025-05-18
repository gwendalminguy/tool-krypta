# Krypta

Krypta is a simple tool offering several common methods to encrypt or decrypt text messages.

## 📋 Description

...

## 📂 Project Structure

The project contains several files, which are the following:

| Files | Description |
| :---- | :---------- |
| [`methods.py`](https://github.com/gwendalminguy/tool-krypta/blob/main/methods.py) | The python file containing all methods. |
| [`script.py`](https://github.com/gwendalminguy/tool-krypta/blob/main/script.py) | The python file containing the script. |

## ⚙️ Installation

In order to install Krypta, the three steps of this guide must be followed:

**1. Cloning the repository**

To use Krypta, this repository must be cloned locally, using the following command:

```
$ git clone https://github.com/gwendalminguy/tool-krypta.git
```

**2. Setting a virtual environment**

Setting a virtual environment is necessary before installing the requirements, and must be done at the root of the Krypta directory. This will prevent from installing libraries globally, to avoid potential conflicts. It will also help ensure each library is installed with the right version. Setting a virtual environment can be achieved using the following commands:

```
$ cd tool-krypta/
$ python3 -m venv venv
$ source venv/bin/activate
```

**3. Installing the requirements**

In order to work, Krypta needs all the libraries from the `requirements.txt` file. They can be installed with the following command:

```
$ pip install -r requirements.txt
```

## 🖥️ Usage

Krypta can be launched using the following command:

```
$ ./script.py
```

### Methods:

Several methods can be used to encrypt or decrypt a message with Krypta. The currently supported methods and their ... are the following:

| Files | Description |
| :---- | :---------- |
| [`ROT13`](https://en.wikipedia.org/wiki/ROT13) | ... |
| [`Caesar`](https://en.wikipedia.org/wiki/Caesar_cipher) | ... |
| [`Vigenère`](https://en.wikipedia.org/wiki/Vigenère_cipher) | ... |
