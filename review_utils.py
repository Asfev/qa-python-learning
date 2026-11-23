def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None
    

def classify_response(code):
    if code == 0:
        return 'no_response'
    elif 200 <= code < 300:
        return 'ok'
    elif 300 <= code < 400:
        return 'redirect'
    elif 400 <= code < 500:
        return 'client_error'
    elif 500 <= code < 600:
        return 'server_error'
    else:
        return 'unknown'
    
if __name__ == '__main__':
    print(safe_int('abc'))
    print(classify_response(200))