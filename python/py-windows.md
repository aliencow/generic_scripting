## How to use Python’s py launcher for Windows

https://www.infoworld.com/article/3617292/how-to-use-pythons-py-launcher-for-windows.html#:~:text=To%20invoke%20a%20specific%20edition,type%20py%20%2D3.9%2D64%20.


Se instala cuando instalas python para Windows. The py launcher is installed directly into the Windows system directory, so it's always available.

funcionamiento basico.

```bash
py
```
Launches de default version
Result:

```txt
Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

To invoke a specific edition of Python, type py followed by the switch in the left-hand column for the appropriate version. For example:

```bash
py -3.9
```

Results:

```txt
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

To run a Python script with the py launcher, simply substitute py and its command-line switches for python or python3. For instance, here is the command typically used to upgrade pip by running it as a module:

```bash
python -m pip install -U pip
```

If we have the py launcher, we just type (default version):

```bash
python -m pip install -U pip
```

O use a specific version:

```bash
py -3.9 -m pip install -U pip
```