from django.urls import path

from .views import SnacksListView, SnacksDetailView, SnacksDeleteView, SnacksCreateView, SnacksUpdateView

urlpatterns = [
    path('',  SnacksListView.as_view(), name='snack_list'),
    path('<int:pk>/', SnacksDetailView.as_view(), name='snack_detail'),
    path('<int:pk>/delete', SnacksDeleteView.as_view(), name='snack_delete'),
    path('create/', SnacksCreateView.as_view(), name='snack_create'),
    path('<int:pk>/update', SnacksUpdateView.as_view(), name='snack_update')
]