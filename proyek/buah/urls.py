from django.urls import path

from .views import tambah_buah, list_buah, detail_buah, update_buah, delete_buah

app_name = "buah"

urlpatterns = [
    path('tambah/', tambah_buah, name="tambah_buah"),
    path('detail/<pk>/', detail_buah, name="detail_buah"),
    path('update/<pk>/', update_buah, name="update_buah"),
    path('delete/<pk>/', delete_buah, name="delete_buah"),
    path('', list_buah, name="list_buah"),
]