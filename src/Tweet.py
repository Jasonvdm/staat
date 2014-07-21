import ImportData
import re

class Tweet:
	def __init__(self, tweet_id, text, retweet_count, favorited, user_location, sentiment_dict):
            self.id = tweet_id
            self.text = text
            self.retweet_count = retweet_count
            self.favorited = favorited
            self.user_location = user_location

            self.score = 0.5
            self.num_pos = 0
            self.num_neg = 0
            self.pos_words = []
            self.neg_words = []
            self.tweet_polarity = "Neutral"

            self.sentiment_dict = sentiment_dict

            self.smoothen_tweet()
            self.parse_tweet()
            self.calculate_tweet_score()

        def get_score(self):
        	return self.score

        def get_text(self):
            return self.text

        def get_positive_words(self):
            return self.pos_words

        def get_negative_words(self):
            return self.neg_words


        def calculate_tweet_score(self):
            if self.num_pos + self.num_neg != 0:
                self.score = self.num_pos/float(self.num_pos + self.num_neg)
            if self.score > 0.5: self.tweet_polarity = "Positive"
            if self.score < 0.5: self.tweet_polarity = "Negative"


        def parse_tweet(self):
        	for word in self.text.split():
        		if self.is_positive(word):
        			self.pos_words.append(word)
        			self.num_pos += 1
        		if self.is_negative(word):
        			self.neg_words.append(word)
        			self.num_neg += 1

        def smoothen_tweet(self):
            self.text = re.sub('[^\ \w]', '', self.text)

        def is_positive(self,word):
            if word in self.sentiment_dict: 
                if self.sentiment_dict[word]["Positiv"] != '': 
                    return True
            else:
                new_word = word +"#" + str(1)
                if new_word in self.sentiment_dict:
                    if self.sentiment_dict[new_word]["Positiv"] != '': 
                        return True
            return False

        def is_negative(self,word):
            if word in self.sentiment_dict: 
                if self.sentiment_dict[word]["Negativ"] != '': 
                    return True
                else:
                    new_word = word +"#" + str(1)
                    if new_word in self.sentiment_dict:
                        if self.sentiment_dict[new_word]["Negativ"] != '': 
                            return True
            return False
