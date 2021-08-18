from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator
from datetime import datetime

# Create your models here.
class User_Authentication(models.Model):
    # Email of the user
    email = models.EmailField(unique=True, blank=True,)
    # Phone number of the user
    phone = PhoneNumberField(blank=True)
    # password of the user account
    password = models.CharField(validators=[MinLengthValidator(6)],max_length=25, blank=False)
    # # last password update date
    # last_updated = models.DateField()
    # # last_sign in date
    # last_sign_in = models.DateField()
    # # account setup date
    # created_on = models.DateTimeField(default=datetime.datetime.now())
    # # One time validation ?
    # is_email_validated = models.BooleanField()
    # is_phone_validated = models.BooleanField()

    def __str__(self):
        return self.email



