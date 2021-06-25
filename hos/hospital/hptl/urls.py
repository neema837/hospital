from . import views
from django.urls import path

urlpatterns = [
    path('', views.doclist, name='doclist'),
    path('<slug:d_slug>/', views.doclist, name='product_by_dept'),
]
