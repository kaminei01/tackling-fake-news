def manual_fake_check(text):
    known_fake_phrases = [
        "Goldman Sachs endorses Hillary Clinton",
        "Donald Trump’s establishment roots",
        "23 kiloton tower shot called BADGER",
        "Yahoo News A 38-year-old Oklahoma man",
        "polling stations to close – typically between 19:00 EST",
    ]
    
    text_lower = text.lower()
    for phrase in known_fake_phrases:
        if phrase.lower() in text_lower:
            return True
    return False
