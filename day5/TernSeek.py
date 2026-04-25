def ternary(items,target):
    begin , end = 0, len(items)-1
    while begin<=end:
        mid1 = begin + (end-begin)//3
        mid2 = end - (end-begin)//3
        if items[mid1] == target: return mid1
        elif items[mid2] == target: return mid2
        # first portion
        elif items[mid1] > target: end = mid1-1
        # third portion
        elif items[mid2] < target: begin = mid2+1
        # second portion
        else:
            begin = mid1+1
            end = mid2-1
    return -1
print(ternary(["flask","hibernate","kepler","laravel","maven","oracle"],"laravel"))
print(ternary(["flask","hibernate","kepler","laravel","maven","oracle"],"flask"))
print(ternary(["flask","hibernate","kepler","laravel","maven","oracle"],"kepler"))