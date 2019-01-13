# -*- coding: utf-8 -*-


def d_if(condition):
    def decorated(method):
        if condition:
            return method
        else:
            return lambda : None
    return decorated
