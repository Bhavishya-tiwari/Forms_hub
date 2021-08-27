from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from E_Form_app import views
urlpatterns = [
    path('', views.Home, name='Home'),
    path('createform', views.createform, name='createform'),
    path('createformdata', views.createformdata, name='createformdata'),
    path('previewform', views.previewform, name='previewform'),
    path('givedata/<int:ii>', views.givedata, name='givedata'),
    path('FormHub/<str:admin>/<int:id>', views.fillform, name='fillform'),
    path('logout', views.hlogout, name='logout'),
    
]
urlpatterns += staticfiles_urlpatterns()