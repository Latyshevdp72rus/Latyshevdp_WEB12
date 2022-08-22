import re
from django.core.exceptions import ValidationError


def validation_stand(stand_name):
    if re.fullmatch(r'[A-ZА-ЯЁ0-9!?:-].*', stand_name):
        return stand_name
    else:
        ValidationError(
            message="не соответствует требованиям: (A-ZА-ЯЁ0-9!?:-)"
        )
