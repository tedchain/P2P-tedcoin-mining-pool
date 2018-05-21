ident = '$Id: Errors.py 921 2005-02-15 16:32:23Z warnes $'
from version import __version__

import exceptions

################################################################################
# Exceptions
################################################################################
class Error(exceptions.Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return "<Error : %s>" % self.msg
    __repr__ = __str__
    def __call__(self):
        return (msg,)

class RecursionError(Error):
    pass

class UnknownTypeError(Error):
    pass

class HTTPError(Error):
    # indicates an HTTP protocol error
    def __init__(self, code, msg):
        self.code = code
        self.msg  = msg
    def __str__(self):
        return "<HTTPError %s %s>" % (self.code, self.msg)
    __repr__ = __str__
    def __call___(self):
        return (self.code, self.msg, )

class UnderflowError(exceptions.ArithmeticError):
    pass

