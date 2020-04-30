import os


def parser(obj, tabs):
    name = type(obj).__name__

    if name == 'bool':
        return 'true' if obj else 'false'
    elif name == 'int':
        return str(obj)
    elif name == 'NoneType':
        return 'NaN' 
    elif name == 'float':
        return parse_number(obj)  
    elif name in ('list', 'tuple'):
        return obj_converter(obj, tabs, False)
    elif name == 'dict':
        return obj_converter(obj, tabs)   
    elif name == 'str':
        return '"{}"'.format(obj)
    raise TypeError()


def parse_number(obj):
    if obj == float('-inf'):
        return '-Infinity'
    if obj == float('inf'):
        return 'Infinity'
    return str(obj)


def obj_converter(obj, tabs, flag = True):
    """ Convert the iterable object to a JSON format string.

        flag: Defines what we parse, a list or a dictionary.

        return: JSON string
    """ 
    tabs += 1
    total = []
    indent = lambda n: '    ' * n
    if flag:
        result = '{\n'
        for k, v in obj.items():
            key = '"{}": '.format(k)
            value = parser(v, tabs)
            total.append(indent(tabs) + key + value)
        return result + ',\n'.join(total) + '\n' + indent(tabs-1) + '}'
    else:
        result = '[\n'
        for v in obj:
            value = parser(v, tabs)
            total.append(indent(tabs) + value)
        return result + ',\n'.join(total) + '\n' + indent(tabs-1) + ']'


def to_json(obj):
    """ Function converts the python object to JSON format
        and writes it to a file.

        return: None
    """
    name = rename('to_json.json')
    with open(name, 'w+') as f:
        tabs = 0
        cond = type(obj).__name__
        if cond == 'dict':
            f.write(obj_converter(obj, tabs))
        else:
            if cond == 'list' or cond == 'tuples':
                f.write(obj_converter(obj, tabs, False))
            else:
                f.write(parser(obj, tabs)) 


def rename(name):
    """ Function renames the file 
        if such a name exists. 

        return: name
    """
    counter = 0 
    while True:
        if os.path.isfile(name):
            counter += 1
            new = name.split('.')
            new[0] += str(counter)
            name = '.'.join(new)
        else:   
            return name 
    

def main():
    data = {"president": {"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}}
    to_json(data)
    print('[READY]')


if __name__ == "__main__":
    main()