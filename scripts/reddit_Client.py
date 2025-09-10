# Reddit Sentiment Analysis Project
# Author: Zuha Farooq Sofi (based on template by Jeffrey Chan, RMIT University, 2023)

import sys
import praw


def redditClient():
    """
        Setup Reedit API authentication.
        Replace username, secrets and passwords with your own.

        @returns: praw Reedit object
    """

    try:
        #
        # TODO: you specify with your details
        #
        clientId = ""
        clientSecret = ""
        password = ""
        userName = ""
        userAgents = 'client for SNAM2024'

        redditClient = praw.Reddit(client_id = "YOUR_CLIENT_ID",
                                    client_secret = "YOUR_CLIENT_SECRET",
                                    password = "YOUR_PASSWORD",
                                    username = "YOUR_USERNAME",
                                    user_agent = userAgents)
    except KeyError:
        sys.stderr.write("Key or secret token are invalid.\n")
        sys.exit(1)


    return redditClient
