from zope.interface import Interface, implements
from collective.flexitopic.browser.flexitopicview import FlexiTopicView
from collective.flexitopic.browser.flexitopicview import FlexiCollectionView
from collective.flexitopic.browser.viewlets import JsViewlet, BaseViewlet
from collective.geo.flexitopic.interfaces import IGeoFlexiTopicViewlet


class IFlexiTopicMapView(Interface):
    ''' add a map to the flexitopc view'''

class FlexiTopicMapView(FlexiTopicView):
    ''' add a map to the flexitopc view'''
    implements(IFlexiTopicMapView)


class FlexiCollectionMapView(FlexiCollectionView):
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

        try {
            var map = $('#default-cgmap').data('collectivegeo').mapwidget.map;
        } catch(e) {
            var map = null;
        };
        if ( map != null){
            var kmls = map.getLayersByClass('OpenLayers.Layer.Vector');
            var kmlUrl = '%s/@@flexitopickml_view' + qs;
            jQuery("a#flexitopickmlurl").attr('href', kmlUrl);
            layer = kmls[0];
            layer.refresh({url: kmlUrl});
        };
        '''

class MapViewlet(BaseViewlet):
    '''' render the map based on the query
    '''
    implements(IGeoFlexiTopicViewlet)

