# !/usr/bin/env python
# -*- coding:utf8 --

class OverallFunctional(object):
    THE_WORD = ''

    def __init__(self, letters):
        self.letters = letters

    def _check_letters(self):
        checked = ''
        for i in self.letters:
            if i in self.THE_WORD:
                checked += i
        return checked

    def _to_word(self):
        new_word = ''
        for i in self._check_letters():
            for ind, val in enumerate(self.THE_WORD):
                if i == val:
                    new_word[ind] == i
        return new_word

    def _capitalize(self):
        return self._to_word().title()

    def _uppercase(self):
        return self._to_word().upper()


class Facade(OverallFunctional):
    def make_sence(self, spelling):
        if spelling == 'Up':
            return self._uppercse()
        if spelling == 'Cap':
            return self._capitalize()
