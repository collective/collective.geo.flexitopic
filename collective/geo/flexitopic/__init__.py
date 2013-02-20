#
from zope.i18nmessageid import MessageFactory

flexitopicMessageFactory = MessageFactory('collective.geo.flexitopic')

DEPENDENCIES = [
    #u'collective.flexitopic',
]

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
