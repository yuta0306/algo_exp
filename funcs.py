import numpy as np
from tqdm import tqdm

import re
import sys
import os
import subprocess

from typing import List, Any, NoReturn, Iterable, Union

__all__ = [
    'measure_time',
    'directory_checker'
]


def directory_checker(dirnames: List[str]) -> NoReturn:
    path = '.'
    for dir_name in dirnames:
        path += f'/{dir_name}'
        if not os.path.isdir(path):
            os.makedirs(path, exist_ok=True)


def change_const(file_name: str, const_name: str, const_value: Any) -> NoReturn:
    with open(file_name, 'r') as f:
        lines: List[str] = f.readlines()

    lines = [
        re.sub('#define\s{}\s\d+'.format(const_name), 
                '#define {} {}'.format(const_name, const_value),
                line)
            for line in lines
    ]

    with open(file_name, 'w') as f:
        f.writelines(lines)


def input_type(file_name: str, ascending: Union[bool]=None) -> NoReturn:
    if ascending is None:
        funcname = 'data_random'
    elif ascending:
        funcname = 'data_ascending'
    else:
        funcname = 'data_descending'

    with open(file_name, 'r') as f:
        lines: List[str] = f.readlines()

    lines = [
        re.sub('data_', '// data_', line) if re.search('\s\s+data_', line) else line
            for line in lines
    ]
    lines = [
        re.sub(f'// {funcname}', funcname, line) for line in lines
    ]

    with open(file_name, 'w') as f:
        f.writelines(lines)


def quick_type(file_name: str, type_: str='rand') -> NoReturn:
    with open(file_name, 'r') as f:
        lines: List[str] = f.readlines()

    lines = [
        re.sub('".+"', f'"{type_}"', line) if re.search('quicksort', line) else line
            for line in lines
    ]

    with open(file_name, 'w') as f:
        f.writelines(lines)


def select_func(how: str) -> NoReturn:
    if how == 'selection':
        cfile = 'algo5-1.c'
    elif how == 'insertion':
        cfile = 'algo5-2.c'
    elif how == 'heap':
        cfile = 'algo5-5.c'
    elif how == 'quick':
        cfile = 'algo6-1.c'
    elif how == 'merge':
        cfile = 'algo7-3.c'
    else:
        raise ValueError()

    if how == 'heap':
        how = '_heap'
    elif how == 'merge':
        how = '_mearge'

    with open('sort-main.c', 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if re.search('sort', line):
            splited = re.split('\s', line)
            splited = [c for c in splited if not re.match('//', c)]
            altered = [
                '// {}'.format(c) if re.search('sort\(', c)
                else c
                    for i, c in enumerate(splited)  
            ]
            line = ' '.join(altered)
            line = line[0:]
            line += '\n'
        new_lines.append(line)
    lines = [
        re.sub('//\s', '', line)[0:]
            if re.search('{}sort'.format(how), line)
            else line
                for line in new_lines
    ]

    with open('sort-main.c', 'w') as f:
        f.writelines(lines)


def measure_time(how: str='selection', data_counts: Iterable=list(range(1000, 21000, 500)),
                ascending: Union[bool]=None, q_type: str='rand', output_file: Union[str]=None,
                ext: str='csv', top: Union[str]=None) -> str:
    if output_file is None:
        output_file = '{}sort'.format(how)
    if top is None:
        top = './'
    else:
        if not top[-1] == '/':
            top += '/'

    if how == 'selection':
        cfile = 'algo5-1.c'
    elif how == 'insertion':
        cfile = 'algo5-2.c'
    elif how == 'heap':
        cfile = 'algo5-5.c'
    elif how == 'quick':
        cfile = 'algo6-1.c'
        quick_type('sort-main.c', q_type)
    elif how == 'merge':
        cfile = 'algo7-3.c'
    else:
        raise ValueError()

    input_type('sort-main.c', ascending=ascending)
    
    f = open('{}{}.{}'.format(top, output_file, ext), 'w+')
    f.write('data,time\n')

    for i in tqdm(data_counts):
        change_const('sort.h', 'N', i)
        select_func(how=how)
        subprocess.run(['cc', 'sort-main.c', 'sort-funcs.c', cfile, '-o', 'sort-main'])
        res = subprocess.run(['./sort-main'], stdout=subprocess.PIPE)
        output = res.stdout.decode('utf-8')
        output = parse_result(output)
        f.write(output)
    f.close()

    return '{}{}.{}'.format(top, output_file, ext)


def parse_result(strings: str) -> str:
    nums = re.sub('\D+', ' ', strings)
    nums = [
        num for num in nums.split(' ')
    ]
    rep = int(nums[1])
    data = int(nums[2])
    time = float('.'.join(nums[3:5]))
    result: str = '{},{}\n'.format(data, time)

    return result
