# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.shortcuts import render

from django.http import HttpResponse

logger = logging.getLogger("worker")

def add_crawl_point(request):
    logger.info("I am in crawl function")
    return HttpResponse("result")
