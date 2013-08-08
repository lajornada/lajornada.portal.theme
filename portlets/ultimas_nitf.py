# -*- coding: utf-8 -*-

from Acquisition import aq_inner
from plone.app.layout.navigation.root import getNavigationRootObject
from plone.app.portlets.cache import render_cachekey
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from Products.CMFCore.utils import getToolByName
from zope import schema
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements



class IUltimas_NitfPortlet(IPortletDataProvider):
    """
    A portlet which shows the latest NITF created and can be filtered
    by section.
    """



    limit = schema.Int(
        title=u"Limit",
        description=u"Specify the maximum number of items to show in the "
                      u"portlet. Leave this blank to show all items.",
        default=10,
        required=False)

    pretty_date = schema.Bool(
        title=u'Pretty dates',
        description=u"Show dates in a pretty format (ie. '4 hours ago').",
        default=True,
        required=False)



class Assignment(base.Assignment):
    """
    Portlet assignment.
    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IUltimas_NitfPortlet)

    

    def __init__(self,
                 limit=10,
                 pretty_date=True,
                 ):


        self.limit = limit
        self.pretty_date = pretty_date


    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen. Here, we use the title that the user gave.
        """
        return u"Ultimos elementos NITF"


class Renderer(base.Renderer):

    render = ViewPageTemplateFile('ultimas_nitf.pt')

    def result(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        self.all_elements = catalog({'portal_type': 'collective.nitf.content',
                                     'review_state': 'published',
                                     'sort_on' : 'effective',
                                     'sort_order': 'descending',
                                     'sort_limit':self.data.limit})
        return self.all_elements

    def get_date(self, obj):
        #import pdb; pdb.set_trace()
        return obj.effective().strftime("%H.%M")

class AddForm(base.AddForm):

    form_fields = form.Fields(IUltimas_NitfPortlet)

    label = u"Agregar los ultimos elementos NITF al porlet"
    description = u"Este Portlet muestra una lista con los ultimos elementos NITF creados. "

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):

    form_fields = form.Fields(IUltimas_NitfPortlet)

    label = u"Agregar los ultimos elementos NITF al porlet"
    description = u"Este Portlet muestra una lista con los ultimos elementos NITF creados. "