#!/usr/bin/env python
# -*- coding; utf-8 -*-


class Engineer(object):
    """
    Abstract class
    """
    def __init__(self):
        self.project = None

    def construct_car(self):
        self.project.new_construction()
        self.project.get_donor()
        self.project.build_engene()
        self.project.put_wheels()

    def get_construction(self):
        return self.project.construction


#Abstract Builder
class StyleStandard(object):
    def __init__(self, donor):
        self.construction = None
        self.donor = donor

    def new_construction(self):
        self.construction = Workshop()


#Product
class Workshop(object):
    def __init__(self):
        self.donor = None
        self.engene = None
        self.wheels = None

    def __repr__(self):
        return '%s %s on %s' % (self.engene, self.donor, self.wheels)


#Client
class BuildIt(object):
    """
    Required parameters are `donor` as string car name
    and `style` as StyleStandard exended class instance.
    """
    def __init__(self, donor, style):
        self.engeneer = Engineer()
        self.donor = donor
        self.style = style
        self.construction = None

    def build(self):
        self.engeneer.project = self.style(donor=self.donor)
        self.engeneer.construct_car()
        self.construction = self.engeneer.get_construction()
        return self.construction

    def __call__(self):
        return self.build()
