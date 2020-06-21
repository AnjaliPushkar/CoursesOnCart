# course-course123
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homepage1, name="homepage1"),
    # path("", views.login, name="login"),
    # path("newuser", views.newuser, name="newuser"),
    path('shop/', include('shop.urls')),
    # path('history/', include('history.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
