from collective.flexitopic.browser.flexitopicview import FlexiTopicView



class FlexiTopicMapView(FlexiTopicView):
    ''' add a map to the flexitopc view'''
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
        layer = kmls[0];
        layer.setVisibility(false);
        layer.loaded = false;
        layer.setUrl('%s/@@flexitopickml_view' + qs);
        layer.refresh({ force: true, params: params });
        layer.setVisibility(true);
        '''

