#!/usr/bin/env python
# -*- coding; utf-8 -*-

import factory_method

class Dictature(factory_method.Culture):
    def __str__(self):
        return 'Dictature'


class GovermentA(factory_method.Goverment):
    def set_culture(self):
        self.culture = Dictature()


g1 = GovermentA()
g1.set_culture()
print str(g1)



