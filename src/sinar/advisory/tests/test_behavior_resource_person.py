# -*- coding: utf-8 -*-
from sinar.advisory.behaviors.resource_person import IResourcePersonMarker
from sinar.advisory.testing import SINAR_ADVISORY_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class ResourcePersonIntegrationTest(unittest.TestCase):

    layer = SINAR_ADVISORY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_resource_person(self):
        behavior = getUtility(IBehavior, 'sinar.advisory.resource_person')
        self.assertEqual(
            behavior.marker,
            IResourcePersonMarker,
        )
