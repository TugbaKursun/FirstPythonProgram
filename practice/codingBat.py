
str= ""
def first_two(str):
    if len(str) == 0:
        return """ "yields the empty string" """
    elif len(str) == 2 or len(str) == 1:
        return str[:]
    else:
        return str[:2]

