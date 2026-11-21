def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None


def validate_status(code):
    if 200 <= code < 300:
        return 'success'
    raise ValueError(f'Not success: {code}')


def check_status(code):
    if 200 <= code < 300:
        return 'success'
    elif 300 <= code < 400:
        return 'redirect'
    elif 400 <= code < 500:
        return 'client error'
    elif 500 <= code < 600:
        return 'server error'
    else:
        return 'unknown'

   
if __name__ == '__main__':
    print(safe_int('200'))
    print(safe_int('abc'))
    print(validate_status(200))