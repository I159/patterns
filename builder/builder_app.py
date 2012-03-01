#!/usr/bin/env python
# -*- coding; utf-8 -*-

import builder


class Boso510(builder.StyleStandard):
    def get_donor(self):
        self.construction.donor = self.donor

    def build_engene(self):
        self.construction.engene = 'sr20det'

    def put_wheels(self):
        self.construction.wheels = 'Work Equip'


Dutsun510Boso = builder.BuildIt(donor='Dutsun 510', style=Boso510)

print Dutsun510Boso()
