def is_num(text):
    try:
        int(text)
    except ValueError:
        return False
    return True
