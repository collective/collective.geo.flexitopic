from zope.interface import implements, Interface
from plone.memoize import view
from Products.CMFCore.utils import getToolByName

from collective.geo.kml.browser.kmldocument import KMLBaseDocument, BrainPlacemark
from collective.flexitopic.browser.utils import get_search_results, get_search_results_ng


class IFlexiTopicKmlView(Interface):
    """
    FlexiTopicKml view interface
    """


class FlexiTopicKmlView(KMLBaseDocument):
    """
    FlexiTopicKml browser view
    """
    implements(IFlexiTopicKmlView)


    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')


    @property
    def features(self):
        results = get_search_results(self)['results']
        for brain in results:
            try:
                if brain.zgeo_geometry['coordinates']:
                    yield BrainPlacemark(brain, self.request, self)
            except:
                continue

class FlexiCollectionKmlView(FlexiTopicKmlView):

    @property
    def features(self):
        results = get_search_results_ng(self)['results']
        for brain in results:
            try:
                if brain.zgeo_geometry['coordinates']:
                    yield BrainPlacemark(brain, self.request, self)
            except:
                continue

