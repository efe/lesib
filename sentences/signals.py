

def set_of_rules(sender, instance, **kwargs):
    """
    This signal find right question to ask.
    get_word(content_type, tag, morphology)
    """
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
    # Neresi?
    elif instance.get_word("Noun", None, "Acc"):
        w = instance.get_word("Noun", None, "Acc")
        instance.ask("neyle", w)
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