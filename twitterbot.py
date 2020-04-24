#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from random import randint
from credentials import *
from utils import *
import spotipy
from spotipy import oauth2
from spotipy.oauth2 import SpotifyClientCredentials
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

last_tweet_ids = [-1 for x in range(len(TWITTER_SEARCH_QUERIES))]

while True:
    for i, twitter_search_query in enumerate(TWITTER_SEARCH_QUERIES):
        try:
            try:
                print("Getting search tweets")
                search_tweets = tweepy.Cursor(api.search, q=twitter_search_query, result_type="recent").items(1)
            except:
                continue
            for tweet in search_tweets:
                if tweet.id in last_tweet_ids:
                    continue
                last_tweet_ids[i] = tweet.id
                if tweet.user.screen_name != BOT_SCREEN_NAME:
                    if not is_reply(tweet.text) and not is_retweet(tweet.text):
                        playlist = spotify.user_playlist(SPOTIFY_PLAYLIST_OWNER, SPOTIFY_PLAYLIST_ID)
                        idx = randint(0, len(playlist["tracks"]["items"]) - 1)
                        reply_text = playlist["tracks"]["items"][idx]["track"]["external_urls"]["spotify"]
                        if reply_text and reply_text != "":
                            try:
                                finalized_reply_text = finalize_reply_text(tweet.user.screen_name, tweet.text, reply_text)
                                api.update_status(finalized_reply_text, in_reply_to_status_id=tweet.id)
                                print(finalized_reply_text)
                                time.sleep(5)
                            except tweepy.TweepError as e:
                                print(e.reason)
        except:
            pass
        time.sleep(10)
