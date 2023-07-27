from .import views
from django.urls import path

urlpatterns=[
    path('',views.home,name="home"),
    # path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('register/',views.register,name="register"),
    path('record/<int:pk>',views.record,name="record"),
    path('delete_record/<int:pk>',views.delete,name="delete"),
    path('add_record',views.add_record,name="add_record"),
    path('update_record/<int:pk>',views.update_record,name="update_record"),
]