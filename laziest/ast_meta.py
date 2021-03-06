import _ast

# TODO: need order by popularity
stnd_types = [str, int, list, dict, tuple, set, float, bool]

iterated = {_ast.List: list,
            _ast.Set: set,
            _ast.Tuple: tuple}


simple = [_ast.Str, _ast.Num]

data_types = [x for x in iterated.keys()] + simple

simple_types = [str, int, float]

ops_pairs = {
    '==': '!=',
    '>': '<=',
    '>=': '<',
    '!=': '==',
    '<=': '>',
    '<': '>=',
    'not': '',
    '': 'not',
    'in': 'not in',
    'not in': 'in'
}

operators = {
    _ast.Eq: '==',
    _ast.GtE: '>=',
    _ast.Gt: '>',
    _ast.LtE: '<=',
    _ast.Lt: '<',
    _ast.Div: '/',
    _ast.Mult: '*',
    _ast.Add: '+',
    _ast.Sub: '-',
    _ast.UAdd: '+=',
    _ast.USub: '-=',
    _ast.Pow: '**',
    _ast.Mod: '%',
    _ast.FloorDiv: '//',
    _ast.LShift: '<<',
    _ast.RShift: '>>',
    _ast.BitOr: '|',
    _ast.BitAnd: '&',
    _ast.BitXor: '^',
    _ast.Or: 'or',
    _ast.And: 'and'
    }

values_for_ast_type = {
    _ast.List: 'elts',
    _ast.Set: 'elts',
    _ast.Tuple: 'elts',
    _ast.Str: 's',
    _ast.Num: 'n'
}

empty_types = {
    str: '',
    None: None,
    list: [],
    dict: dict(),
    set: set([]),
    tuple: tuple()
}
