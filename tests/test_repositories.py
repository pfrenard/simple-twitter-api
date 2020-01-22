# tests/test_repositories.py
from unittest import TestCase
from app.models import Tweet
from app.repositories import TweetRepository  # We will code our `TweetRepositories` class in `app/repositories.py`

class TestTweetRepositories(TestCase):

    def test_instance_variables(self):
        repo = TweetRepository()
        self.assertEqual(repo.tweets, [])

    def test_add_tweet(self):
        # add, return id
        repo = TweetRepository()
        tweet = Tweet("tweet")
        repo.add(tweet)
        print(tweet)
        self.assertEqual(len(repo.tweets), 1)

    def test_auto_increment(self):
        repo = TweetRepository()
        first_tweet = Tweet("Tweet 1")
        second_tweet = Tweet("Tweet 2")

        repo.add(first_tweet)
        self.assertEqual(first_tweet.id,1)

        repo.add(second_tweet)
        self.assertEqual(second_tweet.id,2)

    def test_get_tweet(self):
        # get tweet from id
        repo = TweetRepository()
        tweet = Tweet("a new tweet")

        repo.add(tweet)

        self.assertEqual(tweet, repo.get(tweet.id))
        self.assertIsNone(repo.get(2))

