from funcs import *
from graphics import *

def expA_1():
    directory_checker(['output', 'A-1'])
    methods = ['selection', 'insertion', 'heap', 'quick', 'merge']
    filenames = [
        measure_time(method, top='output/A-1')
            for method in methods
    ]

    datas = load_csv(files=filenames)
    create_img(datas, save=True, fname='output/A-1/graph')

def expA_2():
    directory_checker(['output', 'A-2'])
    methods = ['heap', 'quick', 'merge']
    filenames = [
        measure_time(method, top='output/A-2')
            for method in methods
    ]

    datas = load_csv(files=filenames)
    create_img(datas, save=True, fname='output/A-2/graph')

def expB_1():
    directory_checker(['output', 'B-1'])
    methods = ['selection' for _ in range(3)]
    types_bool = [None, True, False]
    types = ['random', 'ascending', 'descending']
    filenames = [
        measure_time(method, ascending=ascending, output_file=f'{method}_{type_name}', top='output/B-1')
            for method, ascending, type_name in zip(methods, types_bool, types)
    ]

    datas = load_csv(files=filenames)
    create_img(datas, save=True, fname='output/B-1/graph')

def expB_2():
    directory_checker(['output', 'B-2'])
    methods = ['insertion' for _ in range(3)]
    types_bool = [None, True, False]
    types = ['random', 'ascending', 'descending']
    filenames = [
        measure_time(method, ascending=ascending, output_file=f'{method}_{type_name}', top='output/B-2')
            for method, ascending, type_name in zip(methods, types_bool, types)
    ]

    datas = load_csv(files=filenames)
    create_img(datas, save=True, fname='output/B-2/graph')

def expB_3():
    directory_checker(['output', 'B-3'])
    methods = ['heap' for _ in range(3)]
    types_bool = [None, True, False]
    types = ['random', 'ascending', 'descending']
    filenames = [
        measure_time(method, ascending=ascending, output_file=f'{method}_{type_name}', top='output/B-3')
            for method, ascending, type_name in zip(methods, types_bool, types)
    ]

    datas = load_csv(files=filenames)
    create_img(datas, save=True, fname='output/B-3/graph')

def expB_4():
    directory_checker(['output', 'B-4'])
    methods = ['merge' for _ in range(3)]
    types_bool = [None, True, False]
    types = ['random', 'ascending', 'descending']
    filenames = [
        measure_time(method, ascending=ascending, output_file=f'{method}_{type_name}', top='output/B-4')
            for method, ascending, type_name in zip(methods, types_bool, types)
    ]

    datas = load_csv(files=filenames)
    create_img(datas, save=True, fname='output/B-4/graph')

def expC_1():
    directory_checker(['output', 'C-1'])
    methods = ['quick' for _ in range(3)]
    types_bool = [None, True, False]
    types = ['random', 'ascending', 'descending']
    filenames = [
        measure_time(method, ascending=ascending, q_type='rand', output_file=f'{method}_{type_name}', top='output/C-1')
            for method, ascending, type_name in zip(methods, types_bool, types)
    ]

    datas = load_csv(files=filenames)
    create_img(datas, save=True, fname='output/C-1/graph')

def expC_2():
    directory_checker(['output', 'C-2'])
    methods = ['quick' for _ in range(3)]
    types_bool = [None, True, False]
    types = ['random', 'ascending', 'descending']
    filenames = [
        measure_time(method, ascending=ascending, q_type='middle', output_file=f'{method}_{type_name}', top='output/C-2')
            for method, ascending, type_name in zip(methods, types_bool, types)
    ]

    datas = load_csv(files=filenames)
    create_img(datas, save=True, fname='output/C-2/graph')

def expC_3():
    directory_checker(['output', 'C-3'])
    methods = ['quick' for _ in range(3)]
    types_bool = [None, True, False]
    types = ['random', 'ascending', 'descending']
    filenames = [
        measure_time(method, ascending=ascending, q_type='mrand', output_file=f'{method}_{type_name}', top='output/C-3')
            for method, ascending, type_name in zip(methods, types_bool, types)
    ]

    datas = load_csv(files=filenames)
    create_img(datas, save=True, fname='output/C-3/graph')

def expC_4():
    directory_checker(['output', 'C-4'])
    methods = ['quick' for _ in range(3)]
    types_bool = [None, True, False]
    types = ['random', 'ascending', 'descending']
    filenames = [
        measure_time(method, ascending=ascending, q_type='left', output_file=f'{method}_{type_name}', top='output/C-4')
            for method, ascending, type_name in zip(methods, types_bool, types)
    ]

    datas = load_csv(files=filenames)
    create_img(datas, save=True, fname='output/C-4/graph')

def expC_5():
    directory_checker(['output', 'C-5'])
    methods = ['quick' for _ in range(3)]
    types_bool = [None, True, False]
    types = ['random', 'ascending', 'descending']
    filenames = [
        measure_time(method, ascending=ascending, q_type='rigth', output_file=f'{method}_{type_name}', top='output/C-5')
            for method, ascending, type_name in zip(methods, types_bool, types)
    ]

    datas = load_csv(files=filenames)
    create_img(datas, save=True, fname='output/C-5/graph')


if __name__ == "__main__":
    import time
    all_ = [expA_1, expA_2, expB_1, expB_2, expB_3, expB_4, expC_1, expC_2, expC_3, expC_4, expC_5]
    for exp in all_:
        print(exp.__name__)
        exp()
        time.sleep(5)