import praw
from requests import Session


session = Session()
session.verify = "/path/to/certfile.pem"
reddit = praw.Reddit(
    client_id="hW4Dme3gEM52fg",
    client_secret="RT3Ydd9tmWre3K_gy8uEzG8is2vFag",
    requestor_kwargs={"session": session},  # pass Session
    user_agent="botscript",
    username="bot",
)
for submission in reddit.subreddit("learnpython").hot(limit=10):
    print(submission.title)