# -*- coding: utf-8 -*-
from sinar.advisory.content.advisory import IAdvisory  # NOQA E501
from sinar.advisory.testing import SINAR_ADVISORY_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class AdvisoryIntegrationTest(unittest.TestCase):

    layer = SINAR_ADVISORY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_advisory_schema(self):
        fti = queryUtility(IDexterityFTI, name='Advisory')
        schema = fti.lookupSchema()
        self.assertEqual(IAdvisory, schema)

    def test_ct_advisory_fti(self):
        fti = queryUtility(IDexterityFTI, name='Advisory')
        self.assertTrue(fti)

    def test_ct_advisory_factory(self):
        fti = queryUtility(IDexterityFTI, name='Advisory')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IAdvisory.providedBy(obj),
            u'IAdvisory not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_advisory_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Advisory',
            id='advisory',
        )

        self.assertTrue(
            IAdvisory.providedBy(obj),
            u'IAdvisory not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('advisory', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('advisory', parent.objectIds())

    def test_ct_advisory_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Advisory')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_advisory_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Advisory')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'advisory_id',
            title='Advisory container',
        )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type='Document',
            title='My Content',
        )
        self.assertTrue(
            obj,
            u'Cannot add {0} to {1} container!'.format(obj.id, fti.id)
        )
