from django.urls import path
from . import views

urlpatterns = [
    path('', views.populate_invoice_template, name='populate_invoice_template'),
]
