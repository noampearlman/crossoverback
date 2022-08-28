from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', views.getRoutes),
    
    path('cons/', views.getCons),
    path('addcon/', views.addCon),
    path('delcon/<con_id>', views.delCon),

    path('props/', views.getProps),
    path('addprop/', views.addProp),
    path('delprop/<prop_id>', views.delProp),
    
    path('types/', views.getTypes),
    path('addtype/', views.addType),
    
    path('dirs/', views.getDirs),
    path('adddir/', views.addDir),

    # path('users/', views.getUsers),
    path('adduser/', views.addUser),
 
 
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    
    # path('notes/', views.getNotes),
    # path('addnote/', views.addNote),

    # path('kids/', views.getKids),
    # path('addkid/', views.addKid),
]
