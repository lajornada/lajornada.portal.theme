# -*- coding: utf-8 -*-
from zope.schema import TextLine

from plone.uuid.interfaces import IUUID
from plone.app.uuid.utils import uuidToObject
from plone.tiles.interfaces import ITileDataManager

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.cover.tiles.base import IPersistentCoverTile
from collective.cover.tiles.base import PersistentCoverTile


class INitfTile(IPersistentCoverTile):

    uuid = TextLine(title=u'NITF uuid',
                    readonly=True)

    def populate_with_object(obj):
        """
        This method will take a CT collective.nitd as parameter, and it will store a
        reference to it.
        """

    def delete():
        """
        This method removes the persistent data created for this tile
        """

    def accepted_ct():
        """
        Return a list of supported content types.
        """

    def has_data():
        """
        A method that return True if the tile have a data.
        """


class NitfTile(PersistentCoverTile):

    index = ViewPageTemplateFile("templates/nitf_tile.pt")

    is_configurable = False
    is_droppable = True
    is_editable = False

    def result(self):
        uuid = self.data.get('uuid', None)
        if uuid is not None:
            obj = uuidToObject(uuid)
            return obj

    def populate_with_object(self, obj):
        super(NitfTile, self).populate_with_object(obj)

        uuid = IUUID(obj, None)
        data_mgr = ITileDataManager(self)
        data_mgr.set({'uuid': uuid})

    def delete(self):
        data_mgr = ITileDataManager(self)
        data_mgr.delete()

    def accepted_ct(self):
        valid_ct = ['collective.nitf.content']
        return valid_ct

    def has_data(self):
        uuid = self.data.get('uuid', None)
        return uuid is not None

class INitfSecondaryTile(IPersistentCoverTile):

    uuid = TextLine(title=u'NITF uuid',
                    readonly=True)

    def populate_with_object(obj):
        """
        This method will take a CT collective.nitd as parameter, and it will store a
        reference to it.
        """

    def delete():
        """
        This method removes the persistent data created for this tile
        """

    def accepted_ct():
        """
        Return a list of supported content types.
        """

    def has_data():
        """
        A method that return True if the tile have a data.
        """


class NitfSecondaryTile(PersistentCoverTile):

    index = ViewPageTemplateFile("templates/nitf_secondary_tile.pt")

    is_configurable = False
    is_droppable = True
    is_editable = False

    def result(self):
        uuid = self.data.get('uuid', None)
        if uuid is not None:
            obj = uuidToObject(uuid)
            return obj

    def populate_with_object(self, obj):
        super(NitfSecondaryTile, self).populate_with_object(obj)

        uuid = IUUID(obj, None)
        data_mgr = ITileDataManager(self)
        data_mgr.set({'uuid': uuid})

    def delete(self):
        data_mgr = ITileDataManager(self)
        data_mgr.delete()

    def accepted_ct(self):
        valid_ct = ['collective.nitf.content']
        return valid_ct

    def has_data(self):
        uuid = self.data.get('uuid', None)
        return uuid is not None

class INitfTertiaryTile(IPersistentCoverTile):

    uuid = TextLine(title=u'NITF uuid',
                    readonly=True)

    def populate_with_object(obj):
        """
        This method will take a CT collective.nitd as parameter, and it will store a
        reference to it.
        """

    def delete():
        """
        This method removes the persistent data created for this tile
        """

    def accepted_ct():
        """
        Return a list of supported content types.
        """

    def has_data():
        """
        A method that return True if the tile have a data.
        """


class NitfTertiaryTile(PersistentCoverTile):

    index = ViewPageTemplateFile("templates/nitf_tertiary_tile.pt")

    is_configurable = False
    is_droppable = True
    is_editable = False

    def result(self):
        uuid = self.data.get('uuid', None)
        if uuid is not None:
            obj = uuidToObject(uuid)
            return obj

    def populate_with_object(self, obj):
        super(NitfTertiaryTile, self).populate_with_object(obj)

        uuid = IUUID(obj, None)
        data_mgr = ITileDataManager(self)
        data_mgr.set({'uuid': uuid})

    def delete(self):
        data_mgr = ITileDataManager(self)
        data_mgr.delete()

    def accepted_ct(self):
        valid_ct = ['collective.nitf.content']
        return valid_ct

    def has_data(self):
        uuid = self.data.get('uuid', None)
        return uuid is not None


class INitfSecondaryBigImgTile(IPersistentCoverTile):

    uuid = TextLine(title=u'NITF uuid',
                    readonly=True)

    def populate_with_object(obj):
        """
        This method will take a CT collective.nitd as parameter, and it will store a
        reference to it.
        """

    def delete():
        """
        This method removes the persistent data created for this tile
        """

    def accepted_ct():
        """
        Return a list of supported content types.
        """

    def has_data():
        """
        A method that return True if the tile have a data.
        """


class NitfSecondaryBigImgTile(PersistentCoverTile):

    index = ViewPageTemplateFile("templates/nitf_secondarybigimg_tile.pt")

    is_configurable = False
    is_droppable = True
    is_editable = False

    def result(self):
        uuid = self.data.get('uuid', None)
        if uuid is not None:
            obj = uuidToObject(uuid)
            return obj

    def populate_with_object(self, obj):
        super(NitfSecondaryBigImgTile, self).populate_with_object(obj)

        uuid = IUUID(obj, None)
        data_mgr = ITileDataManager(self)
        data_mgr.set({'uuid': uuid})

    def delete(self):
        data_mgr = ITileDataManager(self)
        data_mgr.delete()

    def accepted_ct(self):
        valid_ct = ['collective.nitf.content']
        return valid_ct

    def has_data(self):
        uuid = self.data.get('uuid', None)
        return uuid is not None
