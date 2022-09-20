from django.urls import path
from . import views


urlpatterns = [
    path('flight-data/', views.getFlights, name="routes"),
    path('update-review/', views.updateReview, name="update_review"),
    path('data-page/', views.dataPage.as_view(), name="data_page"),

]