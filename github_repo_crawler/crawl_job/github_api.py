import urllib, json

def extract_data(username):
    githubURL = "https://api.github.com/users/{0}/repos".format(username)
    response = urllib.urlopen(githubURL)
    raw_data = json.loads(response.read())
 
    # when user not found
    if type(raw_data) is dict:
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
    
