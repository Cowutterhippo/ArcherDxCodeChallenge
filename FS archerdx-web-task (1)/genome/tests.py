# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import resolve, reverse
from django.test import TestCase

from .BedFileUploadController import upload


class UploadTest(TestCase):

    def test_upload_url_resolves_to_upload_view(self):
        found = resolve(reverse('genome:upload'))
        self.assertEqual(found.func, upload)
