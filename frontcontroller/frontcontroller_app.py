#!/usr/bin/env python
#-*-coding:utf8-*-

from frontcontroller import Dispatcher


class Request(object):
    pass


print Dispatcher(Request()).get_instance()
