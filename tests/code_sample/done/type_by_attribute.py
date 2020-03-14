def split_line(line):
    return line.split()


def index_line(array, elem):
    return array.index(elem)


def split_by_symbol(line, symbol):
    return line.split(symbol)


def parse_cookie(cookie):
    for chunk in cookie.split(';'):
        key, val = chunk.split('=', 1) if '=' in chunk else ('', chunk)
    return key, val
