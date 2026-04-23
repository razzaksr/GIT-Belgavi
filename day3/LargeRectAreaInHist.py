def findArea(hts):
    stk = []
    mArea = 0
    size = len(hts)
    for index in range(size+1):
        cHt = 0 if index == size else hts[index]
        while stk and cHt < hts[stk[-1]]:
            pHt = hts[stk.pop()]
            wd = index if not stk else index - stk[-1] -1
            area = pHt * wd
            mArea = max(mArea,area)
        stk.append(index)
    return mArea
print(findArea([2,1,5,6,2,3]))
print(findArea([2,4]))