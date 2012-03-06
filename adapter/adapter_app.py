# /usr/bin/env python
# -*- coding:utf:8 -*-

from adapter import *

class Dog(Client):
    pat_name = 'Bob'
    pat_noise = 'Bow-woW!'


class Bob(AbsAdapter, Dog):
    def make_noise(self):
        return self.noise()


bob = ParamAdapter(Dog())

print '%s says %s' % (bob.pat_name, bob.make_noise())
print '%s says %s' % (Bob.pat_name, Bob().make_noise())

