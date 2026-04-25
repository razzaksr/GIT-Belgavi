def merge(left,right):
    result = []
    lt = rt = 0
    while lt<len(left) and rt< len(right):
        if left[lt] <= right[rt]:
            result.append(left[lt])
            lt+=1
        else:
            result.append(right[rt])
            rt+=1
    result.extend(left[lt:]);result.extend(right[rt:])
    return result
def ordering(items):
    if len(items)<=1: return items
    mid = len(items)//2
    left = ordering(items[:mid])
    right = ordering(items[mid:])
    return merge(left,right)
print(ordering([45,28,12,36,7]))
print(ordering(["spring","activemq","maven","jpa","tailwind"]))