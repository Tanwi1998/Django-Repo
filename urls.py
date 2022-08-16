from urllib import request
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.indexpage,name="indexpage"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login,name="login"),
    path("register/",views.registeruser,name="register"),
    path("otppage/",views.otp,name="otppage"),
    path("otpverify/",views.otpverify,name="otpverify"),
    path("loginuser/",views.loginuser,name="loginuser"),
    path("profile/<int:pk>",views.profile,name="profile"),
    path("logout/",views.logout,name="logout"),
    path("update_profile/<int:pk>",views.update_profile,name="update_profile"),
    
   
  
]