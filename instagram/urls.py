from django.conf.urls import url
from . import views

urlpatterns=[
    url(r"^$",views.index,name="home"),
    url(r"stories/$",views.stories,name="stories"),
    url(r"profile/$",views.profile,name="profile"),
    url(r'profile/upload$',views.uploads,name='uploads')
]
