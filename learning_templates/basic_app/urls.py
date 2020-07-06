from django.conf.urls import url
from . import views

###TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    url('index/', views.index, name='index'),
    url('other/', views.other, name='other'),
    url('relative/', views.relative, name='relative_url_templates'),
]
