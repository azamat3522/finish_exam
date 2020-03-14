from django.urls import path

from webapp.views import IndexView, FileView, FileCreateView, FileDeleteView, FileUpdateView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('file/<int:pk>/', FileView.as_view(), name='file_detail'),
    path('file/create/', FileCreateView.as_view(), name='file_create'),
    path('file/<int:pk>/delete/', FileDeleteView.as_view(), name='file_delete'),
    path('file/<int:pk>/update', FileUpdateView.as_view(), name='file_update'),
]
