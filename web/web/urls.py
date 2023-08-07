"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from  dataextractor.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path("user_home",user_home,name="user_home"),
    path("logout",logout,name="logout"),
    path("feedback",feedback,name="feedback"),
    path("view_feedback",view_feedback,name="view_feedback"),
    path("delete_feedback/<int:id>", delete_feedback, name="delete_feedback"),
    path("delete_user/<int:id>", delete_user, name="delete_user"),

                  path("signup",signup,name="signup"),
    path("login",login,name="login"),
    path("admin_home",admin_home ,name="admin_home"),
    path("extrator",extrator,name="extrator"),
    path("view_user",view_user,name="view_user"),

    path("mobilephone_flipkart",mobilephone_flipkart,name="mobilephone_flipkart"),
    path("retrivemobilephone_flipkart",retrivemobilephone_flipkart,name="retrivemobilephone_flipkart"),
    path("retrive_specific_mobilephone_flipkart",retrive_specific_mobilephone_flipkart,name="retrive_specific_mobilephone_flipkart"),
    path("delete_mobilephone_flipkart",delete_mobilephone_flipkart,name="delete_mobilephone_flipkart"),

    path("laptop_flipkart", laptop_flipkart, name="laptop_flipkart"),
    path("retrivelaptop_flipkart", retrivelaptop_flipkart, name="retrivelaptop_flipkart"),
    path("retrive_specific_laptop_flipkart", retrive_specific_laptop_flipkart,name="retrive_specific_laptop_flipkart"),
    path("delete_laptop_flipkart", delete_laptop_flipkart, name="delete_laptop_flipkart"),

    path("interface_television_flipkart", interface_television_flipkart,name="interface_television_flipkart"),
    path("retrive_television_flipkart", retrive_television_flipkart, name="retrive_television_flipkart"),
    path("retrive_specific_telivision_flipkart", retrive_specific_telivision_flipkart,name="retrive_specific_telivision_flipkart"),
    path("delete_television_flipkart", delete_television_flipkart, name="delete_television_flipkart"),

    # *******************************************************Earphone**************************************************************
    path("earphone_flipkart", earphone_flipkart, name="earphone_flipkart"),
    path("retrive_earphone_flipkart", retrive_earphone_flipkart, name="retrive_earphone_flipkart"),
    path("retrive_specific_earphone_flipkart", retrive_specific_earphone_flipkart, name="retrive_specific_earphone_flipkart"),
    path("delete_earphone_flipkart", delete_earphone_flipkart, name="delete_earphone_flipkart"),

    # **************************************************Bike****************************************************************
    path("bike_flipkart", bike_flipkart, name="bike_flipkart"),
    path("retrive_bike_flipkart", retrive_bike_flipkart, name="retrive_bike_flipkart"),
    path("retrive_specific_bike_flipkart", retrive_specific_bike_flipkart,name="retrive_specific_bike_flipkart"),
    path("delete_bike_flipkart", delete_bike_flipkart, name="delete_bike_flipkart"),

                  # **************************************************Washing Machine****************************************************************
    path("washing_machine_flipkart", washing_machine_flipkart, name="washing_machine_flipkart"),
    path("retrive_washing_machine_flipkart", retrive_washing_machine_flipkart, name="retrive_washing_machine_flipkart"),
    path("delete_washing_machine_flipkart", delete_washing_machine_flipkart,name="delete_washing_machine_flipkart"),
    path("reterive_specific_washingmachine_flipkart", reterive_specific_washingmachine_flipkart,name="reterive_specific_washingmachine_flipkart"),
    path("user_extrator",user_extrator,name="user_extrator"),
    path("telivion_view",telivion_view,name="telivion_view"),
    path("laptop_view",laptop_view,name="laptop_view"),
    path("mobile_view",mobile_view,name="mobile_view"),
    path("bike_view",bike_view,name="bike_view"),
    path("washingmachine_view",washingmachine_view,name="washingmachine_view"),
    path("earphone_view",earphone_view,name="earphone_view"),




              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

