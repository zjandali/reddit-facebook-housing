import smtplib
import ssl
from typing import Set, Any
import praw
from facebook_scraper import get_posts

import TokenInfo

# Useful data keywords
keyWords: Set[str] = {"70", "housing", "data 100", "61c"}

# Configuring Reddit api
reddit = praw.Reddit(
    client_secret=TokenInfo.client_secret,
    client_id=TokenInfo.client_id,
    user_agent=TokenInfo.user_agent,
    username=TokenInfo.username,
)

# Berkeley Subreddit
submissions: Set[Any] = set(reddit.subreddit("berkeley").hot(limit=100))


def housing_n_schoo():
    # counters
    message = ''
    Redditi = 0
    Facebooki = 0

    # data
    for word in keyWords:
        for submission in submissions:
            if word in submission.title:
                message += "Reddit Post #" + str(Redditi) + ': \n' + submission.url + '\n\n\n'
                Redditi += 1
    for post in get_posts(group='ucberkeleyoffcampushousing', pages=1):
        message += "Facebook Post #" + str(Facebooki) + ': \n' + str(post.get('text')) + "\n\n " + str(
            post.get('post_url')) + str(post.get('url')) + '\n\n\n'
        Facebooki += 1

    # smtp Server
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "yzjandali@gmail.com"
    receiver_email = "matthewsim2019@gmail.com"
    password = TokenInfo.password

    # Email to be sent
    message = message.encode()
    print(message)

    # Server config
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

# run
housing_n_schoo()

#Next step is to incorporate ML/ai/Data_sci libs
