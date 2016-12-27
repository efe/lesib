import json

from django.db import models
from TwitterAPI import TwitterAPI
from keys.TWITTER_KEY import access_token_secret, access_token, consumer_secret, consumer_key
from sentences.models import Sentence


class Tweet(models.Model):
    url = models.URLField()
    sentence = models.ForeignKey('sentences.Sentence', related_name="tweet")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sentence

    def save(self, *args, **kwargs):
        api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
        r = api.request('statuses/show/:%d' % 210462857140252672)
        d = json.loads(r.text)
        d = d["text"]
        sentence = Sentence.objects.create(content=d)
        super(Tweet, self).save(*args, **kwargs)
