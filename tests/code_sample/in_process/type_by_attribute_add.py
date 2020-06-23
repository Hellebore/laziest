def parse_cookie_full(cookie):
    cookiedict = {}
    for chunk in cookie.split(';'):
        key, val = chunk.split('=', 1) if '=' in chunk else ('', chunk)
        key, val = key.strip(), val.strip()
        if key or val:
            cookiedict[key] = val
    return cookiedict
