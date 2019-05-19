from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns=[
    url(r"^$",views.index,name="home"),
    url(r"stories/$",views.stories,name="stories"),
    url(r"profile/$",views.profile,name="profile"),
    url(r'profile/upload$',views.uploads,name='uploads'),
    url(r'profile/edit$',views.edit,name='edit'),
    url(r'stories/comment/(\d+)/$',views.comments,name='comment'),
    url(r'profile/user/(\d+)/$',views.other_users,name='users'),
    url(r"^search/",views.search,name="search")
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
