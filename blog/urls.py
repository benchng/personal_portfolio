from django.urls import path
from . import views
#from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

app_name = 'blog'

urlpatterns = [
    # Creating Home Page
    path('', views.index, name='index'),
    path("blog/", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("blog/<category>/", views.blog_category, name="blog_category"),

]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()