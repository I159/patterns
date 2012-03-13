# !/usr/bin/env python
# -*- coding:utf8 -*-

from composite import ItemsTree


root = ItemsTree('/')
first = root.add(ItemsTree('1'))
second = root.add(ItemsTree('2'))
second.add(ItemsTree('2.1'))
third = root.add(ItemsTree('3'))
third.add(ItemsTree('3.1'))
third.get(0).add(ItemsTree('3.2'))


def walk(item, level):
    """
    Hierarhy composing.
    """
    print '%s%s' % (" "*level, item.name)
    for i in item:
        walk(i, level+1)

walk(root, 0)
