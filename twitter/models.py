from django.db import models


class Tweet(models.Model):
    url = models.URLField()
    sentence = models.ForeignKey('sentences.Sentence', related_name="tweet")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sentence
