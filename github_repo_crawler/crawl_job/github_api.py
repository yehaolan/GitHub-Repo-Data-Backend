import urllib, json

import boto3

from db_accessor import *

def extract_data(username):
    # check whether search this user 2 min ago
    if visited_in_two_min(username):
        res = {}
        # message: 1  means visited in two min ago
        res["message"] = 1
        return res 

    githubURL = "https://api.github.com/users/{0}/repos".format(username)
    response = urllib.urlopen(githubURL)
    raw_data = json.loads(response.read())
 
    # when user not found
    if type(raw_data) is dict:
        # print type(raw_data)
        # message: 0  means visited in two min ago
        raw_data["message"] = 0
        # print raw_data
        return raw_data

    
    # data for each user
    data = {}
    # set username
    data["username"] = username
    # set image url
    if len(raw_data) == 0:
        data["image"] = "https://pbs.twimg.com/profile_images/600060188872155136/st4Sp6Aw.jpg"
    else:
        data["image"] = raw_data[0]["owner"]["avatar_url"]
    # store useful repo data for all repos of this user
    repos_data = []
    for repo in raw_data:
        repos_data += [parse_repo_data(repo)]

    data["repos_data"] = repos_data
    # message: 2  means visited in two min ago
    data["message"] = 2

    # add to db
    add_user_time_to_db(username)

    return data

def parse_repo_data(repo):
    result = {}
    result["name"] = repo["name"]
    result["description"] = repo["description"]
    result["number_of_star"] = repo["watchers_count"]
    result["repo_id"] = repo["id"]
    return result

if __name__ == "__main__":
    print json.dumps(extract_data("yehaolan"), indent=2)
    
