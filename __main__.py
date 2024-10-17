from . import data_structures

if __name__ == '__main__':
    while True:
        try:
            print(data_structures.truth_table_from_expression(
                *input('Expressions separated by comma: ').split(',')).pretty_string())

        except SyntaxError as e:
            print(e)
