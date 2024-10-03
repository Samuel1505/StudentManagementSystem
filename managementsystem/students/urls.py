from  django.urls import path
from students.views import HomePage, CreatePage, UpdatePage, DeletePage

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("create", CreatePage.as_view(), name="create"),
    path("update/<int:pk>/", UpdatePage.as_view(), name="update"),
    path("delete/<int:pk>/", DeletePage.as_view(), name="delete"),
]