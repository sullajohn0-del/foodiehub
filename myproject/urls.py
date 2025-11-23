"""
URL configuration for myproject project.
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('restaurant/<slug:slug>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/<slug:restaurant_slug>/item/<int:item_id>/', views.menu_item_detail, name='menu_item_detail'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
