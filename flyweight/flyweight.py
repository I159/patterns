#!/usr/bin/en python
#-*-coding:utf8-*-

import weakref
#values = (1, 2, 3)
#suits = ('h', 'v', 'x')
#
#class Card(object):
#    def __init__(self, value, suit):
#        self.value, self.suit = value, suit
#
#    def __repr__(self):
#        print self.value
#        return "<Card: %s%s>" % (self.value, self.suit)
#
#    def __eq__(self, card):
#        return self.value == card.value and self.suit == card.suit
#
#    def __ne__(self, card):
#        return not self.__eq__(card)


class Flyweight(object):
    _card_pool = weakref.WeakValueDictionary()

    def __new__(self, value):
        obj = self._card_pool.get(value, None)
        if not obj:
            obj = object.__new__(self)
            self._card_pool[value] = object
            obj.value = value
        print len(self._card_pool)
        return obj
