# -*- coding: utf-8 -*-

def multiton(cls):
    instances = {}
    print 'cls %s' % cls
    print 'out name %s' % name
    def get_instance(name):
        print 'name %s' % name
        if name not in instances:
            instances[name] = cls()
        return instances[name]
    return get_instance


@multiton
class MyClass(object):
    pass

#a = MyClass('0')
#b = MyClass('0')
c = MyClass('asdfasdf')

#print 'a: %s' % a
#print a is b
#print a is c

