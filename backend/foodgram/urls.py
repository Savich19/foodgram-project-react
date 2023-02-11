from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # hz
    # path('', views.index),
    # path('ice_cream/', views.ice_cream_list),
    # path('ice_cream/<pk>/', views.ice_cream_detail),
    path('api/', include('api.urls', namespace='api')),
]
