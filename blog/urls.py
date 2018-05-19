from django.urls import path

from blog.views import IndexView, ArchivesView, CategoryView
from . import views

app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>', ArchivesView.as_view(), name='archives'),
    path('category/<int:pk>', CategoryView.as_view(), name='categories'),
]