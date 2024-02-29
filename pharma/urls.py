  
from django.urls import re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='index'),

    re_path(r'^dealerform/', views.dealerform, name="dealerform"),
    re_path(r'^dealerforminsert/', views.dealerforminsert, name="dealerforminsert"),
    re_path(r'^dealerformupdate(?P<foo>[0-9]+)/', views.dealerformupdate, name="dealerformupdate"),
    re_path(r'^dealerformview(?P<foo>[0-9]+)/', views.dealerformview, name="dealerformview"),
    re_path(r'^dealerformdelete(?P<foo>[0-9]+)/', views.dealerformdelete, name="dealerformdelete"),
    re_path(r'^dealertable/', views.dealertable, name='dealertable'),

    re_path(r'^medform/', views.medform, name="medform"),
    re_path(r'^medforminsert/', views.medforminsert, name="medforminsert"),
    re_path(r'^medformupdate(?P<foo>[0-9]+)/', views.medformupdate, name="medformupdate"),
    re_path(r'^medformview(?P<foo>[0-9]+)/', views.medformview, name="medformview"),
    re_path(r'^medformdelete(?P<foo>[0-9]+)/', views.medformdelete, name="medformdelete"),
    re_path(r'^medtable/', views.medtable, name='medtable'),

    re_path(r'^empform/', views.empform, name="empform"),
    re_path(r'^empforminsert/', views.empforminsert, name="empforminsert"),
    re_path(r'^empformupdate(?P<foo>[0-9]+)/', views.empformupdate, name="empformupdate"),
    re_path(r'^empformview(?P<foo>[0-9]+)/', views.empformview, name="empformview"),
    re_path(r'^empformdelete(?P<foo>[0-9]+)/', views.empformdelete, name="empformdelete"),
    re_path(r'^emptable/', views.emptable, name='emptable'),

    re_path(r'^custform/', views.custform, name="custform"),
    re_path(r'^custforminsert/', views.custforminsert, name="custforminsert"),
    re_path(r'^custformupdate(?P<foo>[0-9]+)/', views.custformupdate, name="custformupdate"),
    re_path(r'^custformview(?P<foo>[0-9]+)/', views.custformview, name="custformview"),
    re_path(r'^custformdelete(?P<foo>[0-9]+)/', views.custformdelete, name="custformdelete"),
    re_path(r'^custtable/', views.custtable, name='custtable'),

    re_path(r'^purchaseform/', views.purchaseform, name="purchaseform"),
    re_path(r'^purchaseforminsert/', views.purchaseforminsert, name="purchaseforminsert"),
    re_path(r'^purchaseformupdate(?P<foo>[0-9]+)/', views.purchaseformupdate, name="purchaseformupdate"),
    re_path(r'^purchaseformview(?P<foo>[0-9]+)/', views.purchaseformview, name="purchaseformview"),
    re_path(r'^purchaseformdelete(?P<foo>[0-9]+)/', views.purchaseformdelete, name="purchaseformdelete"),
    re_path(r'^purchasetable/', views.purchasetable, name='purchasetable'),
]
