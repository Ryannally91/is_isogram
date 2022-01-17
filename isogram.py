def is_isogram(string):
    mark = 1
    for i in string:
        if i in string[mark:].lower():
            return False
        mark +=1
    return True