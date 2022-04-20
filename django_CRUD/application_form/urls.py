from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactList.as_view(), name='contact_list'),
    path('create', views.ContactCreate.as_view(), name='contact_create'),
    path('contact/<int:pk>', views.ContactDetail.as_view(), name='contact_detail'),
    path('update/<int:pk>', views.ContactUpdate.as_view(), name='contact_update'),
    path('delete/<int:pk>', views.ContactDelete.as_view(), name='contact_delete'),
]
