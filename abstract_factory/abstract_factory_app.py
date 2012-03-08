#!/usr/bin/env python
# -*- coding; utf-8 -*-

from abstract_factory import Donor, WorkShop


class RatBug(Donor):
    """
    Client inherited from abtract client.
    Prsonalized require methods
    """
    def get_model(self):
        return "VW Cafer'65"

    def get_style(self):
        return 'Rat Look'


class RestoWagenWorkShop(WorkShop):
    """
    Appointed objects for reproducing in factory interface
    """
    objects = {'Bug': RatBug()}


# Usage of factory
WorkShop = RestoWagenWorkShop()
Bug = WorkShop.build_it('Bug')

print Bug
