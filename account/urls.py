from django.urls import path
from account.views import login_request,register_request,index,logout_request,instagram


urlpatterns = [
    path('login/',login_request,name="login"),
    path('register/',register_request, name='register'),
    path('',index, name='index'),
    path('logout/',logout_request, name='logout'),
    path('instagram/',instagram, name='instagram'),
] 