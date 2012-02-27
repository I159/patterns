#!/usr/bin/env python
# -*- coding; utf-8 -*-
"""
Builder pattern
"""

#Director
class Engineer(object):
    """
    Abstract class 
    """
    def __init__(self):
        self.project = None

    def construct_car(self):
        self.project.new_building()
        self.project.get_donor()
        self.project.build_engene()
        self.project.put_wheels()

    def get_building(self):
        return self.project.building

#Abstract Builder
class Donor(object):
    def __init__(self, donor):
        self.building = None
        self.donor = donor

    def new_building(self):
        self.building = Building()


class BosoProject(Donor):
    def get_donor(self):
        self.building.donor = self.donor

    def build_engene(self):
        self.building.engene = 'sr20det'

    def put_wheels(self):
        self.building.wheels = 'Work Ewing III'


class VIPProject(Donor):
    def get_donor(self):
        self.building.donor = self.donor

    def build_engene(self):
        self.building.engene = '4M Bi-Turbo'

    def put_wheels(self):
        self.building.wheels = 'Vienna 8.5/9.5 with Yokohama moto tyres'


#Product
class Building(object):
    def __init__(self):
        self.donor = None
        self.engene = None
        self.wheels = None

    def __repr__(self):
        return '%s %s on %s' % (self.engene, self.donor, self.wheels)


#Client
class BuildIt(object):
    def __init__(self, donor):
        self.engeneer = Engineer()
        self.donor = donor
        self.building = None

    def build(self):
        self.engeneer.project = VIPProject(donor=self.donor)
        self.engeneer.construct_car()
        self.building = self.engeneer.get_building()
        return self.building

    def __call__(self):
        return self.build()

