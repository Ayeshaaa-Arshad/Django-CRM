from website import views
from django.urls import path

urlpatterns=[
    path('',views.HomeView.as_view(),name="home"),
    # path('login/',views.login_view,name="login"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
    path('register/',views.RegisterView.as_view(),name="register"),
    path('record/<int:pk>',views.RecordView.as_view(),name="record"),
    path('delete_record/<int:pk>',views.DeleteRecordView.as_view(),name="delete"),
    path('add_record',views.AddRecordView.as_view(),name="add_record"),
    path('update_record/<int:pk>',views.UpdateRecordView.as_view(),name="update_record"),
]
