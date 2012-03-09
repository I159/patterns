#!/usr/bin/env python
# -*- coding; utf-8 -*-

import builder


class Boso510(builder.StyleStandard):
    """
    Concrete builder (in original pattern).
    Provides implementation for Builder. It is an object able to construct
    other objects. Constructs and assembles parts to build the objects.
    """
    def get_donor(self):
        self.construction.donor = self.donor

    def build_engene(self):
        self.construction.engene = 'sr20det'

    def put_wheels(self):
        self.construction.wheels = 'Work Equip'


Dutsun510Boso = builder.BuildIt(donor='Dutsun 510', project=Boso510)

print Dutsun510Boso()
