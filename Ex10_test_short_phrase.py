import requests


class TestShortPhrase:
    def test_short_phrase(self):
        phrase = input("Set a phrase: ")
        max_phrase_len = 15
        actual_phrase_len = len(phrase)

        assert actual_phrase_len < max_phrase_len, f"Phrase length must be at least {max_phrase_len} characters"
