from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('eligibility/', include('eligibility.urls')),
    path('accounts/', include('accounts.urls')),
    path('schemes/', include('schemes.urls')),
    
]
