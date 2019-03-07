def is_pal(string):
    if len(string)<2:
        return True
    if string[0] == string[-1]:
        return is_pal(string[1:-1])  
    else:
        return False
print(is_pal('pass'))
print(is_pal('rotor'))

