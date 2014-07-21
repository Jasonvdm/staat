import csv
import re
import sys
import twitter
import Tweet

def get_sentiment_dictionary():
	sentiment_file = open("../data/inquirerbasic.csv", 'rU')
	reader = csv.DictReader(sentiment_file)
	sentiment_dict = dict()

	for row in reader:
		key = row['Entry'].lower()
		sentiment_dict[key] = row
	return sentiment_dict


def import_tweets():
	tweet_dictionary = dict()
	raw_tweets = open("../data/tweets.txt", 'r')
	for line in raw_tweets:
		hashtag = line[:line.find(" ")]
		full_tweets = line[line.find(" ")+1:]
		final_tweets = []
		for tweet in full_tweets.split("||"):
			if tweet != '': final_tweets.append(curate_line(tweet))
		tweet_dictionary[hashtag.lower()] = final_tweets
	return tweet_dictionary
	

def pull_tweets(hashtag):
	print hashtag
	api = twitter.Api(consumer_key='AHVsVuYleKQGpcE4EzZONZ4TF',
                      consumer_secret='SBrOKeoM2thuZW7FUQcXSZQA5Qx6qAIdAyioBB3hWVMGpJ2NWJ',
                      access_token_key='45966388-kh2vJceOPuyTAqG2IF88ca21zZdUfhQptT9TWH0dq',
                      access_token_secret='0Imzz1yic0XSIuhgfLWeQVzWSUxigmLVeGzcgkYyd57hX')

	search = api.GetSearch(term=hashtag, lang='en', result_type='recent', count=5, max_id='')
	final_tweets = []
	for tweet in search:
		final_tweets.append(Tweet(tweet.id, text.text.encode('utf-8'), tweet.retweet_count, tweet.favorited, tweet.user.user_location))
	return final_tweets
	# final_tweets = []
	# for t in search:
	# 	print t
 # 		tweet_text =  curate_line(t.text.encode('utf-8'))
 # 		final_tweets.append(tweet_text)
 # 	return final_tweets
 	



def get_tweets(hashtag="#mh17"):
	hashtag = hashtag.lower()
	tweets = import_tweets()
	return tweets[hashtag]
	

def curate_line(tweet):
	return re.sub('[^\ \w]', '', tweet)
	


"""
commandline interface takes a directory name and gold file.
It then processes each file within that directory and extracts any
matching e-mails or phone numbers and compares them to the gold file
"""
if __name__ == '__main__':
    pull_tweets()