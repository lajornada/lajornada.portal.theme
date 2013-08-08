from five import grok

#3rd party imports
from collective.nitf.content import INITF

from collective.nitf.browser import View

# Local imports
from plonetheme.sunburst.browser.interfaces import IThemeSpecific

from Products.ATContentTypes.interfaces import IATImage
from openmultimedia.contenttypes.content.video import IVideo

grok.templatedir("templates")


class NITFDefaultView(View):
    grok.context(INITF)
    grok.name('view')
    grok.template('nitf_view')
    grok.require('zope2.View')
    grok.layer(IThemeSpecific)

    def get_media(self):
        """ Return a list of object brains inside the NITF object.
        """
        media_types = ['Image', 'Video']

        return self._get_brains(media_types)

    def media_type(self, obj):
        media = ''
        if IATImage.providedBy(obj):
            media = 'image'

        if IVideo.providedBy(obj):
            media = 'video'

        return media

    def get_videos(self):
        media_types = ['Video']
        return self._get_brains(media_types)

    def get_video(self):
        videos = self.get_videos()
        result = None
        if videos:
            result = videos[0]
        return result