# !/usr/bin/env python
# -*- coding:utf8 --

class OverallFunctional(object):
    THE_WORD = 'superman'

    def __init__(self, letters):
        self.letters = letters

    def _check_letters(self):
        checked = ''
        for i in self.letters:
            if i in self.THE_WORD:
                checked += i
        return checked

    def _to_word(self):
        new_word = range(len(self.THE_WORD))
        for i in self._check_letters():
            for ind, val in enumerate(self.THE_WORD):
                if i == val:
                    new_word[ind] = i
        return ''.join(new_word)

    def _capitalize(self):
        return self._to_word().title()


class Facade(OverallFunctional):
    def make_sence(self):
        return self._capitalize()
