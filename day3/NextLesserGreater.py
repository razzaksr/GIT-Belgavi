def coldTemp(degrees):
    result = [-1] * len(degrees)
    stk = []
    for index in range(len(degrees)):
        while stk and degrees[stk[-1]] > degrees[index]:
            pos = stk.pop()
            result[pos] = degrees[index]
        stk.append(index)
    return result
def warmTemp(degrees):
    result = [-1] * len(degrees)
    stk = []
    for index in range(len(degrees)):
        while stk and degrees[stk[-1]] < degrees[index]:
            pos = stk.pop()
            result[pos] = degrees[index]
        stk.append(index)
    return result
print(coldTemp([73,74,75,71,69,72,76,73]))
print(coldTemp([36,25,38,42,20]))
print(coldTemp([4,5,2,25]))
print(warmTemp([73,74,75,71,69,72,76,73]))
print(warmTemp([36,25,38,42,20]))
print(warmTemp([4,5,2,25]))