from django.db.models import Model, IntegerField, CharField, EmailField, FloatField
from django_google_maps import fields as map_fields

class Customer(Model):
    """
        Customer Model
    """
    id = IntegerField(primary_key=True, null=False)
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    email = EmailField(max_length=100)
    gender = CharField(max_length=50, choices=[('Male', 'Male'), ('Female', 'Female')])
    company = CharField(max_length=100)
    city = CharField(max_length=100)
    title = CharField(max_length=100)
    latitude = map_fields.AddressField(max_length=200)
    longitude = map_fields.AddressField(max_length=200)

    def __str__(self):
        return '<Customer %s >' % self.email
