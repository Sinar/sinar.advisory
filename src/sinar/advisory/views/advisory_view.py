# -*- coding: utf-8 -*-

# from sinar.advisory import _
from plone.dexterity.browser.view import DefaultView
from zope.interface import Interface

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IAdvisoryView(Interface):
    """ Marker Interface for IAdvisoryView"""


class AdvisoryView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('advisory_view.pt')

    def __call__(self):
        # Implement your own actions:
        return super(AdvisoryView, self).__call__()
