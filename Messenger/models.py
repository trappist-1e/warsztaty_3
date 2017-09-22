from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    address = models.ForeignKey('Address', null=True)


class Address(models.Model):
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    building_nr = models.CharField(max_length=10)
    flat_nr = models.CharField(max_length=10)


class PhoneNumber(models.Model):
    types = ((1, 'home'), (2, 'work'), (3, 'other'))
    phone_number = models.CharField(max_length=128)
    type = models.IntegerField(choices=types)
    person = models.ForeignKey(Person)


class Email(models.Model):
    types = ((1, 'home'), (2, 'work'), (3, 'other'))
    email = models.CharField(max_length=128)
    type = models.IntegerField(choices=types)
    person = models.ForeignKey(Person)
