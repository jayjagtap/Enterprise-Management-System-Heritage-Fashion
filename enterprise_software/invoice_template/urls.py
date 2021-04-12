from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('sample/', views.populate_invoice_template, name='populate_invoice_template'),
    path('print/', views.print_invoice, name='print_invoice'),
]
