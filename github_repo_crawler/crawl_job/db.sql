CREATE TABLE GITHUB_REPO (
    username    TEXT,
    time        DOUBLE PRECISION,
    PRIMARY KEY (username)
);

CREATE INDEX usernamex   ON GITHUB_REPO (username);
CREATE INDEX timex   ON GITHUB_REPO (time);
