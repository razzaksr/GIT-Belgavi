from collections import OrderedDict
class LRUCache:
    def __init__(self, cap):
        self.__limit = cap
        self.__cache = OrderedDict()
    def push(self,package, person):
        if package in self.__cache:
            self.__cache.move_to_end(package)
        self.__cache[package]=person
        if len(self.__cache) > self.__limit:
            self.__cache.popitem(last=False)
    def find(self,package):
        if package not in self.__cache: return -1
        self.__cache.move_to_end(package)
        return self.__cache[package]
lru = LRUCache(2)
lru.push(4.5,"Vikas")
lru.push(2.5,"Richard")
print(lru.find(2.5))
lru.push(6.5,"Praveen")
print(lru.find(4.5))