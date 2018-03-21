# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings

# ['track_name', 'example_1',  'type', 'bed', description', 'example_1', 'visibility', '3', 'itemRgb', 'On']
# {0: 'chr1', 1: '115251158', 2: '115251275', 3: 'NRAS_NM_002524_exon_005_kJfGBiIv', 4: '0', 5: '-', 6: '115251158', 7: '115251275'}
#remember to convert the string values to numeric values 1,2,4,6,7


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

