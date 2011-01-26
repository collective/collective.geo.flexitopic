#
from collective.geo.mapwidget.browser.widget import MapLayers
#from collective.geo.kml.browser.maplayers import KMLMapLayer
from collective.geo.mapwidget.maplayers import MapLayer

class KMLMapLayer(MapLayer):
    """
    a layer for one level sub objects.
    """

    def __init__(self, context):
        self.context = context

    @property
    def jsfactory(self):
        context_url = self.context.absolute_url()
        if not context_url.endswith('/'):
            context_url += '/'

        return"""
        function() { return new OpenLayers.Layer.GML('%s', '%s' + '@@flexitopickml_view',
            { format: OpenLayers.Format.KML,
              projection: cgmap.createDefaultOptions().displayProjection,
              formatOptions: {
                  extractStyles: true,
                  extractAttributes: true }
            });}""" % (self.context.Title().replace("'", "\'"), context_url)


class KMLMapLayers(MapLayers):
    '''
    create all layers for this view.
    '''

    def layers(self):
        layers = super(KMLMapLayers, self).layers()
        layers.append(KMLMapLayer(self.context))
        return layers
