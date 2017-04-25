# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import HttpResponse

from django.shortcuts import render

from github_api import *

logger = logging.getLogger("worker")

def add_crawl_point(request):
    logger.info("I am in crawl function ")
    request_obj = json.loads(request.body)
    print request_obj
    name = request_obj["username"]
    data = extract_data(name) # TODO: change parameter to request_obj
    
    logger.info("Result: {0}".format(json.dumps(data, indent=2)))

    return HttpResponse(json.dumps(data, indent=2))

