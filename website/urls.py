from website import views
from django.urls import path

urlpatterns=[
    path('',views.home.as_view(),name="home"),
    # path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view.as_view(),name="logout"),
    path('register/',views.register.as_view(),name="register"),
    path('record/<int:pk>',views.record.as_view(),name="record"),
    path('delete_record/<int:pk>',views.delete.as_view(),name="delete"),
    path('add_record',views.add_record.as_view(),name="add_record"),
    path('update_record/<int:pk>',views.update_record.as_view(),name="update_record"),
]
