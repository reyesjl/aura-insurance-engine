from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/carriers/', views.get_carriers),
    path('api/v1/coverages/', views.get_coverages),
    path('api/v1/questions/', views.get_questions),
    path('api/v1/sessions/', views.get_sessions),
    path('api/v1/create-session/', views.create_session),
    path('api/v1/fill/<uuid:token>/', views.fill_session),
    path('api/v1/submit/<uuid:token>/', views.submit_form),
    path('api/v1/status/<uuid:token>/', views.get_status),
]
