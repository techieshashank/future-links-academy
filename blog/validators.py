from django.core.exceptions import ValidationError

BY = ['Shashank']

def validate_by(value):
    cat = value.capitalize()
    if not value in BY and not cat in BY:
        raise ValidationError(f"{value} not authorised to enter post")