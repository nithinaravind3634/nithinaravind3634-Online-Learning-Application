from django.urls import path
from . views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',index),
    path('loginindex/',loginindex),
    path('teacherlogin/',teacherlogin),
    path('studentlogin/',studentlogin),
    path('studentregister/',studentregister),
    path('teacherregister/',teacherregister),
    path('postvideo/<str:username>/',postvideo, name='postvideo'),
    path('logout/',logout_view),
    path('postfile/<str:username>/',postfile, name='postfile'),
    path('uiux/',uiux),
    path("python/",python),
    path("angular/",angular),
    path('reactjs/',reactjs),
    path("nodejs/",nodejs),
    path("django/",django),
    path('viewresponse/<str:username>/',viewresponse, name='viewresponse'),
    path('postresponse/<str:teachername>/<path:videotopic>/<path:videodescription>/', postresponse, name='postresponse'),
    path('myuploads/<str:username>/',myuploads, name='myuploads'),
    path("delete/<int:id>/",delitem)





]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)