import psycopg2

# add_repo_data_to_db(username, image, repo["name"], 
# repo["description"], repo["number_of_star"])
# INSERT INTO github_repo (username, user_image, repo_id, repo_name, repo_description, repo_star) VALUES ('a', 'b', 123, 'c', 'd', 1) ON CONFLICT (id) DO NOTHING;
def add_repo_data_to_db(username, user_image, repo_id, repo_name, repo_description, repo_star):
    # create connection
    # I don't want anyone see that
    # check this file on ec2 instance

    # Execute SQL
    with conn.cursor() as cur:
        cur.execute("INSERT INTO github_repo (username, user_image, repo_id, repo_name, repo_description, repo_star) " + 
                    "VALUES (%s, %s, %s, %s, %s, %s)" + "ON CONFLICT (repo_id) DO NOTHING", 
                    (username, user_image, repo_id, repo_name, repo_description, repo_star))
    # connection commit
    conn.commit()


