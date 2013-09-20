from collective.geo.flexitopic.browser import maplayer
from collective.geo.mapwidget.browser.widget import MapLayers


class KMLMapLayers(MapLayers):
    '''
    create all layers for this view.
    '''

    def layers(self):
        layers = super(KMLMapLayers, self).layers()
        layers.append(maplayer.KMLMapLayer(self.view.view.collection()))
        return layers
