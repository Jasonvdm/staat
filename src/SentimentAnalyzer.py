import ImportData
import sys


def analyze_topic(topic):
	tweets = ImportData.pull_tweets(topic)
	score = 0
	for tweet in tweets:
		score += tweet.get_score()
	score /= len(tweets)

if __name__ == '__main__':
	if (len(sys.argv) < 2):
	    print 'usage:\tSpamLord.py <topics>'
	    sys.exit(0)
	topic = ""
	for i in range(1,len(sys.argv)):topic += " " + sys.argv[i]
	topic = topic[1:]
	print topic
	analyze_topic(topic)