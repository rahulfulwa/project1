from django.urls import path
# remember here we are accessing all the file from polls app

from polls import views

urlpatterns = [
    path('', views.main_page, name="Main Page"),
    path('<int:ques_id>/details/', views.details, name="Details"),
    path('<int:ques_id>/results/', views.results, name="Results"),
    path('<int:ques_id>/vote/', views.vote, name="Vote"),
]
