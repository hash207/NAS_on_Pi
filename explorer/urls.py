from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_explorer, name='explorer_root'),
    path('explore/<path:path>', views.file_explorer, name='explorer'),
    path('serve/<path:path>', views.serve_file, name='serve_file'),
]
