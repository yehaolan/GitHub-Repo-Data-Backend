from __future__ import unicode_literals

import logging

from django.http import HttpResponse

from django.shortcuts import render

from github_api import *

logger = logging.getLogger("worker")

def crawl(request):
    logger.info("I am in add_crawl_point")
    logger.info(request)
    # get argument from request
    username = request.GET["username"]

    # get data from api with extract_data function
    data = extract_data(username) 

    logger.info("Result: {0}".format(json.dumps(data, indent=2)))
 
    return HttpResponse(json.dumps(data, indent=2))
    # return HttpResponse(json.dumps(data))


