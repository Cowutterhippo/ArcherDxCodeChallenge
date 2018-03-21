# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings

class BedFileModel(models.Model):
	bed_id = models.AutoField(primary_key=True)
	filename = models.CharField(max_length=300,null=True)
	track_name = models.CharField(max_length=300,null=True)
	bed_type = models.CharField(max_length=128,null=True)
	file_description = models.CharField(max_length=300, null=True)
	visibility = models.IntegerField(null=True)
	itemrgb = models.CharField(max_length=4,null=True)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	def __unicode__(self):
		return unicode(self.filename)

class BedData(models.Model):
	bedfilemodel = models.ForeignKey(BedFileModel, on_delete=models.CASCADE)
	specifiedchromosome	= models.CharField(max_length=300)
	chrom_start = models.BigIntegerField(null=True)
	chrom_end = models.BigIntegerField(null=True)
	bed_line_name = models.CharField(max_length=400, null=True)
	score = models.IntegerField(null=True)
	strand = models.CharField(max_length=2,null=True)
	thickstart = models.BigIntegerField(null=True)
	thickend = models.BigIntegerField(null=True)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	def __unicode__(self):
		return unicode(self.bedfilemodel)

