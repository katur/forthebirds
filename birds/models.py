from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name


class Family(models.Model):
    name = models.CharField(max_length=30, unique=True)
    common_name = models.CharField(max_length=50)
    order = models.ForeignKey(Order)

    def __unicode__(self):
        return self.name


class Subfamily(models.Model):
    name = models.CharField(max_length=30, unique=True)
    family = models.ForeignKey(Family)

    def __unicode__(self):
        return self.name


class Genus(models.Model):
    name = models.CharField(max_length=30, unique=True)
    subfamily = models.ForeignKey(Subfamily)

    def __unicode__(self):
        return self.name


class Species(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    genus = models.ForeignKey(Genus)
    common_name = models.CharField(max_length=50)
    french_name = models.CharField(max_length=50)
    nacc_annotation = models.TextField()
    nacc_is_accidental = models.NullBooleanField()
    nacc_is_hawaiian = models.NullBooleanField()
    nacc_is_introduced = models.NullBooleanField()
    nacc_is_nonbreeding = models.NullBooleanField()
    nacc_is_extinct = models.NullBooleanField()
    nacc_is_misplaced = models.NullBooleanField()

    def __unicode__(self):
        return self.name
