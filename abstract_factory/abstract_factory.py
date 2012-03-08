#!/usr/bin/env python
# -*- coding; utf-8 -*-

"""
Provide an interface for creating families of related or dependent objects
without specifying their concrete classes.
"""

class Styles(object):
    def __init__(self, style):
        self.style = style

    def get_style(self):
        styles = {'Rat Look': 'Rusty slammed',
                  'Glance Resto': 'Low, glance and shavy'}
        return styles

    def __call__(self):
        return self.get_style().get(self.style)


class Donor(object):
    def get_model(self):
        raise NotImplementedError

    def get_style(self):
        raise NotImplementedError


class WorkShop(Donor):
    objects = {}

    def build_it(self, name='default'):
        ride = self.objects.get(name)()
        style = Styles(ride.get_style())
        return '%s %s' % (style(), ride.get_model())
