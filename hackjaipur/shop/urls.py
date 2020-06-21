
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="ShopHome"),
    # path("", views.index.as_view(), name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    # path('<int:prod_id>', views.detail, name='detail'),
    path("search/", views.search, name="Search"),
    path("contact/", views.contact, name="ContactUs"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("blog/", views.blog, name="blog"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
