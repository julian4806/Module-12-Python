from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
import werken.views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', views.home, name='home'),
    path("", werken.views.home, name="home"),
    path("werken/", include("werken.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),  # gebruikers
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
