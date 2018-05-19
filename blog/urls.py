from django.urls import path

from blog.views import IndexView, ArchivesView, CategoryView, PostDetailView
from . import views

app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('archives/<int:year>/<int:month>', ArchivesView.as_view(), name='archives'),
    path('category/<int:pk>', CategoryView.as_view(), name='categories'),
]