from django.db import models

PACKAGE_TYPE = (
    ('Nylon', 'Nylon'),
    ('Paper', 'Paper'),
    ('Sealed', 'Sealed'),
    ('Bottle', 'Bottle'),
)


class Label(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % (self.name,)


class Product(models.Model):
    name = models.CharField(max_length=100)
    label = models.ForeignKey(Label)
    manufactured_date = models.DateField()
    shipped_date = models.DateField()
    expiracy_date = models.DateField()
    weight = models.IntegerField()
    package_type = models.CharField(
        choices=PACKAGE_TYPE, blank=True, max_length=100
    )

    def __unicode__(self):
        return "%s" % (self.name, )
