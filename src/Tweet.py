from enum import Enum
import ImportData

class Tweet:

	Polarity = Enum(Positive, Negative, Neutral)
	sentiment_dict = ImportData.get_sentiment_dictionary()
 
	def __init__(self, tweet_id, text, retweet_count, favorited, user_location):
        self.id = tweet_id
        self.text = text
        self.retweet_count = retweet_count
        self.favorited = favorited
        self.user_location = user_location

        self.score = 0
        self.num_pos = 0
        self.num_neg = 0
        self.pos_words = []
        self.neg_words = []
        self.tweet_polarity = Polarity.Neutral

        smoothen_tweet()
        parse_tweet()
        calculate_tweet_score()

    def get_score(self):
    	return self.score


    def calculate_tweet_score(self):
        self.score = self.num_pos()/float(self.num_pos + self.num_neg)
        if self.score > 0.5: self.tweet_polarity = Polarity.Positive
        if self.score < 0.5: self.tweet_polarity = Polarity.Negative 


    def parse_tweet(self):
    	for word in self.text.split():
    		if is_positive(word):
    			self.pos_words.append(word)
    			self.num_pos += 1
    		if is_negative(word):
    			self.neg_words.append(word)
    			self.num_neg += 1

    def smoothen_tweet(self):
        self.text = re.sub('[^\ \w]', '', self.text)

    def is_positive(self,word):
        if word in sentiment_dict: 
            if sentiment_dict[word]["Positiv"] != '': 
                return True
        else:
            new_word = word +"#" + str(1)
                if new_word in sentiment_dict:
                    if sentiment_dict[new_word]["Positiv"] != '': 
                        return True
        return False

     def is_negative(self,word):
        if word in sentiment_dict: 
            if sentiment_dict[word]["Negativ"] != '': 
                return True
        else:
            new_word = word +"#" + str(1)
                if new_word in sentiment_dict:
                    if sentiment_dict[new_word]["Negativ"] != '': 
                        return True
        return False
