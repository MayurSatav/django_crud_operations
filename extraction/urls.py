from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('create/', views.create, name='create' ),
    path('add_invoice/', views.add_invoice, name='add_invoice' ),
    path('delete/<id>/', views.delete, name='delete' ),
    path('edit/<id>/', views.edit, name='edit' ),
    path('update/<id>/', views.update, name='update' ),
]
