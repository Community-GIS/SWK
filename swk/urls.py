from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.HomePage, name = 'Swacch Worli Koliwada'),
    # path('adminlogin/', views.login_view, name='adminlogin'),
    url (r'^aboutus/', views.AboutUs, name = 'AboutUs'),
    path('adminlogin/', views.user_login, name='adminlogin'),
    # path ('adminlogin/trackform/', views.TracksheetPage, name = 'TracksheetPage'),
    # url(r'^trackform/',views.TracksheetPage, name = 'trackform'),
    url(r'^trackform/', views.TracksheetPage, name = "trackform"),
    # url(r'^multipleforms/',views.MultipleForms, name = "multipleforms"),
    # url(r'^form1/',views.form1, name = "form1"),
    # url(r'^form2/',views.form2, name = "form2"),

]

