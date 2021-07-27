from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('kontakt/', include('stronaglowna.urls')),
    path('admin/', admin.site.urls),


]
