from pydbc.readdbc import read_dbc

import pandas as pd
import wget
import os


def test_read_dbc():
    ftp_file = 'ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Dados/RDAC0801.dbc'
    wget.download(ftp_file, 'temp.dbc')
    df = read_dbc('temp.dbc')
    os.unlink('temp.dbc')
    print(df.iloc[:5, [0, 1, 5, 6]])
    assert(type(df) == pd.DataFrame)