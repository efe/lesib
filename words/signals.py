from words.models import Word


def initialize_words(sender, instance, created, **kwargs):
    """
    This signal separates the sentences to its words and save them one by one.
    """
    if created:
        word_list = instance.query_body.split("\n")
        for word in word_list:
            word = word.split("\t")
            position = word[0]
            content = word[1]
            stem = word[2]
            content_type = word[3]
            stem_type = word[4]
            morphology = word[5]
            numbering = word[6]
            tag = word[7]
            Word.objects.create(parent_sentence=instance, position=position, content=content, stem=stem,
                              content_type=content_type, stem_type=stem_type, morphology=morphology, numbering=numbering,
                              tag=tag)
