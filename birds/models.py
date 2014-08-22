from django.db import models


class TaxonomicLevel(models.Model):
    name = models.CharField(max_length=20)
    depth = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.name


class TaxonomicGroup(models.Model):
    name = models.CharField(max_length=30, unique=True)
    common_name = models.CharField(max_length=50)
    level = models.ForeignKey(TaxonomicLevel)
    parent = models.ForeignKey('self', null=True, blank=True)
    position_within_siblings = models.PositiveSmallIntegerField(null=True)

    def __unicode__(self):
        return self.common_name if self.common_name else self.name


class Species(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    absolute_position = models.PositiveSmallIntegerField(null=True)
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey(TaxonomicGroup)
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
