from pydbc.readdbc import read_dbc
import pandas as pd

def test_read_dbc():
    file = '/home/gui/tcc_hemato_sus/raw_data_teste/RDAC1701.dbc'
    df = read_dbc(file)
    assert(type(df) == pd.DataFrame)