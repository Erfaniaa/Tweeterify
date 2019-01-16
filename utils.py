# -*- coding: utf-8 -*-
from credentials import *
import re
from random import randint
reply_texts = ["Let's listen to this song: ", "Let's play this: ", "Check out this song on Spotify: ", "I recommend this to you: ", "You can listen this song: ", "I suggest this song to you: "]

def remove_retweet_prefix(tweet_text):
	regex_string = r"RT @(.+?): (.+)"
	r = re.search(regex_string, tweet_text)
	if r:
		return r.group(2)
	else:
		return tweet_text

def remove_url_postfix(tweet_text):
	regex_string = r"(.+) (https:\/\/t\.co\/.+)"
	r = re.search(regex_string, tweet_text)
	if r:
		return r.group(1)
	else:
		return tweet_text

def is_retweet(tweet_text):
	regex_string = r"RT @(.+?): (.+)"
	r = re.search(regex_string, tweet_text)
	if r:
		return True
	else:
		return False

def is_reply(tweet_text):
	regex_string = r"@(.+?) "
	r = re.search(regex_string, tweet_text)
	if r and r.group(1) != BOT_SCREEN_NAME:
		return True
	else:
		return False

def remove_bot_screen_name_prefix(tweet_text):
	regex_string = r"@(.+?) (.+)"
	r = re.search(regex_string, tweet_text)
	if r:
		return r.group(2)
	else:
		return tweet_text

def finalize_reply_text(user_id, tweet_text, reply_text):
	idx = randint(0, len(reply_texts) - 1)
	ret = "@" + user_id + " " + reply_texts[idx]
	ret = ret + " " + reply_text
	return ret
