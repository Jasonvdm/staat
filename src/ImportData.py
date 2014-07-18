import csv


def get_sentiment_dictionary():
	sentiment_file = open("../data/inquirerbasic.csv", 'rU')
	return csv.DictReader(sentiment_file)


def get_tweets(hashtag):
	return tweets[hashtag]
	