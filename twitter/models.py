import json

from django.db import models
from django.utils.translation import ugettext_lazy as _
from TwitterAPI import TwitterAPI
from keys.TWITTER_KEY import access_token_secret, access_token, consumer_secret, consumer_key
from sentences.models import Sentence


class Tweet(models.Model):
    tweet_id = models.CharField(_("Id of Tweet"), max_length=255, blank=True, help_text="https://twitter.com/efeoge/status/748450479600959488 için 748450479600959488")
    sentence = models.ForeignKey('sentences.Sentence', related_name="tweet", blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sentence.content

    def save(self, *args, **kwargs):
        api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
        r = api.request('statuses/show/:%s' % self.tweet_id)
        d = json.loads(r.text)
        d = d["text"]
        self.sentence = Sentence.objects.create(content=d)
        super(Tweet, self).save(*args, **kwargs)
