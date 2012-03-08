# !/usr/bin/env python
# -*- coding: utf-8 -*-

from object_pool import Resource, ObjectPool


def main():
    pool = ObjectPool.get_instance()

    one = pool.get_resource()
    one.set_value(10)
    pool.set_resource(one)
    print "%s = %d" % (one, one.get_value())


    one = pool.get_resource()
    one.set_value(100)
    pool.set_resource(one)
    print "%s = %d" % (one, one.get_value())

    two = pool.get_resource()
    two.set_value(300)
    pool.set_resource(two)
    print "%s = %d" % (two, two.get_value())

main()
