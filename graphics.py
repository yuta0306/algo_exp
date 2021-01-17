import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from typing import List, Union
import re

__all__ = [
    'load_csv',
    'create_img',
]

def load_csv(files: List[str]) -> pd.DataFrame:
    datas: Union[pd.DataFrame] = None
    for file in files:
        tmp = pd.read_csv(file)
        tmp.columns = ['data', re.sub("\..+", "", file.split('/')[-1])]
        if datas is None:
            datas = tmp
        else:
            datas = pd.merge(datas, tmp, on='data', how='inner')

    return datas

def create_img(datas: pd.DataFrame, save: bool=False, fname: Union[str]=None):
    for col in datas.drop('data', axis=1).columns.tolist():
        plt.plot(datas['data'], datas[col], 'o-', label=f'{col}')
    plt.xlabel('data')
    plt.ylabel('time')
    plt.legend(loc='best')
    if save:
        if fname is None:
            raise ValueError('You must give fname')
        plt.savefig(fname)

    else:
        plt.show()
    plt.clf()
    plt.close()