from django.db import models


class AvailablePrimers(models.Model):
    CHROM = models.CharField(max_length=200)
    POS = models.CharField(max_length=200)
    Primer = models.CharField(max_length=200)


class UnavailablePrimers(models.Model):
    CHROM = models.CharField(max_length=200)
    POS = models.CharField(max_length=200)


class ResultFiles(models.Model):
    vcf = models.FileField(upload_to='files')
    bed = models.FileField(upload_to='files')
