#coding: utf-8
"""
VW factory
"""
class Styles(object):
    def __init__(self, style):
        self.style = style

    def __call__(self):
        styles = {'Rat': 'Old rusty', 'Glance': 'Bright and shiny'}
        return styles.get(self.style)


class Volkswagen(object):
    def get_model(self):
        raise NotImplementedError

    def get_style(self):
        raise NotImplementedError


class RatCafer(Volkswagen):
    def __init__(self):
        self.model = 'Cafer 1200'
        self.style = 'Rat'

    def get_model(self):
        return self.model

    def get_style(self):
        return self.style


class CarmannChia(Volkswagen):
    def __init__(self):
        self.model = 'Carmann Chia'

    def get_model(self):
        return self.model


class T1(Volkswagen):
    def __init__(self):
        self.model = 'T1'

    def get_model(self):
        return self.model

class RestoShop(Volkswagen):
    objects = {
            'Cafer': RatCafer,
            'Carmann': CarmannChia,
            'T1': T1
            }

    def build_it(self, name='default'):
        ride = self.objects.get(name, 'default')()
        style = Styles(ride.get_style())
        return '%s %s' % (style(), ride.get_model())


Shop = RestoShop()
Cafer = Shop.build_it('Cafer')

print Cafer
