import csv


def get_sentiment_dictionary():
	sentiment_file = open("inquirerbasic.csv", 'rU')
	return csv.DictReader(sentiment_file)

