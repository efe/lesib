from django.db import models
from django.utils.translation import ugettext_lazy as _

from words.signals import initialize_words
from sentences.signals import set_of_rules, get_query_body


class Sentence(models.Model):
    content = models.CharField(_("Sentence"), max_length=255, blank=False)
    question = models.CharField(_("Question"), max_length=255, blank=True)
    query_body = models.TextField(_("Query Body"), blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def ask(self, question_type, changed_word):
        question = self.content
        question = question.replace(changed_word.content, question_type).replace(".", "")
        question += "?"
        Sentence.objects.filter(id=self.id).update(question=question)

    def get_word(self, content_type, tag, morphology):
        if not morphology:
            return self.words.filter(content_type=content_type, tag=tag).first()
        if not content_type:
            return self.words.filter(tag=tag, morphology__contains=morphology).first()
        if not tag:
            return self.words.filter(content_type=content_type, morphology__contains=morphology).first()
        else:
            return self.words.filter(content_type=content_type, tag=tag, morphology__contains=morphology).first()

models.signals.post_save.connect(get_query_body, sender=Sentence)
models.signals.post_save.connect(initialize_words, sender=Sentence)
models.signals.post_save.connect(set_of_rules, sender=Sentence)

