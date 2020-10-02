from django.urls import path
from . import views
from .views import Store,Product
app_name ='store'
urlpatterns=[
    path('',Store.as_view(),name='Home'),
    path('search/',views.search,name='search'),
    path('product/<slug>/',Product.as_view(),name='product'),
]