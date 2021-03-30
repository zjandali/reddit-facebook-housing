import smtplib
import ssl
from typing import Set, Any
import praw
from facebook_scraper import get_posts

import TokenInfo

keyWords: Set[str] = {"70", "housing", "data 100", "61c"}

reddit = praw.Reddit(
    client_id=TokenInfo.client_id,
    client_secret=TokenInfo.client_secret,
    user_agent=TokenInfo.user_agent,
    username=TokenInfo.username,
)
submissions: Set[Any] = set(reddit.subreddit("berkeley").hot(limit=100))


def housing_n_schoo():
    message = ''

    for word in keyWords:
        for submission in submissions:
            if word in submission.title:
                message += '\n' + submission.url
    for post in get_posts(group='ucberkeleyoffcampushousing', pages=1):
        message += '\n' + 'NEWPOST ' + str(post.get('text')) + " " + str(post.get('post_url'))

    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "yzjandali@gmail.com"
    receiver_email = "yzjandali@gmail.com"
    password = TokenInfo.password

    message = message.encode()
    print(message)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


housing_n_schoo()
