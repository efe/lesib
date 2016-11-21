from django.db import models
from django.utils.translation import ugettext_lazy as _


class Word(models.Model):
    parent_sentence = models.ForeignKey('sentences.Sentence', related_name="words")
    content = models.CharField(_("Word"), max_length=255)
    stem = models.CharField(_("Stem"), max_length=255)
    content_type = models.CharField(_("Type of the word"), max_length=255)
    stem_type = models.CharField(_("Type of the stem"), max_length=255)
    morphology = models.CharField(_("Morphology"), max_length=255)
    position = models.PositiveSmallIntegerField(_("Postion in the parent sentence"))
    numbering = models.PositiveSmallIntegerField()
    tag = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s, %s" % (self.content, self.parent_sentence)


