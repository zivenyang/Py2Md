from py2md import dict2md

test_dict = dict(
    str_test="hello",
    lsit_test=[1, 2],
    dict_test={"dict1": [3, 4], "dict2": 1},
    bool_test=True,
    int_test=1,
    float_test=0.001
)

if __name__ == '__main__':
    d2m = dict2md.Dict2table(
        dictionary=test_dict,
        md_path='./demo.md',
        title='test',
        is_subLink=True,
        sort='alphabetical',
        type_sort='bsl'
    )
    d2m.dict2table()
