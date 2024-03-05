def capitalize(string):
    return string.upper()

def capitalize_frst_lttr(string):
    '''
    делает заглавными первые буквы каждого слова в строке, поступившей на вход функции.
    '''
    return "".join(word.capitalize() for word in string.split())
