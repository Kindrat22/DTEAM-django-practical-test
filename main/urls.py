from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/cv', views.CVViewSet, basename='cv')

urlpatterns = [
    path('', views.cv_list, name='cv_list'),
    path('cv/<int:pk>/', views.cv_detail, name='cv_detail'),
    path('cv/<int:pk>/pdf/', views.cv_pdf, name='cv_pdf'),
    path('settings/', views.settings_page, name='settings_page'),
    path('', include(router.urls)),
]
