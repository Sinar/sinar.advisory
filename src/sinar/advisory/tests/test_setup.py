# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from sinar.advisory.testing import SINAR_ADVISORY_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that sinar.advisory is properly installed."""

    layer = SINAR_ADVISORY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sinar.advisory is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'sinar.advisory'))

    def test_browserlayer(self):
        """Test that ISinarAdvisoryLayer is registered."""
        from sinar.advisory.interfaces import (
            ISinarAdvisoryLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ISinarAdvisoryLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SINAR_ADVISORY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product('sinar.advisory')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if sinar.advisory is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'sinar.advisory'))

    def test_browserlayer_removed(self):
        """Test that ISinarAdvisoryLayer is removed."""
        from sinar.advisory.interfaces import \
            ISinarAdvisoryLayer
        from plone.browserlayer import utils
        self.assertNotIn(ISinarAdvisoryLayer, utils.registered_layers())
