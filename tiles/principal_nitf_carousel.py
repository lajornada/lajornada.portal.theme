# -*- coding: utf-8 -*-

from collective.cover import _
from collective.cover.tiles.list import IListTile
from collective.cover.tiles.list import ListTile
from collective.cover.widgets.textlinessortable import TextLinesSortableFieldWidget
from plone.autoform import directives as form
from plone.tiles.interfaces import ITileDataManager
from plone.uuid.interfaces import IUUID
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope import schema
from zope.interface import implements


class IPrincipalCarouselTile(IListTile):
    """
    """
    
    autoplay = schema.Bool(
        title=_(u'Auto play'),
        required=False,
        default=True,
        )

    form.widget(uuids=TextLinesSortableFieldWidget)
    uuids = schema.List(
        title=_(u'Elements'),
        value_type=schema.TextLine(),
        required=False,
        readonly=False,
        )
    

class PrincipalCarouselTile(ListTile):
    implements(IPrincipalCarouselTile)
    
    index = ViewPageTemplateFile("templates/principal_nitf_carousel_edit.pt")
    is_configurable = True
    is_editable = True
    
    def populate_with_object(self, obj):
        super(PrincipalCarouselTile, self).populate_with_object(obj)  # check permission
        try:
            scale = obj.restrictedTraverse('@@images').scale('image')
        except:
            scale = None
            if not scale:
                return
            self.set_limit()
            uuid = IUUID(obj, None)
            data_mgr = ITileDataManager(self)
            
            old_data = data_mgr.get()
            if data_mgr.get()['uuids']:
                uuids = data_mgr.get()['uuids']
                if type(uuids) != list:
                    uuids = [uuid]
                elif uuid not in uuids:
                    uuids.append(uuid)
                    old_data['uuids'] = uuids[:self.limit]
            else:
                old_data['uuids'] = [uuid]
                data_mgr.set(old_data)

    def autoplay(self):
        if self.data['autoplay'] is None:
            return True  # default value
        
        return self.data['autoplay']

    def init_js(self):
        return """

$(function() {                                                                                                                                 
                                                                                                                                               
    Galleria.loadTheme("++resource++lajornada.portal.theme/galleria-theme/galleria.cover_theme.js");                                                     
                          
    Galleria.run('#galleria-%s .galleria-inner',                                                                                                   
    {                                                                                                                                              
        dataConfig: function(img){                                                                                                                     
                                                                                                                                               
            return {                                                                                                                                       
                                                                                                                                               
                thumbDesc: $(img).attr('data-thumbDesc')                                                                                                       
                                                                                                                                               
            };                                                                                                                                             
    }});      


    Galleria.ready(function() {                                                                                                                
                                                                                                                                               
        this.bind('image', function(e) {                                                                                                               
        // alert("Cambio en el CSS cuando los elementos ya estan creados");                                                                         
        $(".galleria-thumbnails-list").css("width","970px");
        $(".galleria-thumbnails-list").css("height","200px");
        $(".galleria-thumbnails").css("height","200px");
        $(".galleria-thumbnails").css("width","970px");
        $(".galleria-thumbnails .galleria-image").css("width","170px");                                                                            
       $(".galleria-thumbnails .galleria-image").css("height","190px");                                                                           
       $(".galleria-thumbnails .galleria-image img").css("width","170px");                                                                        
        $(".galleria-thumbnails .galleria-image img").css("height","128px");
       // $(".galleria-thumbnails .galleria-image img").css("left","210px");
     //   $(".galleria-thumbnails .galleria-image img").css("top","150px");                                                     $(".galleria-thumbDesc").css("position","absolute");
          $(".galleria-thumbDesc").css("top","150px");                        
                                                                                                                                               
    });
                                                                                                                                            
});   


if($('body').hasClass('template-view')) {                                                                                                  
     Galleria.configure({ autoplay: %s,
           imageCrop: false,
 imageCrop: false,
thumbCrop: false                                                                                                                      
 });


}else{

 Galleria.configure({ imageCrop: false,
 imageCrop: false,
thumbCrop: false                                                                                                                                
 });


}
;

                                                                            
});

""" % (self.id, str(self.autoplay()).lower())


                                                                                                                     
