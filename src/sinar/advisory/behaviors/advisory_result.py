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


class IAdvisoryResultMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IAdvisoryResult(model.Schema):
    """
    """

    advisory_result = schema.TextLine(
        title=_(u'Advisory Result'),
        description=_(u'Result or impact of the advisory provided'),
        required=False,
    )


@implementer(IAdvisoryResult)
@adapter(IAdvisoryResultMarker)
class AdvisoryResult(object):
    def __init__(self, context):
        self.context = context

    @property
    def advisory_result(self):
        if safe_hasattr(self.context, 'advisory_result'):
            return self.context.advisory_result
        return None

    @advisory_result.setter
    def advisory_result(self, value):
        self.context.advisory_result = value
