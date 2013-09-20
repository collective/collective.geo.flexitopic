from zope.interface import implements
from collective.geo.flexitopic.browser import flexitopicview
from collective.geo.flexitopic.interfaces import IGeoFlexiTopicPortletViewlet

class JsMapViewlet(flexitopicview.JsMapViewlet):

 def __init__(self, context, request, view, manager=None):
        super(JsMapViewlet, self).__init__(context, request, view, manager)
        self.topic = self.view.collection()
        if self.view.data.flexitopic_width:
            self.flexitopic_width = self.view.data.flexitopic_width
        if self.view.data.flexitopic_height:
            self.flexitopic_height = self.view.data.flexitopic_height
        if self.view.data.limit:
            self.items_ppage = self.view.data.limit

class MapViewlet(flexitopicview.MapViewlet):
    '''' render the map based on the query
    '''
    implements(IGeoFlexiTopicPortletViewlet)
