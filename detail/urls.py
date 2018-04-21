from django.urls import path
from detail.views import simple_view,Bank,Banklist

urlpatterns={
    path('',simple_view),
    path('Bank',Bank),
    path('Banklist',Banklist),
}