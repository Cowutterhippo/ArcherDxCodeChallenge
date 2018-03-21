from django.conf.urls import url
from . import BedFileUploadController as genome_views

urlpatterns = [
    url(r'^upload$', genome_views.upload_view, name='upload-view'),
    url(r'^ajax-upload$', genome_views.ajax_uploader, name='ajax-upload'),
    url(r'^bed-analytics$', genome_views.bed_analytics, name='bed-analytics'),
    url(r'^get-bedfiles$', genome_views.get_all_bedfiles_from_sql, name='get-bedfiles'),
]