from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """ Marker interface that defines a browser layer against which you can
    register views and viewlets.
    """
