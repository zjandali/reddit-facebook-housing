#!/usr/bin/python
import praw

reddit = praw.Reddit('bot1')

x = 0

for submission in reddit.subreddit("berkeley").search("CS70"):
    print(submission.title)
    print(submission.selftext + "\n\n")
    x += 1
    if x == 4:
        break
