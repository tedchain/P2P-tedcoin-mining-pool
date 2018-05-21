from __future__ import nested_scopes

ident = '$Id: NS.py 1468 2008-05-24 01:55:33Z warnes $'
from version import __version__

##############################################################################
# Namespace Class
################################################################################
def invertDict(dict):
    d = {}

    for k, v in dict.items():
        d[v] = k

    return d

class NS:
    XML  = "http://www.w3.org/XML/1998/namespace"

    ENV  = "http://schemas.xmlsoap.org/soap/envelope/"
    ENC  = "http://schemas.xmlsoap.org/soap/encoding/"

    XSD  = "http://www.w3.org/1999/XMLSchema"
    XSD2 = "http://www.w3.org/2000/10/XMLSchema"
    XSD3 = "http://www.w3.org/2001/XMLSchema"

    XSD_L = [XSD, XSD2, XSD3]
    EXSD_L= [ENC, XSD, XSD2, XSD3]

    XSI   = "http://www.w3.org/1999/XMLSchema-instance"
    XSI2  = "http://www.w3.org/2000/10/XMLSchema-instance"
    XSI3  = "http://www.w3.org/2001/XMLSchema-instance"
    XSI_L = [XSI, XSI2, XSI3]

    URN   = "http://soapinterop.org/xsd"

    # For generated messages
    XML_T = "xml"
    ENV_T = "SOAP-ENV"
    ENC_T = "SOAP-ENC"
    XSD_T = "xsd"
    XSD2_T= "xsd2"
    XSD3_T= "xsd3"
    XSI_T = "xsi"
    XSI2_T= "xsi2"
    XSI3_T= "xsi3"
    URN_T = "urn"

    NSMAP       = {ENV_T: ENV, ENC_T: ENC, XSD_T: XSD, XSD2_T: XSD2,
                    XSD3_T: XSD3, XSI_T: XSI, XSI2_T: XSI2, XSI3_T: XSI3,
                    URN_T: URN}
    NSMAP_R     = invertDict(NSMAP)

    STMAP       = {'1999': (XSD_T, XSI_T), '2000': (XSD2_T, XSI2_T),
                    '2001': (XSD3_T, XSI3_T)}
    STMAP_R     = invertDict(STMAP)

    def __init__(self):
        raise Error, "Don't instantiate this"



