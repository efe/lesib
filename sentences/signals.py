import requests

from keys.ITU_API_KEY import ITU_API_KEY


def get_query_body(sender, instance, created, **kwargs):
    if created:
        tool = 'pipelineNoisy'
        url = 'http://tools.nlp.itu.edu.tr/SimpleApi?tool=%s&input=%s&token=%s' % (tool, instance.content, ITU_API_KEY)
        q = requests.get(url).text
        instance.query_body = q
        instance.save()

def set_of_rules(sender, instance, created, **kwargs):
    """
    This signal find right question to ask.
    get_word(content_type, tag, morphology)
    """
    if created:
        # Nereden?
        if instance.get_word("Noun", None, "Abl"):
            w = instance.get_word("Noun", None, "Abl")
            instance.ask("nereden", w)
        # Nerede?
        elif instance.get_word("Noun", None,"Loc"):
            w = instance.get_word("Noun", None, "Loc")
            instance.ask("nerede", w)
        # Neyle?
        elif instance.get_word("Noun", None, "Ins"):
            w = instance.get_word("Noun", None, "Ins")
            instance.ask("neyle", w)
        # Nereye?
        elif instance.get_word("Noun", None, "Dat"):
            w = instance.get_word("Noun", None, "Dat")
            instance.ask("nereye", w)

        # Ne yaptım?
        elif instance.get_word("Verb", "PREDICATE", "1sg"):
            w = instance.get_word("Verb", "PREDICATE", "1sg")
            instance.ask("ne yaptım", w)
        elif instance.get_word("Verb", "PREDICATE", "2sg"):
            w = instance.get_word("Verb", "PREDICATE", "sg")
            instance.ask("ne yaptın", w)
        elif instance.get_word("Verb", "PREDICATE", "sg"):
            w = instance.get_word("Verb", "PREDICATE", "sg")
            instance.ask("ne yaptı", w)

        # Ne yaptık?
        elif instance.get_word("Verb", "PREDICATE", "1pl"):
            w = instance.get_word("Verb", "PREDICATE", "1sg")
            instance.ask("ne yaptık", w)
        elif instance.get_word("Verb", "PREDICATE", "2pl"):
            w = instance.get_word("Verb", "PREDICATE", "sg")
            instance.ask("ne yaptınız", w)
        elif instance.get_word("Verb", "PREDICATE", "3pl"):
            w = instance.get_word("Verb", "PREDICATE", "sg")
            instance.ask("ne yaptılar", w)

        # Kimin?
        elif instance.get_word("Noun", "SUBJECT", "Gen"):
            w = instance.get_word("Noun", "SUBJECT", "Gen")
            instance.ask("kimin", w)
        # Kim?
        elif instance.get_word("Noun", "POSSESSOR", None):
            w = instance.get_word("Noun", "POSSESSOR", None)
            instance.ask("kim", w)
        # Kim?
        elif instance.get_word("Pron", "SUBJECT", None):
            w = instance.get_word("Pron", "SUBJECT", None)
            instance.ask("kim", w)
        # Ne?
        elif instance.get_word("Noun", "SUBJECT", None):
            w = instance.get_word("Noun", "SUBJECT", None)
            instance.ask("ne", w)



        # Low Performance :(
        elif instance.get_word(None, "SUBJECT", None):
            w = instance.get_word(None, "SUBJECT", None)
            instance.ask("kim", w)
        elif instance.get_word(None, "SUBJECT", None):
            w = instance.get_word(None, "SUBJECT", None)
            instance.ask("ne", w)
        elif instance.get_word(None, "MODIFIER", None):
            w = instance.get_word(None, "MODIFIER", None)
            instance.ask("nasıl", w)
        # Neyi?
        elif instance.get_word("Noun", None, "Acc"):
            w = instance.get_word("Noun", None, "Acc")
            instance.ask("neyi", w)
