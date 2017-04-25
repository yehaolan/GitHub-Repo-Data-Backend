-- how I create table in database
CREATE TABLE GITHUB_REPO (
    username             TEXT,
    user_image           TEXT,
    repo_id              INT,
    repo_name            TEXT,
    repo_description     TEXT,
    repo_star            INT,
    PRIMARY KEY (repo_id)
);

CREATE INDEX usernamex          ON GITHUB_REPO (username);
CREATE INDEX user_imagex        ON GITHUB_REPO (user_image);
CREATE INDEX repo_idx           ON GITHUB_REPO (repo_id);
CREATE INDEX repo_namex         ON GITHUB_REPO (repo_name);
CREATE INDEX repo_descriptionx  ON GITHUB_REPO (repo_description);
CREATE INDEX repo_starx         ON GITHUB_REPO (repo_star);
