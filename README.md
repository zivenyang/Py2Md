# Py2Md
> 将python字典转换为Markdown表格
## 示例：
代码示例 *(见demi.py)*：
```python
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
```

输出结果 *(见demo.md)*：
### test_dict_test
|keys|values|
|:--:|:-----|
|dict1|[3, 4]|
|dict2|1|
## test
|keys|values|
|:--:|:-----|
|bool_test|True|
|str_test|hello|
|lsit_test|[1, 2]|
|[dict_test](#test_dict_test)|{'dict1': [3, 4], 'dict2': 1}|
|float_test|0.001|
|int_test|1|


## 环境：
* Python2.X    
* *暂不支持Python3*

## 使用方法：
* 将`py2md`文件夹放入自己的工程文件夹中
* ```python
    from py2md import dict2md
    d2m = dict2md.Dict2table(dictionary, md_path, **augments**)
    d2m.dict2table()
    ```
## 参数：
* **dictionary**: 需要转换的字典
* **md_path**: Markdown文件路径
* **title**: 默认为None, 表格的标题
* **is_subLink**: 默认为False, 是否对字典中的子字典生成子表格, 并为子表格生成一个链接
* **is_chief**: 默认为True, 用于判定是否是主表
* **chief_flag**: 默认为"##", 用于设置主表标题的级别
* **subLink_flag**: 默认为"###", 用于设置子表标题的级别
* **mode**: 默认为"a+", 必须为'a+', 文件打开模式
* **sort**: 默认为"default", 对字典中的keys进行排序,  "default"为字典默认排序, "alphabetical"为按字母表排序,  "r_alphabetical"为按字母表逆排序
* **type_sort**: 默认为None, 对字典中的keys按type进行排序, 必须为None或由's' (for str), 'l' (for list), 'd' (for dict), 'i' (for int), 'f' (for float), 'b' (for bool)组成的字符串
