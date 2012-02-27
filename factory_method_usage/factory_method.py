#!/usr/bin/env python
# -*- coding; utf-8 -*-


class Culture(object):
    """
    Base class for main content processing.
    """
    def get_culture(self):
        return self.__str__()



class Goverment(object):
    """
    Base structure class.
    """
    def __str__(self):
        return self.culture.__str__()

    def get_culture(self):
        return self.culture.get_culture()

    def set_culture(self):
        """
        Must be overrided. Assign self.culture attribute,
        which used in other methods. self.culture is
        Culture class instance.
        """
        raise NotImplementedError
