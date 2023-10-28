from django.urls import path

from .views import ContactViewSet

urlpatterns = [
    path('', ContactViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='contact-list'),
    path('<int:id>', ContactViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='contact-detail'),
]
