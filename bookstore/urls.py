from django.urls import path
from .views import BookViewSet, JournalViewSet

urlpatterns = [
    path('books/', BookViewSet.as_view({
        'get':'list',
        'post' : 'create'
        })),
    path('books/<int:pk>/', BookViewSet.as_view({
            'get' : 'retrieve',
            'put' : 'update',
            'delete' : 'destroy'
        })),
    path('journals/', JournalViewSet.as_view({
        'get':'list',
        'post' : 'create'
        })),
    path('journals/<int:pk>/', JournalViewSet.as_view({
            'get' : 'retrieve',
            'put' : 'update',
            'delete' : 'destroy'
        })),
]