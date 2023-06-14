from attending import views
from django.urls import path

urlpatterns = [
    path('attending/', views.AttendingList.as_view()),
    path('attending/<int:pk>/', views.AttendingDetail.as_view()),
]
