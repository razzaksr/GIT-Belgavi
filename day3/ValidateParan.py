def isValid(exp):
    stk = []
    tab = {'}':'{',']':'[',')':'('}
    for each in exp:
        if each in tab:
            popped = stk.pop() if stk else '#'
            if popped != tab[each]: return False
        else: stk.append(each)
    return not stk
print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))