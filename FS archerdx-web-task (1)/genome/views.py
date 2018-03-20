# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def upload(request):
    """Handle uploads of files that specify genomic regions"""
    # TODO: Handle uploads
    return render(request, "genome/upload.html")
