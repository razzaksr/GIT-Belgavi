def bin(items,target):
    begin , end = 0, len(items)-1
    while begin<=end:
        mid = begin + (end-begin)//2
        if items[mid] == target: return mid
        elif items[mid] < target: begin = mid+1
        else: end = mid-1
    return -1

print(bin([2,5,8,10,14],10))
print(bin([2,5,8,10,14],2))
print(bin([2,5,8,10,14],14))
print(bin([2,5,8,10,14],12))