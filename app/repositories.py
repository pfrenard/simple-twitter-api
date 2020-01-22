"""
    app/repositories.py
"""

class TweetRepository():
    def __init__(self):
        self.clear()

    def clear(self):
        self.tweets = []
        self.next_id = 0

    def add(self,tweet):

        self.next_id += 1
        self.tweets.append( tweet )
        tweet.id = self.next_id
        return self.next_id

    def get(self,id):
       my_ret = None
       for tweet in self.tweets:
           if tweet.id == id:
               my_ret = tweet
       return my_ret
