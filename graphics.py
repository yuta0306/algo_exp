import numpy as np
from tqdm import tqdm

import re
import sys
import os
import subprocess

def change_const(file_name, const_name, const_value):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    lines = [
        re.sub('#define\s{}\s\d+'.format(const_name), 
                '#define {} {}'.format(const_name, const_value),
                line)
            for line in lines
    ]

    with open(file_name, 'w') as f:
        f.writelines(lines)

def select_func(how):
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


def measure_time(how='selection', data_counts=list(range(1000, 11000, 1000)), output_file=None, ext='csv', ):
    if output_file is None:
        output_file = '{}sort'.format(how)
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
    
    f = open('{}.{}'.format(output_file, ext), 'w+')
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

def parse_result(strings):
    nums = re.sub('\D+', ' ', strings)
    nums = [
        num for num in nums.split(' ')
    ]
    rep = int(nums[1])
    data = int(nums[2])
    time = float('.'.join(nums[3:5]))
    result = '{},{}\n'.format(data, time)

    return result

if __name__ == "__main__":
    how = sys.argv[1] if len(sys.argv) > 1 else 'selection'
    measure_time(how=how)