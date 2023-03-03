# -*- coding: utf-8 -*-

from sinar.advisory import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class IResourcePersonMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IResourcePerson(model.Schema):
    """
    """

    resource_person = schema.TextLine(
        title=_(u'Resource person'),
        description=_(u'Name of resource person who provided advisory'),
        required=False,
        )



@implementer(IResourcePerson)
@adapter(IResourcePersonMarker)
class ResourcePerson(object):
    def __init__(self, context):
        self.context = context

    @property
    def resource_person(self):
        if safe_hasattr(self.context, 'resource_person'):
            return self.context.resource_person
        return None

    @resource_person.setter
    def resource_person(self, value):
        self.context.resource_person = value
