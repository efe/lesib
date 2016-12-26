from django.contrib import admin
from sentences.models import Sentence
from words.models import Word


class WordsInline(admin.TabularInline):
    model = Word
    readonly_fields = ('content', 'stem', 'content_type', 'stem_type', 'morphology', 'position', 'tag', 'numbering',)
    max_num = 0
    can_delete = False


class SentenceAdmin(admin.ModelAdmin):
    inlines = [
        WordsInline,
    ]
    readonly_fields = ('question', 'query_body', 'date')
admin.site.register(Sentence, SentenceAdmin)
