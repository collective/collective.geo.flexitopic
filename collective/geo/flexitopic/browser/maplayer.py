#
from collective.geo.mapwidget.browser.widget import MapLayers
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
        query_string =''
        return u"""
        function() {
                return new OpenLayers.Layer.Vector("%s", {
                    protocol: new OpenLayers.Protocol.HTTP({
                      url: "%s@@flexitopickml_view?%s",
                      format: new OpenLayers.Format.KML({
                        extractStyles: true,
                        extractAttributes: true})
                      }),
                    strategies: [new OpenLayers.Strategy.Fixed()],
                    visibility: true,
                    projection: widget.map.displayProjection
                  });
                } """ % (self.context.Title().replace("'", "&apos;"),
                        context_url, query_string)



class KMLMapLayers(MapLayers):
    '''
    create all layers for this view.
    '''

    def layers(self):
        layers = super(KMLMapLayers, self).layers()
        layers.append(KMLMapLayer(self.context))
        return layers
