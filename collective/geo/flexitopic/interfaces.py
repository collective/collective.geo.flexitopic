"""Define interfaces for your add-on.
"""
from collective.flexitopic.interfaces import IFlexiTopicLayer
from collective.geo.kml.interfaces import IKMLOpenLayersViewlet

class IGeoFlexiTopicLayer(IFlexiTopicLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """


class IGeoFlexiTopicViewlet(IKMLOpenLayersViewlet):
    """ Marker interface for browser.flexitopicview.MapViewlet
    """

class IGeoFlexiTopicPortletViewlet(IGeoFlexiTopicViewlet):
    """ Marker interface for browser.flexitopicview.MapViewlet
    """
