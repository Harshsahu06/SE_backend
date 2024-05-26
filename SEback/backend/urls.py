from django.contrib import admin
from django.urls import path

# from SE_backend.SEback.SEback import settings
from . import views

urlpatterns = [
    # for passing arguments in urls
    # path("user/<str:id>/<str:name>",views.userdata,name="data"),
    path("user/<int:pk>",views.userdata,name="data"),
    path("hospital",views.hospitaldata,name="hospitaldata"),
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup1"),
    # path("/medical",views.medicaldata,name="medical"),    
]
# +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)