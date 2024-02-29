from django.urls import re_path, include
from django.contrib import admin
from pharma import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^pharma/', include('pharma.urls')),
    re_path(r'^$', views.home, name='index'),
]