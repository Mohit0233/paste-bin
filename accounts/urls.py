from django.urls import path

from accounts import views


app_name = "accounts"


urlpatterns = [

    path('login', views.LoginView.as_view(), name="loginView"),
    path('logout', views.LogoutView.as_view(), name="logoutView"),
    # path('signup', views.SignUpView.as_view(), name="singUpView"),

]
