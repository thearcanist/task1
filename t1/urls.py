from django.conf.urls import include,url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
admin.autodiscover()
from . import views

urlpatterns=(
   url(r'^api/$',views.TupleList.as_view()),
   
   url(r'^admin/',include(admin.site.urls)),
   url(r'^$',views.index,name='index')
);

urlpatterns=format_suffix_patterns(urlpatterns)
