# pydbc
Lib to handle .dbc files in python 3.

Inspired from https://github.com/AlertaDengue/PySUS.

## Installing

There are some dependencies which can't be installed through pip, namely `libffi`. Therefore on an ubuntu system:

```
sudo apt install libffi-dev
```

This is my preferred way of sharing/storing/installing packages. Use pip to install it from that repo directly.

```
pip install git+https://github.com/gbletsch/pydbc.git

```

Or if, for some reason, you don't want to use git:

```
pip install https://github.com/gbletsch/pydbc/zipball/master
```


## Example:

The file needs to be saved loccaly.

```python
file = 'RDAC1701.dbc'
df = read_dbc(file)
print(df.iloc[:5, [0, 1, 5, 6])

    UF_ZI ANO_CMPT          N_AIH IDENT
0  120000     2017  1217100012601     1
1  120000     2017  1217100012612     1
2  120000     2017  1217100012667     1
3  120000     2017  1216100555406     1
4  120000     2017  1216100555428     1
```
