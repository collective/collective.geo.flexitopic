"""Define interfaces for your add-on.
"""
from plone.theme.interfaces import IDefaultPloneLayer
from collective.geo.kml.interfaces import IKMLOpenLayersViewlet

class IGeoFlexiTopicLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """


class IGeoFlexiTopicViewlet(IKMLOpenLayersViewlet):
    """ Marker interface for browser.flexitopicview.MapViewlet
    """
