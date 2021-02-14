
from django.contrib import admin
from django.urls import path
# from Product.views import (product_Landing_View,check_Out,success,cancel)
from Product.views import *

# checkOut_Session_View,
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',product_Landing_View,name='product_Landing_View'),
    path('success/',success.as_view(),name='success'),
    path('cancel/',cancel.as_view(),name='cancel'),
    path('check_Out',check_Out,name='check_Out'),
]
