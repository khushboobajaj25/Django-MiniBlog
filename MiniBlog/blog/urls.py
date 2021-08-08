
from django.urls import path
from blog import views

urlpatterns = [
    path("",  views.home),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("accounts/register/", views.register, name="register"),
    path("accounts/login/", views.signin, name="login"),
    path("accounts/logout/", views.signout,name="logout"),
    path("addpost/", views.add_new_post,name="addpost"),
    path("update/<id>", views.update_post,name="updatepost"),
    path("delete/<id>", views.delete_post,name="deletepost"),


]
