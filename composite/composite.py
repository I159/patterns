# /usr/bin/env python
# -*-coding:utf8 -*-

class ItemsTree(object):

    def __init__(self, name):
        self.items = []
        self.name = name
        self.current = 0

    def __iter__(self):
        return self

    def add(self, item):
        self.items.append(item)
        return item

    def remove(self, item):
        self.items = [i for i in self.items if i.name != item]

    def __len__(self):
        return len(self.items)

    def get(self, item):
        return self.items[item]

    def next(self):
        self.current += 1
        if len(self.items) >= self.current:
            return self.items[self.current-1]
        else:
            self.current = 0
            raise StopIteration
