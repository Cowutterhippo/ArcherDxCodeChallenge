from django.conf.urls import url
from . import views as genome_views

urlpatterns = [
    url(r'^upload$', genome_views.upload, name='upload'),
]
