
from django.contrib import admin
from django.urls import path,include
#from khana.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("receipe.urls")),
]
