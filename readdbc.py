from _readdbc import ffi, lib
import os
import pandas as pd
from tempfile import NamedTemporaryFile
from dbfread import DBF


def read_dbc(local_file, encoding='utf-8'):
    """
    Opens a .dbc file and return its contents as a pandas
    Dataframe.
    :param filename: .dbc filename
    :param encoding: encoding of the data
    :return: Pandas Dataframe.
    """
    if isinstance(local_file, str):
        filename = local_file.encode()
    with NamedTemporaryFile(delete=False) as tf:
        dbc2dbf(local_file, tf.name.encode())
        dbf = DBF(tf.name, encoding=encoding)
        df = pd.DataFrame(list(dbf))
    os.unlink(tf.name)

    return df


def dbc2dbf(infile, outfile):
    """
    Converts a DATASUS dbc file to a DBF database.
    :param infile: .dbc file name
    :param outfile: name of the .dbf file to be created.
    """
    if isinstance(infile, str):
        infile = infile.encode()
    if isinstance(outfile, str):
        outfile = outfile.encode()
    p = ffi.new('char[]', os.path.abspath(infile))
    q = ffi.new('char[]', os.path.abspath(outfile))

    lib.dbc2dbf([p], [q])

