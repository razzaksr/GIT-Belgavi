def findPivot(items,start,end):
    piData = items[end]
    it = start-1
    for cur in range(start,end):
        if items[cur]>=piData:
            it+=1
            items[cur], items[it] = items[it], items[cur]
    items[end], items[it+1] = items[it+1], items[end]
    return it+1
def ordering(items,start,end):
    if start<end:
        piPoint = findPivot(items,start,end)
        ordering(items,start,piPoint-1)
        ordering(items,piPoint+1,end)
    return items
print(ordering([45,28,12,36,7],0,4))
print(ordering(["spring","activemq","maven","jpa","tailwind"],0,4))