from django.contrib import admin
from django.urls import path
from Room import views

urlpatterns = [
    path('', views.index,name='Room'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('contact',views.contact, name='contact'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
