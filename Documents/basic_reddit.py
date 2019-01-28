#!/usr/bin/env python3

"""
@author: jatanloya

"""
import praw

reddit = praw.Reddit(client_id='goes here',
                     client_secret='goes here',
                     password='goes here',
                     user_agent='goes here',
                     username='goes here')
 
for submission in reddit.subreddit('goes here').hot(limit=20):
    print(submission.title)
    print(submission.selftext)
