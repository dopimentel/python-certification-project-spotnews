from django.core.exceptions import ValidationError


class Validate:
    @classmethod
    def two_words(cls, value):
        if len(value) <= 200:
            words = value.split()
            if len(words) != 2:
                raise ValidationError(
                    "O título deve conter pelo menos 2 palavras."
                )
