from django.urls import path

from . import views  # learn news

app_name = 'learn'

urlpatterns = [
    path('', views.index, name="home"),
    path('add/', views.add, name='add'),  # get
    
    path('add2/<int:a>/<int:b>/',views.add2,name="add2"),
    path('add/<int:a>/<int:b>/', views.old_add2_redirect),
    path('new_add/<int:a>/<int:b>/', views.add2, name='add2'),
    path('jiafa/<int:a>/<int:b>/', views.add2, name='add2'),
    path('grade', views.getGrades, name='grade'),
]
