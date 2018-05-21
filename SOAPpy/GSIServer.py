from __future__ import nested_scopes

ident = '$Id: GSIServer.py 1468 2008-05-24 01:55:33Z warnes $'
from version import __version__

#import xml.sax
import re
import socket
import sys
import SocketServer
from types import *
import BaseHTTPServer

# SOAPpy modules
from Parser      import parseSOAPRPC
from Config      import SOAPConfig
from Types       import faultType, voidType, simplify
from NS          import NS
from SOAPBuilder import buildSOAP
from Utilities   import debugHeader, debugFooter

try: from M2Crypto import SSL
except: pass

#####

from Server import *

from pyGlobus.io import GSITCPSocketServer, ThreadingGSITCPSocketServer
from pyGlobus import ioc

def GSIConfig():
    config = SOAPConfig()
    config.channel_mode = ioc.GLOBUS_IO_SECURE_CHANNEL_MODE_GSI_WRAP
    config.delegation_mode = ioc.GLOBUS_IO_SECURE_DELEGATION_MODE_FULL_PROXY
    config.tcpAttr = None
    config.authMethod = "_authorize"
    return config

Config = GSIConfig()

class GSISOAPServer(GSITCPSocketServer, SOAPServerBase):
    def __init__(self, addr = ('localhost', 8000),
                 RequestHandler = SOAPRequestHandler, log = 0,
                 encoding = 'UTF-8', config = Config, namespace = None):

        # Test the encoding, raising an exception if it's not known
        if encoding != None:
            ''.encode(encoding)

        self.namespace          = namespace
        self.objmap             = {}
        self.funcmap            = {}
        self.encoding           = encoding
        self.config             = config
        self.log                = log
        
        self.allow_reuse_address= 1
        
        GSITCPSocketServer.__init__(self, addr, RequestHandler,
                                    self.config.channel_mode,
                                    self.config.delegation_mode,
                                    tcpAttr = self.config.tcpAttr)
        
    def get_request(self):
        sock, addr = GSITCPSocketServer.get_request(self)

        return sock, addr
       
class ThreadingGSISOAPServer(ThreadingGSITCPSocketServer, SOAPServerBase):

    def __init__(self, addr = ('localhost', 8000),
                 RequestHandler = SOAPRequestHandler, log = 0,
                 encoding = 'UTF-8', config = Config, namespace = None):
        
        # Test the encoding, raising an exception if it's not known
        if encoding != None:
            ''.encode(encoding)

        self.namespace          = namespace
        self.objmap             = {}
        self.funcmap            = {}
        self.encoding           = encoding
        self.config             = config
        self.log                = log
        
        self.allow_reuse_address= 1
        
        ThreadingGSITCPSocketServer.__init__(self, addr, RequestHandler,
                                             self.config.channel_mode,
                                             self.config.delegation_mode,
                                             tcpAttr = self.config.tcpAttr)

    def get_request(self):
        sock, addr = ThreadingGSITCPSocketServer.get_request(self)

        return sock, addr

