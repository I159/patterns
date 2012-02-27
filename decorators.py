#!/usr/bin/env python
# -*- coding; utf-8 -*-


class DebugTrace(object):
    def __init__(self, f):
        print("Tracing: {0}".format(f.__name__))
        self.f = f

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)


class Greeter(object):
    instances = 0

    def __init__(self):
        self.instances += 1
        self._inst = self.instances

    @DebugTrace
    def hello(self):
        print ("*** Greeter {0} sas hello".format(self._inst))


#@DebugTrace
#def greet():
#    g = Greeter()
#    g2 = Greeter()
#    g.hello()
#    g2.hello()
#
#greet()
