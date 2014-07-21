import ImportData
import sys


def analyze_topic(topic):
	print "ANALYZING TOPIC: " + topic
	print "------------------------------"
	tweets = ImportData.pull_tweets(topic)
	score = 0
	for tweet in tweets:
		score += tweet.get_score()
	score /= len(tweets)
	print "# of Tweets: " + str(len(tweets))
	print "Tweet Score: " + str(score*100) + "% positve. \n"

if __name__ == '__main__':
	if (len(sys.argv) < 2):
	    print 'usage:\tSpamLord.py <topics>'
	    sys.exit(0)
	topic = ""
	for i in range(1,len(sys.argv)):topic += " " + sys.argv[i]
	topic = topic[1:]
	analyze_topic(topic)