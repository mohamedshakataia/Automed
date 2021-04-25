from django.urls import path
from . import views



app_name='product'


urlpatterns = [
    path('' , views.Product_List.as_view()),
    path('<int:pk>', views.Product_Detail.as_view()),
    path('<str:name_category>', views.filter_by_category,name='filter_by_category'),

    ]