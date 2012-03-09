#!/usr/bin/env python
# -*- coding; utf-8 -*-

"""
The builder pattern is an object creation software design pattern. The
intention is to abstract steps of construction of objects so that different 
implementations of these steps can construct different representations of 
objects. Often, the builder pattern is used to build products in accordance
with the composite pattern.
"""

class Engineer(object):
    """
    Director (in original pattern)
    The Director class is responsible for managing the correct sequence of
    object creation. It receives a Concrete Builder as a parameter and
    executes the necessary operations on it.
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


class StyleStandard(object):
    """
    Abstract builder (in original pattern).
    Abstract interface for creating objects (product).
    """
    def __init__(self, donor):
        self.construction = None
        self.donor = donor

    def new_construction(self):
        self.construction = Workshop()


class Workshop(object):
    """
    Product (in original pattern)
    The final object that will be created by the Director using Builder.
    """
    def __init__(self):
        self.donor = None
        self.engene = None
        self.wheels = None

    def __repr__(self):
        return '%s %s on %s' % (self.engene, self.donor, self.wheels)


class BuildIt(object):
    """
    Client as callable class.
    Client is not required to be a callable class, but in my opinion, it is
    pretty useful.
    """
    def __init__(self, donor, project):
        self.engeneer = Engineer()
        self.donor = donor
        self.style = project
        self.construction = None

    def build(self):
        self.engeneer.project = self.style(donor=self.donor)
        self.engeneer.construct_car()
        self.construction = self.engeneer.get_construction()
        return self.construction

    def __call__(self):
        return self.build()
