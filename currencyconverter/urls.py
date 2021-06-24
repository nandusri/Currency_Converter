from converter import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('convert/', views.CurrencyConverter.as_view()),
]
