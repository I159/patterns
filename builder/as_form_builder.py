#!/usr/bin/env python
# -*- coding; utf-8 -*-
"""
Separate the construction of a complex object from its representation. Allowing
to use the same construction process to create various representations.
"""

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
        self.project.get_type_attr()
        self.project.build_tag()
        self.project.put_html_attrs()

    def get_construction(self):
        return self.project.construction


class StyleStandard(object):
    """
    Abstract builder (in original pattern).
    Abstract interface for creating objects (product).
    """
    def __init__(self, type_attr):
        self.construction = None
        self.type_attr = type_attr

    def new_construction(self):
        self.construction = Workshop()


class Workshop(object):
    """
    Product (in original pattern)
    The final object that will be created by the Director using Builder.
    """
    def __init__(self):
        self.type_attr = None
        self.tag = None
        self.html_attrs = None

    def __repr__(self):
        if self.html_attrs:
            joined_attrs = ('='.join((key, '"%s"' % value)) for key, value in self.html_attrs.items())
        return '<%s type="%s" %s>' % (self.tag, self.type_attr, ' '.join(joined_attrs))


class BuildIt(object):
    """
    Client as callable class.
    Client is not required to be a callable class, but in my opinion, it is
    pretty useful.
    """
    def __init__(self, type_attr, project):
        self.tager = Engineer()
        self.type_attr = type_attr
        self.style = project
        self.construction = None

    def build(self):
        self.tager.project = self.style(type_attr=self.type_attr)
        self.tager.construct_car()
        self.construction = self.tager.get_construction()
        return self.construction

    def __call__(self):
        return self.build()


class Boso510(StyleStandard):
    """
    Concrete builder (in original pattern).
    Provides implementation for Builder. It is an object able to construct
    other objects. Constructs and assembles parts to build the objects.
    """
    def get_type_attr(self):
        self.construction.type_attr = self.type_attr

    def build_tag(self):
        self.construction.tag = 'input'

    def put_html_attrs(self):
        self.construction.html_attrs = {'class': 'form', 'id': 'id_form'}


Dutsun510Boso = BuildIt(type_attr='text', project=Boso510)

print Dutsun510Boso()


class AbsField(object):
    tag = None
    tag_type = None

    def get_type(self):
        if self.tag == 'input':
            return self.tag_type

    def get_structure(self):
        if self.tag == 'input':
            return "single"
        return "closing"

    def field_repr(self):
        structures = {"single": "<%s %s %s />", "closing": "<%s %s></%s>"}
        return structures.get(self.get_structure())


