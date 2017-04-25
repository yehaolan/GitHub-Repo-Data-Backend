# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import HttpResponse

from django.shortcuts import render

from github_api import *
from db_accessor import *

logger = logging.getLogger("worker")

def add_crawl_point(request):
    logger.info("I am in add_crawl_point")
    request_obj = json.loads(request.body)
    print request_obj
    name = request_obj["username"]
    data = extract_data(name) # TODO: change parameter to request_obj
    
    logger.info("Result: {0}".format(json.dumps(data, indent=2)))

    username = data["username"]
    image = data["image"]
    repos_data = data["repos_data"]
    for repo in repos_data:
        # INSERT INTO github_repo (username, user_image, repo_id, repo_name, repo_description, repo_star) VALUES ('a', 'b', 123, 'c', 'd', 1) ON CONFLICT (repo_id) DO NOTHING;
        add_repo_data_to_db(username, image, repo["repo_id"], repo["name"], 
                            repo["description"], repo["number_of_star"])

    return HttpResponse(json.dumps(data, indent=2))

