# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index_front(request):

    return render (request, "front/index.html", locals())

