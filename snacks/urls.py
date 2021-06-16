from django.urls import path
from .views import (
    SnackView,
    SnackListView,
    SnackCreatView,
    SnackDetailView,
    SnackUpdateView,
    SnackDeleteView
)


urlpatterns = [
    path("", SnackView.as_view(), name = "home"),
    path("list", SnackListView.as_view(), name="snack_list"),
    path("create", SnackCreatView.as_view(), name="snack_create"),
    path("list/<int:pk>", SnackDetailView.as_view(), name="snack_detail"),
    path("<int:pk>/update", SnackUpdateView.as_view(), name="snack_update"),
    path("<int:pk>/delete", SnackDeleteView.as_view(), name="snack_delete"),
]


