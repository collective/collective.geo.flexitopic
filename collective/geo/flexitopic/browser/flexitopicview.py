from zope.interface import Interface, implements
from collective.flexitopic.browser.flexitopicview import FlexiTopicView
from collective.flexitopic.browser.viewlets import JsViewlet, BaseViewlet
from collective.geo.kml.interfaces import IKMLOpenLayersViewlet

class IFlexiTopicMapView(Interface):
    ''' add a map to the flexitopc view'''

class FlexiTopicMapView(FlexiTopicView):
    ''' add a map to the flexitopc view'''
    implements(IFlexiTopicMapView)

class JsMapViewlet(JsViewlet):
    ''' overide the flexitopic js viewlet '''

    add_form_data_js = '''
       // refresh map
        var qs = '?';
        var params = {};
        jQuery.each(dt, function(i, field){
            qs = qs + field.name + '=' + field.value + "&";
            params[field.name] = field.value;
        });
        var map = cgmap.config['default-cgmap'].map;
        var kmls = map.getLayersByClass('OpenLayers.Layer.GML');
        var kmlUrl = '%s/@@flexitopickml_view' + qs;
        jQuery("a#flexitopickmlurl").attr('href', kmlUrl);
        layer = kmls[0];
        layer.setVisibility(false);
        layer.loaded = false;
        layer.setUrl(kmlUrl);
        layer.refresh({ force: true, params: params });
        layer.setVisibility(true);
        '''

class MapViewlet(BaseViewlet):
    '''' render the map based on the query
    '''
    implements(IKMLOpenLayersViewlet)

