import requests
from django.db import models
from django.utils.translation import ugettext_lazy as _

from keys.ITU_API_KEY import ITU_API_KEY
from words.signals import initialize_words


class Sentence(models.Model):
    content = models.CharField(_("Sentence"), max_length=255, blank=False)
    question = models.CharField(_("Question"), max_length=255, blank=True)
    query_body = models.TextField(_("Query Body"), blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        self.query_body = self.get_query_body()
        super(Sentence, self).save(*args, **kwargs)

    def get_query_body(self):
        tool = 'pipelineNoisy'
        url = 'http://tools.nlp.itu.edu.tr/SimpleApi?tool=%s&input=%s&token=%s' % (tool, self.content, ITU_API_KEY)
        return requests.get(url).text

models.signals.post_save.connect(initialize_words, sender=Sentence)
