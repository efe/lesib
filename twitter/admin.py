from django.contrib import admin

from sentences.models import Sentence
from .models import Tweet

admin.site.register(Tweet)


# class SentenceInline(admin.TabularInline):
#     model = Sentence
#     readonly_fields = ('content', 'question',)
#     max_num = 0
#     can_delete = False
#
#
# class TweetAdmin(admin.ModelAdmin):
#     inlines = [
#         SentenceInline,
#     ]
#
# admin.site.register(Tweet, TweetAdmin)
