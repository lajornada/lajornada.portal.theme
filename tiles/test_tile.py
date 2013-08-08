# -*- coding: utf-8 -*-
from zope.interface import implements

from zope import schema

from plone.tiles.interfaces import ITileDataManager

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.cover.tiles.base import IPersistentCoverTile
from collective.cover.tiles.base import PersistentCoverTile


class ITestTile(IPersistentCoverTile):

    name = schema.TextLine(
        title= u'a name',
        required=False,
    )

    def delete():
        """
        This method removes the persistent data created for this tile
        """

    def get_name():
        """
        Get the stored name.
        """

    def accepted_ct():
        """
        Check wich content types are accepted.
        """


class TestTile(PersistentCoverTile):

    index = ViewPageTemplateFile("templates/test_tile.pt")
    implements(IPersistentCoverTile)
    is_configurable = False
    is_droppable = False
    is_editable = True

    def get_name(self):
        return self.data['name']

    def delete(self):
        data_mgr = ITileDataManager(self)
        data_mgr.delete()

    def accepted_ct(self):
        return None