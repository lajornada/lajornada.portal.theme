# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.cover.tiles.list import ListTile, IListTile


class INitfSecondaryList(IListTile):
    """
    """


class NitfSecondaryList(ListTile):

    index = ViewPageTemplateFile("templates/nitf_secondary_list.pt")

    is_configurable = False
    is_droppable = True

    limit = 4

    def accepted_ct(self):
        valid_ct = ['collective.nitf.content', ]
        return valid_ct
