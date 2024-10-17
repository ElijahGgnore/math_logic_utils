from itertools import product

from regex import regex


def truth_table_from_expression(*exps):
    vars_ = list(dict.fromkeys(regex.findall(r'\b[a-zA-Z]\b', exps[0])))
    vars_.sort()
    header = vars_ + list(exps)
    table = []
    for row in product((0, 1), repeat=len(vars_)):
        var_dict = dict(zip(vars_, row))
        table.append(list(row) + [int(eval(e_, var_dict)) for e_ in exps])
    return Table2D(table, header)


class Table2D:
    def __init__(self, table, header=None):
        self.table = table
        self.rows = len(table)
        self.columns = len(table[0])
        self.header: list = header if header else [i for i in range(self.columns)]

    def get_column(self, c):
        return [r[c] for r in self.table]

    def get_transposed(self):
        t = [[] for _ in range(self.columns)]
        for j in range(self.columns):
            for i in range(self.rows):
                t[j].append(self.table[i][j])
        return Table2D(t)

    def pretty_string(self):
        s = ''
        column_sizes = {}
        columns = self.get_transposed()
        for i, c in enumerate(columns.table):
            column_sizes[i] = max([len(str(cell)) for cell in c] + [len(str(self.header[i]))])
        h = ' | '.join(f'{self.header[i]!s:^{column_sizes[i]}}' for i in range(self.columns))
        s += h + '\n' + '-' * len(h) + '\n'
        for r in self.table:
            s += ' | '.join(f'{r[i]!s:^{column_sizes[i]}}' for i in range(self.columns)) + '\n'
        return s

    def __str__(self):
        s = '[' + str(self.header) + '\n ' + '\n '.join(str(r) for r in self.table) + ']'
        return s
